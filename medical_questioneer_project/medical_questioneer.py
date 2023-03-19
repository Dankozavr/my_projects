import os
from json_handler import JsonHandler
from patient import Patient
import uuid

class MedicalQuestioneer:

    def __init__(self):
        self.jh = JsonHandler()
        self.messages = self.jh.read_json(self.jh.messages_file_path)
        pass

    def list_patients(self):
        self.clear_console()
        all_patients = self.jh.read_json(self.jh.patients_file_path)
        if all_patients == {}:
            print(self.messages["patient_list_empty"])
        else:
            print(self.messages["listing_patients"])
            i = 1
            for patient_id, patient_info in all_patients.items():
                print(str(i) + ". Patient ID:", patient_id)
                for info in patient_info:
                    if info != "diagnosis":
                        print(info.capitalize() + ':', patient_info[info])
                    else:
                        print(info.capitalize() + ':')
                        for date_time, diagnosis in patient_info["diagnosis"].items():
                            print("-", date_time + ':', diagnosis)
                print("\n")
                i += 1
        input(self.messages["return_to_menu"])
        return

    def assess_appearance(self):
        self.clear_console()
        while True:
            appearance = input(self.messages["appearance_prompt"])
            if appearance == "1":
                return self.assess_eyes()
            elif appearance == "2":
                return self.assess_skin()
            else:
                input(self.messages["unrecognised_input"])
                self.clear_console()

    def assess_skin(self):
        while True:
            skin_assessment = input(self.messages["skin_prompt"])
            if skin_assessment == "1":
                return self.messages["some_dehidration"]
            elif skin_assessment == "2":
                return self.messages["severe_dehidration"]
            else:
                input(self.messages["unrecognised_input"])
                self.clear_console()
    
    def assess_eyes(self):
        while True:
            eye_assessment = input(self.messages["eyes_prompt"])
            if eye_assessment == "1":
                return self.messages["no_dehidration"]
            elif eye_assessment == "2":
                return self.messages["severe_dehidration"]
            else:
                input(self.messages["unrecognised_input"])
                self.clear_console()
    
    def check_patient_record(self, all_patients, current_patient):
        for patient_id, patient in all_patients.items():
            if  current_patient.name == patient["name"] and \
                current_patient.surname == patient["surname"] and \
                current_patient.dob == patient["dob"] and \
                current_patient.email == patient["email"]:
                while True:
                    answer = input(self.messages["patient_exists"])[0].lower()
                    if answer == "y":
                        current_patient.id = patient_id
                        return False
                    elif answer == "n":
                        return input(self.messages["cant_add_patient"])
                    else:
                        input(self.messages["unrecognised_input"])
                        self.clear_console()
        else:
            while True:
                current_patient.id = uuid.uuid4().hex
                if current_patient.id not in all_patients.keys():
                    break
        return True

    def start_new_diagnosis(self):
        self.clear_console()
        print(self.messages["new_diagnosis"])
        current_patient = Patient(mq)
        all_patients = self.jh.read_json(self.jh.patients_file_path)
        current_patient.is_new = self.check_patient_record(all_patients, current_patient)
        current_patient.diagnosis = self.assess_appearance()
        print("\n" + current_patient.diagnosis, self.messages["file_diagnosis"])
        self.jh.file_diagnosis(all_patients, current_patient)
        input(self.messages["return_to_menu"])
        return

    def clear_console(self):
        os.system('cls')
        return
    
if __name__ == "__main__":

    mq = MedicalQuestioneer()
    while True:
        mq.clear_console()
        selection = input(mq.messages["welcome_message"])
        if selection == "1":
            mq.list_patients()
        elif selection == "2":
            mq.start_new_diagnosis()
        elif selection.lower() == "q":
            break
        else:
            input(mq.messages["unrecognised_input"])
        