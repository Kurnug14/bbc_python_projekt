import json
import random

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

def save_to_json(set_name, set_card):
    json_card = json.dumps(set_card, indent=4)
    file_end = ".json"

    json_file = open("sets/"+set_name+file_end, "x")
    json_file.write(json_card)
    json_file.close()