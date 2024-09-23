from json_functions import *
import tkinter
from tkinter.filedialog import *
def test_new_set():
    end_loop = True
    new_set = {}
    index_card = 1
    set_name = input("give me the set name")
    while end_loop:
        ask_cont = input("Do you want to continue? y/n ")
        if ask_cont == "n":
            end_loop = False
            continue
        level_constant = 1
        question = input("Give me the question")
        answer = input("Give me the answer to that")
        new_set[index_card] = {"Frage":question, "Level":level_constant, "Antwort":answer}
        index_card += 1
    print(new_set)
    save_to_json(set_name, new_set)
def main_menu():
    f_path = askopenfilename(initialdir="./sets", title="Select File", filetypes=(("JSON files", "*.json*"), ("All Files", "*.*")))
    print(f_path)
main_menu()