import json
import random

def randomized_dic():
    json_file = open("sets/randomized_json_25_entries.json")
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

def save_to_json():
    set_name = {
        0 : {
            "Frage":"bliblablub",
            "Level" : 42,
            "Antwort":"ehhh",
            "random":"Whooo"
        },
        1 : {
            "Frage":"test",
            "Level" : 420,
            "Antwort":"new",
            "random":"question"
        }
    }
    json_card = json.dumps(set_name, indent=4)
    file_end = ".json"
    file_name = input("Name der Datei eingeben: ")

    json_file = open("sets/"+file_name+file_end, "x")
    json_file.write(json_card)
    json_file.close()

def load_json(indexc):
    f = open("sets/randomized_json_25_entries.json")
    indexc = str(indexc)
    data = json.load(f)
    f.close()
    return data[indexc]

def get_size_set():
    return;

def mod_json(index_card, level):
    json_file = open("sets/randomized_json_25_entries.json")
    data = json.load(json_file)
    json_file.close()
    data[index_card]["Level"] = level
    json_file_write = open("sets/randomized_json_25_entries.json", "w")
    between = json.dumps(data, indent=4)
    json_file_write.write(between)
    json_file_write.close()