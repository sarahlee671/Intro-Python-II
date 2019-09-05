# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.current_room = location
    
    def __str__(self):
        return 'Name: {self.name}, Room: {self.current_room}'.format(self=self)