import json

def load_fields(config_path):
    with open(config_path, 'r') as f:
        return json.load(f).get("fields_to_extract", [])