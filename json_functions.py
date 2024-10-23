import json
import random
from textwrap import indent
from typing import Union

#Um das Zugreifen zu vereinfachen als auch die Informationen konstant zu behalten, wird OOP verwendet. Diese Klasse wird verwendet um ein vorhandenes Set auszuwählen
class ActiveSet :

    def __init__(self, set_name):
        self.active_set = set_name

    #Mischt ein Set durch
    def randomized_dic(self):
        json_file = open(self.active_set)
        data = json.load(json_file)
        json_file.close()
        returnDict= {}
        for x in data:
            chance = 1 / data[x]['Level']
            if random.random() < chance:
                returnDict[x] = data[x]
        temp = list(returnDict.items())
        random.shuffle(temp)
        returnDict = dict(temp)
        return returnDict

    #Ladet die Informatien von einer JSON-Datei und konvertiert duese zu einem Dictionary
    def load_json(self, indexc):
        f = open(self.active_set)
        indexc = str(indexc)
        data = json.load(f)
        f.close()
        return data[indexc]

    #Modifiziert die Levels
    def mod_json(self,index_card, level):
        json_file = open(self.active_set)
        data = json.load(json_file)
        json_file.close()
        data[index_card]["Level"] = level
        json_file_write = open(self.active_set, "w")
        between = json.dumps(data, indent=4)
        json_file_write.write(between)
        json_file_write.close()

    #Gibt eine geordnet Liste zurück
    def list_set(self):
        json_file = open(self.active_set)
        data = json.load(json_file)
        json_file.close()
        full_dic = dict(data)
        short_dic = {}
        for index in full_dic:
            short_dic[index] = {full_dic[index]["Frage"]}
        return full_dic

    #Überschreibt eine JSON-Datei
    def safe_set_changes(self, cards):
        json_file = open(self.active_set, "w")
        json_cards = json.dumps(cards, indent=4)
        json_file.write(json_cards)
        json_file.close()


#Funktionalität für ein neues Set zu erstellen
class NewSet:
    def __init__(self):
        self.cards = {}
        self.index = 1

    #Formatiert die übergebene Dateen
    def add_new_card(self, question, awnser):
        self.cards[self.index] = {"Frage": question, "Level": 1, "Antwort": awnser}
        self.index += 1
    #Erstellt eine neue JSON-Datei
    def make_set(self, new_set):
        json_cards = json.dumps(self.cards, indent=4)
        json_new_name = new_set+".json"
        json_file = open("sets/"+json_new_name, "x")
        json_file.write(json_cards)
        json_file.close()