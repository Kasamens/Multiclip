import sys
import clipboard
import json

# This function saves commands in a json file


def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

# This function reads commands from a json file


def load_items(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
        return data


if(len(sys.argv) == 2):
    command = sys.argv[1]

    if command == "save":
        pass
    elif command == "load":
        pass
    elif command == "list":
        pass
    else:
        print("Unknown Command")
else:
    print("Please pass exactly one command")
