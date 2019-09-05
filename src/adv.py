from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

current_room = room["outside"]
name = input("\nWhat is your name? ")
print (f"\nGoodluck, {name}!")

player = Player(name, room["outside"])

while True:
    current_room = player.current_room
    print("\n-------------------------------------------------------------------------")
    print(f"\n    Current room: {current_room.name}")
    print(f"\n    Room description: {current_room.description}\n")
    command = input("Please pick a command:\n(n)orth\n(s)outh\n(e)ast\n(w)est\n(q)uit\n   Command: ")
    command = command.lower().strip()
    if command == '':
        continue
    command = command[0]
    if command == "n":
        if current_room.n_to is not None:
            player.current_room = current_room.n_to
        else:
            print("\n**There is no room in that direction**")
    elif command == "s":
        if current_room.s_to is not None:
            player.current_room = current_room.s_to
        else:
            print("\n**There is no room in that direction**")
    elif command == "e":
        if current_room.e_to is not None:
            player.current_room = current_room.e_to
        else:
            print("\n**There is no room in that direction**")
    elif command == "w":
        if current_room.w_to is not None:
            player.current_room = current_room.w_to
        else:
            print("\n**There is no room in that direction**")
    elif command == "q":
        print("\n**You have quit the game! Goodbye!**")
        break
    else:
        print("\n**Did not recognize the command**")
