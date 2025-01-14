import tkinter as tk
import json_functions
from tkinter.filedialog import askopenfilename
current_set = None
cancel_button = False

def cancel (window):
    window.destroy()
    global cancel_button
    cancel_button = True

# Funktion welche die Fenster standartisiert
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (width / 2))
    y_coordinate = int((screen_height / 2) - (height / 2))
    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")
    window.attributes('-topmost', True)
# GUI mit der Funktionalität neue Sets zu machen
def new_card_gui():
    new_set = json_functions.NewSet()
    new_card_window = tk.Tk()
    new_card_window.title("Neues Set erstellen")
    def addcard():
        new_set.add_new_card(question_input.get(), awnser_input.get())
        question_input.delete(0, "end")
        awnser_input.delete(0, "end")
    def make_set():
        new_set.make_set(setname_input.get())
        new_card_window.destroy()
    center_window(new_card_window, 400, 200)

    setname_label = tk.Label(new_card_window, text= "Set Name:", font=("Arial", 12))
    setname_label.grid(row=0, column=0, padx=10, pady=10)
    setname_input = tk.Entry(new_card_window, width=45)
    setname_input.grid(row=0, column=1, padx = 10, pady=10)

    question_label = tk.Label(new_card_window, text= "Frage:", font=("Arial", 12))
    question_label.grid(row=1, column=0, padx=10, pady=10)
    question_input = tk.Entry(new_card_window, width=45)
    question_input.grid(row=1, column=1, padx = 10, pady=10)

    awnser_label = tk.Label(new_card_window, text= "Antwort:", font=("Arial", 12))
    awnser_label.grid(row=2, column=0, padx=10, pady=10)
    awnser_input = tk.Entry(new_card_window, width=45)
    awnser_input.grid(row=2, column=1, padx = 10, pady=10)

    button_frame = tk.Frame(new_card_window)
    button_frame.grid(row=3, column=0, columnspan=2, pady=10)
    another_card_button = tk.Button(button_frame, text="Zum Set hinzufügen", font=("Arial", 12), command=lambda: addcard())
    another_card_button.pack(side=tk.LEFT, padx=10, ipadx = 10)
    end_set_button = tk.Button(button_frame, text="Set machen beenden", font=("Arial", 12), command=lambda: make_set())
    end_set_button.pack(side=tk.LEFT, padx=10, ipadx = 10)
    new_card_window.mainloop()

#Funktionen die Parameter übergeben basierend auf dem Input. Diese modifizieren den Level Attribut
def correct_answer(answer_window, card):
    card_data = current_set.load_json(card)
    card_data['Level'] += 1
    current_set.mod_json(card, card_data['Level'])
    answer_window.destroy()

def false_answer(answer_window, card):
    card_data = current_set.load_json(card)
    card_data['Level'] = 1
    current_set.mod_json(card, card_data['Level'])
    answer_window.destroy()

# Funktion welche die Antwort der Karte anzeigen
def show_answer(question_window, card):
    card_data = current_set.load_json(card)
    answer_window = tk.Tk()
    answer_window.title("Flashcard - Answer")
    center_window(answer_window, 400, 200)
    answer_label = tk.Label(answer_window, text=f"Antwort: {card_data['Antwort']}", font=("Arial", 12), wraplength=300)
    answer_label.pack(pady=20)
    button_frame = tk.Frame(answer_window)
    button_frame.pack(pady=10)
    correct_button = tk.Button(button_frame, text="Korrekt", font=("Arial", 12),
                               command=lambda: correct_answer(answer_window, card))
    correct_button.pack(side=tk.LEFT, padx=10)
    false_button = tk.Button(button_frame, text="Falsch", font=("Arial", 12),
                              command=lambda: false_answer(answer_window, card))
    false_button.pack(side=tk.LEFT, padx=10)
    question_window.destroy()

# Gibt den User die Frage
def show_question(card):
    question_window = tk.Tk()
    card_data = current_set.load_json(card)
    question_window.title("Karte - Frage")
    center_window(question_window, 400,200)
    question_label = tk.Label(question_window, text=f"Frage: {card_data['Frage']}", font=("Arial", 12), wraplength=300)
    question_label.pack(pady=20)
    show_answer_button = tk.Button(question_window, text="Zeige Antwort", command=lambda: show_answer(question_window, card), font=("Arial", 12) )
    show_answer_button.pack(pady=10)
    close_button = tk.Button(question_window, text="Abbrechen", command=lambda: cancel(question_window), font=("Arial", 12))
    close_button.pack(pady=10)
    question_window.mainloop()

