from room import Room
from game_object import GameObject
from json_handler import JsonHandler

class Game:
    def __init__(self):
        jh = JsonHandler()
        self.object_data = jh.read_json(jh.objects_file_path)
        self.attempts = 0
        objects = self.create_objects()
        self.room = Room(111, objects)

    def create_objects(self):
        objects = []
        for object, object_data in self.object_data.items():
            temp = []
            for _, property_description in object_data.items():
                temp.append(property_description)
            objects.append(GameObject(object, temp[0], temp[1], temp[2]))
        return objects
    
    def take_turn(self):
        prompt = self.get_room_prompt()
        selection = int(input(prompt))
        if  1 <= selection <= 5:
            self.select_object(selection - 1)
            self.take_turn()
        else:
            if self.guess_code(selection):
                print(f"You win in {self.attempts + 1} guess(es)!")
            else:
                if self.attempts == 3:
                    print("Game over, you ran out of attempts! Better luck next time!")
                else:
                    print(f"Code is incorrect, try again, you have {3 - self.attempts} left!")
                    self.take_turn()

    def get_room_prompt(self):
        prompt = "Enter the 3 digit lock code or choose an item to interract with:\n"
        names = self.room.get_game_object_names()
        for index, name in enumerate(names):
            prompt += f"{index + 1}. {name}\n"
        return prompt
    
    def select_object(self, index):
        selected_object = self.room.game_objects[index]
        prompt = self.get_object_interaction_string(selected_object.name)
        interaction = input(prompt)
        clue = self.interact_with_object(selected_object, interaction)
        print(clue)

    def get_object_interaction_string(self, name):
        return f"How do you want to interact with the {name}?\n1. Look\n2. Touch\n3. Smell\n"
    
    def interact_with_object(self, object, interaction):
        if interaction == "1":
            return object.appearance
        elif interaction == "2":
            return object.feel
        else:
            return object.smell
    
    def guess_code(self, code):
        if self.room.check_code(code):
            return True
        else:
            self.attempts += 1
            return False
    
if __name__ == "__main__":
    game = Game()
    game.take_turn()