#!/usr/bin/python3
"""Module for add_item"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation."""
    with open(filename, 'w') as f:
        import json
        f.write(json.dumps(my_obj))

def load_from_json_file(filename):
    """Method for loading a JSON file."""
    import json

    with open(filename, 'r') as f:
        return json.load(f)
    
def add_item():
    """Method for adding items to a list."""
    import sys
    import os

    filename = "add_item.json"
    if os.path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    for arg in sys.argv[1:]:
        my_list.append(arg)

    save_to_json_file(my_list, filename)
