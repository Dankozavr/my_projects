import json
import os
from datetime import datetime

class JsonHandler:
    def __init__(self):
        self.objects_file_path = os.path.join(os.path.dirname(__file__), "game_objects.json")

    def read_json(self, json_file):
        """
        json_file - full path to the json_file        
        """
        try:
            with open(json_file, "r") as open_file:
                json_object = json.load(open_file)
        except:
            return {}
        return json_object