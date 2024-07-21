import json
import os

def load_config():
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config', 'config.json'))
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    return config
