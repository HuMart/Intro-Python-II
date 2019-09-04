# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room):
        self.name = name
        self.currentRoom = room

    def __repr__(self):
        return ''+self.name+''+self.currentRoom+''

    def __str__(self):
        return ''+self.name+''+self.currentRoom+''


