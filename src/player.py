# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room):
        self.name = name
        self.currentRoom = room

    def move(self, direction):
        if direction == 'n' and self.currentRoom.n_to:
            return f'You are in {self.currentRoom.name}.\n{self.currentRoom.desc}'
        elif direction == 's' and self.currentRoom.s_to:
            return f'You ar in {self.crrentRoom.name}.\n{self.currentRoom.desc}'
        elif direction == 'e' and self.currentRoom.e_to:
            return f'You ar in {self.crrentRoom.name}.\n{self.currentRoom.desc}'
        elif direction == 'w' and self.currentRoom.w_to:
            return f'You ar in {self.crrentRoom.name}.\n{self.currentRoom.desc}'
        else:
            return "Wrong, there is no room in that direction."

