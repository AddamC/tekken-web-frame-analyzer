import json

class Character:
    def __init__(self):
        self.char_name = ''
        self.moves = []

    def to_json(self):
        return json.dumps(self.__dict__)

class Move:
    def __init__(self, move_data):
        self.command = move_data[1]
        self.hit_level = move_data[2]
        self.startup = move_data[3]
        self.on_block = move_data[4]
        self.on_hit = move_data[5]
        self.on_counter_hit = move_data[6]

    def __str__(self):
        string = ""
        string += self.command + "\n"
        string += self.hit_level + "\n"
        string += self.startup + "\n"
        string += self.on_block + "\n"
        string += self.on_hit + "\n"
        string += self.on_counter_hit + "\n"
        return string
