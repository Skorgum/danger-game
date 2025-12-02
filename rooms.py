import sys

# TODO: Complete the room's description and commands. Number of wrong options will increase with each room.
def first_room():
    print("""You have chosen Danger! Bold choice.
The door slams behind you. You find yourself in a room with three doors, but are only marked as 'one', 'two', and 'three'.
What do you want to do? (Type a command like 'look', help.)
""")
    counter = 5 # starting value will decrease with each room
    while counter != 0:
        command = input("enter a command> ").lower()

        if command in ("help", "?"):
            # 2 wrong options in this room
            print("Commands: 'one', 'two', 'three', 'look', and 'help'")
        elif command == "look":
            counter -= 1
            print("There are three doors in front of you labled 'one', 'two', and 'three'.")
        elif command == "one":
            print("The door was booby-trapped with a 12 gauge shotgun that blows your head off! Game over small brain!")
            sys.exit()
        elif command == "two":
            print("You step through door two and onto a metal grate. The door slams behind you and you are immediately engulfed in flames! Game over small brain!")
            sys.exit()
        elif command == "three":
            second_room() # go to the next room (where next_room is the next room's function)
            return
        else:
            print("Invalid command! Try help or ? for a list of valid commands.")
            counter -= 1
    print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")

# TODO: Complete the room's description and commands
def second_room(): # change the name to fit the room's description
    print("""Congratulations big brain, you made it to the next room!
This is placeholder text describing the second room.
What do you want to do? (Type a command like 'look', help.)
""")
    counter = 4 # starting value will decrease with each room
    while counter != 0:
        command = input("enter a command> ").lower()

        if command in ("help", "?"):
            # 3 wrong options in this room
            print("Commands: 'incorrect option', 'correct option', 'look', 'help'")
        elif command == "look":
            counter -= 1
            print("This is placeholder text describing the second room")
        elif command == "incorrect option":
            print("Placeholder text describing a gruesome death! Game over small brain!")
            sys.exit()
        elif command == "correct option":
            third_room() # go to the next room
            return
        else:
            print("Invalid command! Try help or ? for a list of valid commands.")
            counter -= 1
    print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")

# TODO: Complete the room's description and commands
def third_room(): # change the name to fit the room's description
    print("""Congratulations big brain, you made it to the next room!
This is placeholder text describing the third room.
What do you want to do? (Type a command like 'look', help.)
""")
    counter = 3 # starting value will decrease with each room
    while counter != 0:
        command = input("enter a command> ").lower()

        if command in ("help", "?"):
            # 4 wrong options in this room
            print("Commands: 'incorrect option', 'correct option', 'look', 'help'")
        elif command == "look":
            counter -= 1
            print("This is placeholder text describing the third room")
        elif command == "incorrect option":
            print("Placeholder text describing a gruesome death! Game over small brain!")
            sys.exit()
        elif command == "correct option":
            final_room() # go to the next room
            return
        else:
            print("Invalid command! Try help or ? for a list of valid commands.")
            counter -= 1
    print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")

# TODO: Complete the room's description and commands
def final_room(): # change the name to fit the room's description
    print("""Congratulations big brain, you made it to the final room!
This is placeholder text describing the final room.
What do you want to do? (Type a command like 'look', help.)
""")
    counter = 2 # starting value will decrease with each room
    while counter != 0:
        command = input("enter a command> ").lower()

        if command in ("help", "?"):
            # 5 wrong options in this room
            print("Commands: 'incorrect option', 'correct option', 'look', 'help'")
        elif command == "look":
            counter -= 1
            print("This is placeholder text describing the third room")
        elif command == "incorrect option":
            print("Placeholder text describing a gruesome death! Game over small brain!")
            sys.exit()
        elif command == "correct option":
            real_final_room() # go to the next room
            return
        else:
            print("Invalid command! Try help or ? for a list of valid commands.")
            counter -= 1
    print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")

# TODO: Complete the room's description and commands
def real_final_room(): # change the name to fit the room's description
    print("""I lied!! This is the *real* final room! Good luck!
This is placeholder text describing the real final room.
What do you want to do? (Type a command like 'look', help.)
""")
    counter = 1 # starting value will decrease with each room
    while counter != 0:
        command = input("enter a command> ").lower()

        if command in ("help", "?"):
            # 7 options in this room, all resulting in death
            print("Commands: 'incorrect option', 'correct option', 'look', 'help'")
        elif command == "look":
            counter -= 1
            print("This is placeholder text describing the real final room")
        elif command == "incorrect option":
            print("Placehold text describing a gruesome death! Game over small brain!")
            sys.exit()
        elif command == "correct option":
            print("Placeholder text describing a gruesome death! Game over small brain!")
            sys.exit()
        else:
            print("Invalid command! Try help or ? for a list of valid commands.")
            counter -= 1
    print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")