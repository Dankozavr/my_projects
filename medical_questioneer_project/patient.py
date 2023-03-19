from datetime import datetime
import re
class Patient:
    
    def __init__(self, mq):
        self.id = ""
        self.is_new = True
        self.diagnosis = ""
        self.get_patient_details(mq)
    
    def get_patient_details(self, mq):
        while True:
            self.name = input(mq.messages["name_prompt"])
            if self.validate_alpha(self.name, mq.messages["invalid_name"]): break
            else: mq.clear_console()
        while True:
            self.surname = input(mq.messages["surname_prompt"])
            if self.validate_alpha(self.surname, mq.messages["invalid_surname"]): break
            else: mq.clear_console()
        while True:
            self.dob = input(mq.messages["dob_prompt"])
            if self.validate_dob(self.dob, mq.messages["invalid_dob"]): break
            else: mq.clear_console()
        while True:
            self.email = input(mq.messages["email_prompt"])
            if self.validate_email(self.email, mq.messages["invalid_email"]): break
            else: mq.clear_console()

    
    def validate_alpha(self, data, message):
        if not data.isalpha():
            input(message)
            return False
        return True
    
    def validate_dob(self, dob, message):
        format = "%d/%m/%Y"
        is_format_correct = True
        try:
            is_format_correct = bool(datetime.strptime(dob, format))
        except:
            is_format_correct = False
        if not is_format_correct:
            input(message)
            return False
        return True
    
    def validate_email(self, email, message):
        format = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        is_format_correct = re.fullmatch(format, email)
        if not is_format_correct:
            input(message)
            return False
        return True