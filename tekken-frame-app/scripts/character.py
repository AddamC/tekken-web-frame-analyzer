class Character:
    def __init__(self):
        self.char_name = ''
        self.moves = []

    def to_json():
        print('to_json method')

    

class Move:
    def __init__(self, move):
        self.command = move[0]
        self.hit_level = move[1]
        self.startup = move[2]
        self.on_block = move[3]
        self.on_hit = move[4]
        self.on_counter_hit = move[5]

    def __str__(self):
        string = ""
        string += self.command + "\n"
        string += self.hit_level + "\n"
        string += self.startup + "\n"
        string += self.on_block + "\n"
        string += self.on_hit + "\n"
        string += self.on_counter_hit + "\n"
        return string
