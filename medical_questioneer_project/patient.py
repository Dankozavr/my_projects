class Patient:
    
    def __init__(self, mq):
        self.name = input(mq.messages["name_prompt"])
        self.surname = input(mq.messages["name_prompt"])
        self.dob = input(mq.messages["dob_prompt"])
        self.email = input(mq.messages["email_prompt"])
        self.id = ""
        self.is_new = True
        self.diagnosis = ""