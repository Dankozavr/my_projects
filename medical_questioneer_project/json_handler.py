import json
import os
from datetime import datetime

class JsonHandler:
    def __init__(self):
        self.messages_file_path = os.path.join(os.path.dirname(__file__), "medical_questioneer_data\\messages.json")
        self.patients_file_path = os.path.join(os.path.dirname(__file__), "medical_questioneer_data\\patients.json")

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
     
    def file_diagnosis(self, all_patients, current_patient):
        current_date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        try:
            if current_patient.is_new:
                patient_data = {
                    current_patient.id: {
                        "name": current_patient.name,
                        "surname": current_patient.surname,
                        "dob": current_patient.dob,
                        "email": current_patient.email,
                        "diagnosis": {
                            current_date_time: current_patient.diagnosis
                        }
                    }
                }
                all_patients.update(patient_data)
            else:
                patient_data = {
                    current_date_time: current_patient.diagnosis
                }
                all_patients[current_patient.id]["diagnosis"].update(patient_data)
            with open(self.patients_file_path, 'w', encoding='utf-8') as f:
                json.dump(all_patients, f, ensure_ascii=False, indent=4)
        except:
            print("Failed to file a diagnosis")
        return