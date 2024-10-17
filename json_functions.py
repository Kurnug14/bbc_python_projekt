import json
import random
from typing import Union


#Make an object that stores the functions and variables necessary to do a learning flashcard session

class ActiveSet :
    def __init__(self, set_name):
        self.active_set = set_name
    #randomize the set
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
    #load the card information
    def load_json(self, indexc):
        f = open(self.active_set)
        indexc = str(indexc)
        data = json.load(f)
        f.close()
        return data[indexc]
    #modify the level of a card
    def mod_json(self,index_card, level):
        json_file = open(self.active_set)
        data = json.load(json_file)
        json_file.close()
        data[index_card]["Level"] = level
        json_file_write = open(self.active_set, "w")
        between = json.dumps(data, indent=4)
        json_file_write.write(between)
        json_file_write.close()
        print (index_card, level)

class NewSet:
    def __init__(self):
        self.cards = {}
        self.index = 1
    def add_new_card(self, question, awnser):
        self.cards[self.index] = {"Frage": question, "Level": 1, "Antwort": awnser}
        self.index += 1
    def make_set(self, new_set):
        json_cards = json.dumps(self.cards, indent=4)
        json_new_name = new_set+".json"
        json_file = open("sets/"+json_new_name, "x")
        json_file.write(json_cards)
        json_file.close()