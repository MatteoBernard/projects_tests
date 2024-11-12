import json
import os


def load_data(path="data.json"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "..", path)
    with open(config_path, "r") as file:
        data = json.load(file)
    return data
