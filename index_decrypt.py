import json
import shutil
import os

try:
    index = json.load(open(input("Enter index json file path: "), 'r'))
except FileNotFoundError:
    print("\033[91mError: The specified json file wasn't found.")
    input("Press Enter key to exit...\033[0m")
    exit(1)
except json.JSONDecodeError:
    print("\033[91mError: Failed to decode the json file.")
    input("Press Enter key to exit...\033[0m")
    exit(1)

minecraft_path = input("Enter Minecraft folder directory: ")

osErrors = []
fileNotFoundErrors = []

def decode_file(name):
    global osErrors, fileNotFoundErrors
    try:
        hash = index["objects"][name]["hash"]
        source_file = minecraft_path + f"\\assets\\objects\\{hash[:2]}\\{hash}"
        file = "result\\" + name.replace("/", "\\")
        path = os.path.dirname(file) 
        os.makedirs(path, exist_ok=True)
        shutil.copy(source_file, file)
    except FileNotFoundError:
        print(f"Error: The source file '{source_file}' does not exist.")
        fileNotFoundErrors.append(name)
    except OSError as e:
        print(f"\033[91mError: Failed to process file '{name}': {str(e)}")
        osErrors.append(name)


for object in index["objects"]:
    if object != "pack.mcmeta":
        decode_file(object)
        print(f"\033[0mDecoded file '{object}'")

print(f"\033[93mFound Errors:\n    Files not found: {len(fileNotFoundErrors)}: {fileNotFoundErrors}\n    Proccess errors: {len(osErrors)}: {osErrors}\033[0m")
input("Press Enter key to exit...")
