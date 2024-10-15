import json
import shutil
import os

index = json.load(open('index.json', 'r'))

def decode_file(name):
    hash = index["objects"][name]["hash"]

    source_file = f"C:\\Users\\usuario\\AppData\\Roaming\\.minecraft\\assets\\objects\\{hash[:2]}\\{hash}"

    file = "result\\" + name.replace("/", "\\")

    path = os.path.dirname(file) 
    os.makedirs(path, exist_ok=True)  

    shutil.copy(source_file, file) 

for object in index["objects"]:
    if object != "pack.mcmeta":
        decode_file(object)
        print(f"Decoded file {object}")