def choose_set():
    f_path = askopenfilename(initialdir="./sets", title="Select File",
                             filetypes=(("JSON files", "*.json*"), ("All Files", "*.*")))
    return(f_path)
# Flashcard learning loop
def initiate_loop(mainmenu):
    mainmenu.destroy()
    flashcard_loop()

def flashcard_loop():
    global current_set
    global cancel_button
    current_set = json_functions.ActiveSet(choose_set())
    try:
        for card in current_set.randomized_dic():
            show_question(card)
            if cancel_button:
                cancel_button = False
                break
    except FileNotFoundError:
        tk.messagebox.showwarning(title="Keine Gültige JSON Datei ausgewählt", message="Bitte wähle eine gültige JSON Datei aus.")
        flashcard_loop()
    main_menu()

#Fenster mit der Fähigkeiten die Karten in einem Set zu bearbeiten
def modify_set():
    set_var = choose_set()
    mod_set = json_functions.ActiveSet(set_var)
    mod_card_window = tk.Tk()
    mod_card_window.title("Karten überarbeiten")
    card_full_info = mod_set.list_set()
    option_list = [f"{key}: {data['Frage']}" for key, data in card_full_info.items()]

    def get_card_infos(key, *args):
        question_input.delete(0, tk.END)
        question_input.insert(0, f"{card_full_info[key]['Frage']}")
        awnser_input.delete(0, tk.END)
        awnser_input.insert(0, f"{card_full_info[key]['Antwort']}")

    def change_card(awnser, question, key):
        card_full_info[key]['Frage'] = question
        card_full_info[key]['Antwort']=awnser

    def commit_change():
        mod_set.safe_set_changes(card_full_info)
        mod_card_window.destroy()
        main_menu()

    center_window(mod_card_window, 400, 200)
    card_label = tk.Label(mod_card_window, text="Karte:", font=("Arial", 12))
    card_label.grid(row=0, column=0, padx=10, pady=10)

    string_var_dropdown = tk.StringVar(mod_card_window, "Wähle eine Karte aus")
    string_var_dropdown.trace("w", lambda *args: get_card_infos(string_var_dropdown.get().split(":")[0]))
    card_choice = tk.OptionMenu(mod_card_window, string_var_dropdown, *option_list)
    card_choice.config(width=40)
    card_choice.grid(row=0, column=1, padx=10, pady=10)

    question_label = tk.Label(mod_card_window, text="Frage:", font=("Arial", 12))
    question_label.grid(row=1, column=0, padx=10, pady=10)
    question_input = tk.Entry(mod_card_window, width=45)
    question_input.grid(row=1, column=1, padx=10, pady=10)

    awnser_label = tk.Label(mod_card_window, text="Antwort:", font=("Arial", 12))
    awnser_label.grid(row=2, column=0, padx=10, pady=10)
    awnser_input = tk.Entry(mod_card_window, width=45)
    awnser_input.grid(row=2, column=1, padx=10, pady=10)

    button_frame = tk.Frame(mod_card_window)
    button_frame.grid(row=3, column=0, columnspan=2, pady=10)
    another_card_button = tk.Button(button_frame, text="Karte Speichern", command=lambda: change_card(awnser_input.get(), question_input.get(), string_var_dropdown.get().split(":")[0]), font=("Arial", 12))
    another_card_button.pack(side=tk.LEFT, padx=10, ipadx=10)
    end_set_button = tk.Button(button_frame, text="Verarbeitung beenden", command=lambda: commit_change(), font=("Arial", 12))
    end_set_button.pack(side=tk.LEFT, padx=10, ipadx=10)
    mod_card_window.mainloop()

def main_menu():
    main_window = tk.Tk()
    main_window.title("Hauptmenü")
    center_window(main_window, 400, 200)
    frame = tk.Frame(main_window)
    frame.pack(expand=True, fill='both', padx=20, pady=20)
    learn_button = tk.Button(frame, text="Lernen", command= lambda: initiate_loop (main_window))
    learn_button.pack(pady=10, fill="x", padx=20, expand=True)
    newset_button = tk.Button(frame, text="Neues Set erstellen", command=lambda: new_card_gui())
    newset_button.pack(pady=10, fill="x", padx=20, expand=True)
    editset_button = tk.Button(frame, text="Set Verarbeiten", command=lambda: modify_set())
    editset_button.pack (pady=10, fill="x", padx=20, expand=True)
    main_window.mainloop()

main_menu()