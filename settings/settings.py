import json
import os

config = {}
def get_config(config_type):
    global config
    base_path = "./settings/"

    full_settings_file_path = os.path.join(base_path, config_type)
    with open(full_settings_file_path) as setting_file:
        config = json.load(setting_file)