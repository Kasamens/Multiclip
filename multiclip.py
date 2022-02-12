import sys

from numpy import save
import clipboard
import json

# This is the name of the file to store data
SAVED_DATA = "clipboard.json"

# This function saves commands in a json file


def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

# This function reads commands from a json file


def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


if(len(sys.argv) == 2):
    command = sys.argv[1]
    # This copies all the commands in the file into the variable
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()

        # This apppends the new item to the dictionary
        # and overwrites the clipboard file with the data
        save_data(SAVED_DATA, data)
        print("Data saved")

    elif command == "load":
        key = input("Enter a key: ")
        if key not in data:
            print("Key does not exist")
        else:
            clipboard.copy(data[key])
            print("Data copied to clipboard")

    elif command == "list":
        print(data)

    elif command == "delete":
        key = input("Enter a key: ")
        if key not in data:
            print("Key does not exist")
        else:
            data = data.pop(key)
            save_data(SAVED_DATA, data)
            print(f"{key} deleted successfully")

    else:
        print("Unknown Command")
else:
    print("Please pass exactly one command")
