import sys
import random
from deaths import random_death
# TODO: Complete the room's description and commands. Number of wrong options will increase with each room.
def first_room():
    print("""You have chosen Danger! Bold choice.
The door slams behind you. You find yourself in a room with three doors, but are only marked as 'one', 'two', and 'three'.
What door will you choose? (Type your door choice or a command like 'look' or 'help'.)
""")
    counter = 5 # starting value will decrease with each room

    correct_door = random.choice(["one", "two", "three"])

    while counter != 0:
        command = input("enter a command> ").lower()

        if command in ("help", "?"):
            # 2 wrong options in this room
            print("Commands: 'one', 'two', 'three', 'look', and 'help'")
        elif command == "look":
            counter -= 1
            print("There are three doors in front of you labled 'one', 'two', and 'three'.")
        elif command in ("one", "two", "three"):
            if command == correct_door:
                second_room()
                return
            else:
                random_death()
        else:
            print("Invalid command! Try 'help' or '?' for a list of valid commands.")
            counter -= 1
    print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")

def second_room():
    print("""Congratulations big brain, you made it to the next room!
The door slams behind you. This room is slightly larger than the one before, with 4 doors labled 'one' through 'four.
What door will you choose? (Type your door choice or a command like 'look' or 'help'.)
""")
    counter = 4 # starting value will decrease with each room

    correct_door = random.choice(["one", "two", "three", "four"])

    while counter != 0:
        command = input("enter a command> ").lower()

        if command in ("help", "?"):
            # 3 wrong options in this room
            print("Commands: 'one', 'two', 'three', 'four', 'look', and 'help'")
        elif command == "look":
            counter -= 1
            print("There are four doors in front of you labled 'one' through 'four'.")
        elif command in ("one", "two", "three", "four"):
            if command == correct_door:
                third_room()
                return
            else:
                random_death()
        else:
            print("Invalid command! Try 'help' or '?' for a list of valid commands.")
            counter -= 1
    print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")

def third_room():
    print("""Congratulations big brain, you made it to the next room!
The door slams behind you. This room is even larger, this time with 5 doors labled 'one' through 'five'.
What door will you choose? (Type your door choice or a command like 'look' or 'help'.)
""")
    counter = 3 # starting value will decrease with each room

    correct_door = random.choice(["one", "two", "three", "four", "five"])

    while counter != 0:
        command = input("enter a command> ").lower()

        if command in ("help", "?"):
            # 4 wrong options in this room
            print("Commands: 'one', 'two', 'three', 'four', 'five', 'look', and 'help'")
        elif command == "look":
            counter -= 1
            print("There are five doors in front of you labled 'one' through 'five'.")
        elif command in ("one", "two", "three", "four", "five"):
            if command == correct_door:
                final_room()
                return
            else:
                random_death()
        else:
            print("Invalid command! Try 'help' or '?' for a list of valid commands.")
            counter -= 1
    print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")

def final_room():
    print("""Congratulations big brain, you made it to the final room!
The door slams behind you. This room is quite large, tnow with 6 doors labled 'one' through 'six'.
What door will you choose? (Type your door choice or a command like 'look' or 'help'.)
""")
    counter = 2 # starting value will decrease with each room

    correct_door = random.choice(["one", "two", "three", "four", "five", "six"])

    while counter != 0:
        command = input("enter a command> ").lower()

        if command in ("help", "?"):
            # 5 wrong options in this room
            print("Commands: 'one', 'two', 'three', 'four', 'five', 'six', 'look', and 'help'")
        elif command == "look":
            counter -= 1
            print("There are six doors in front of you labled 'one' through 'six'.")
        elif command in ("one", "two", "three", "four", "five", "six"):
            if command == correct_door:
                real_final_room()
                return
            else:
                random_death()
        else:
            print("Invalid command! Try 'help' or '?' for a list of valid commands.")
            counter -= 1
    print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")

def real_final_room():
    print("""Congratulations!! You have arrived at the treasure room!
The door slams behind you. This room is huge, with 7 chests labled 'one' through 'seven'.
What chest will you choose? (Type your chest choice or a command like 'look' or 'help'.)
""")
    counter = 1 # starting value will decrease with each room
    while counter != 0:
        command = input("enter a command> ").lower()

        if command in ("help", "?"):
            # 7 options in this room, all resulting in death
            print("Commands: 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'look', and 'help'")
        elif command == "look":
            counter -= 1
            print("There are seven chests in front of you labled 'one' through 'seven'.")
        elif command in ("one", "two", "three", "four", "five", "six", "seven"):
            print("Oh no! The chest was booby trapped! Game over small brain!")
            sys.exit()
        else:
            print("Invalid command! Try 'help' or '?' for a list of valid commands.")
            counter -= 1
    print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")