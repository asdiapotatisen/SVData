import json
import os

def jsoncleaner(filename):
    with open(filename) as infile:
        jsondirty = json.load(infile)

    os.remove(filename)

    with open(filename, "w") as outfile:
        json.dump(jsondirty, outfile, indent=2)
        
jsoncleaner("database.json")
