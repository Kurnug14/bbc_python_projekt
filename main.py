import tkinter as tk
from json_test import *
# Function to center a window on the screen
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # Calculate the position to center the window
    x_coordinate = int((screen_width / 2) - (width / 2))
    y_coordinate = int((screen_height / 2) - (height / 2))
    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

def correct_answer(answer_window):
    card_data = load_json(card)
    card_data['Level'] += 1
    mod_json(card, card_data['Level'])
    answer_window.destroy()

def false_answer(answer_window):
    card_data = load_json(card)
    card_data['Level'] = 1
    mod_json(card, card_data['Level'])
    answer_window.destroy()
# Function to show the answer window
def show_answer():
    #Close and load the window
    root.destroy()
    card_data = load_json(card)
    answer_window = tk.Tk()
    answer_window.title("Flashcard - Answer")
    center_window(answer_window, 400, 200)
    # Add a label to display the answer
    answer_label = tk.Label(answer_window, text=f"Antwort: {card_data['Antwort']}", font=("Arial", 12), wraplength=300)
    answer_label.pack(pady=20)
    # Create a frame to hold the buttons side by side and create the buttons with their functionality
    button_frame = tk.Frame(answer_window)
    button_frame.pack(pady=10)
    korrekt_button = tk.Button(button_frame, text="Korrekt", font=("Arial", 12),
                               command=lambda: correct_answer(answer_window))
    korrekt_button.pack(side=tk.LEFT, padx=10)
    falsch_button = tk.Button(button_frame, text="Falsch", font=("Arial", 12),
                              command=lambda: false_answer(answer_window))
    falsch_button.pack(side=tk.LEFT, padx=10)

# Function to show the question
def show_question():
    card_data = load_json(card)
    root.title("Flashcard - Question")
    center_window(root, 400,200)
    question_label = tk.Label(root, text=f"Frage: {card_data['Frage']}", font=("Arial", 12), wraplength=300)
    question_label.pack(pady=20)
    show_answer_button = tk.Button(root, text="Zeige Antwort", command=show_answer, font=("Arial", 12))
    show_answer_button.pack(pady=10)
    close_button = tk.Button(root, text="Schliessen", command=root.destroy, font=("Arial", 12))
    close_button.pack(pady=10)
    root.mainloop()

# Main window
current_set = randomized_dic()
for card in current_set:
    root = tk.Tk()
    show_question()