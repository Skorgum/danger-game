import sys

# TODO: Complete the room's description and commands. Number of wrong options will increase with each room.
def first_room():
    print("""You have chosen Danger! Bold choice.
The door slams behind you. You find yourself in a room with three doors, but are only marked as 'one', 'two', and 'three'.
What door will you choose? (Type a command like 'look', help.)
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
            second_room() # go to the next room
            return
        else:
            print("Invalid command! Try help or ? for a list of valid commands.")
            counter -= 1
    print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")

def second_room():
    print("""Congratulations big brain, you made it to the next room!
The door slams behind you. This room is slightly larger than the one before, with 4 doors labled 'one' through 'four.
What door will you choose? (Type a command like 'look', help.)
""")
    counter = 4 # starting value will decrease with each room
    while counter != 0:
        command = input("enter a command> ").lower()

        if command in ("help", "?"):
            # 3 wrong options in this room
            print("Commands: 'one', 'two', 'three', 'four' 'look', and 'help'")
        elif command == "look":
            counter -= 1
            print("There are four doors in front of you labled 'one' through 'four'.")
        elif command == "one":
            print("As soon as you open the door, a pack of rabid wolves tears you apart! Game over small brain!")
            sys.exit()
        elif command == "two":
            third_room() # go to the next room
            return
        elif command == "three":
            print("As soon as you step through the door, you are impaled by a spike trap! Game over small brain!")
            sys.exit()
        elif command == "four":
            print("You step through the door and it slams behind you. The room gets suddenly really cold! You desperately try in vein to open the sealed door before passing out from hypothermia. Game over small brain!")
            sys.exit()
        else:
            print("Invalid command! Try help or ? for a list of valid commands.")
            counter -= 1
    print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")

def third_room():
    print("""Congratulations big brain, you made it to the next room!
The door slams behind you. This room is even larger, this time with 5 doors labled 'one' through 'five'.
What door will you choose? (Type a command like 'look', help.)
""")
    counter = 3 # starting value will decrease with each room
    while counter != 0:
        command = input("enter a command> ").lower()

        if command in ("help", "?"):
            # 4 wrong options in this room
            print("Commands: 'one', 'two', 'three', 'four', 'five' 'look', and 'help'")
        elif command == "look":
            counter -= 1
            print("There are five doors in front of you labled 'one' through 'five'.")
        elif command == "one":
            print("You step through door two and onto a metal grate. The door slams behind you and you are immediately engulfed in flames! Game over small brain!")
            sys.exit()
        elif command == "two":
            print("The door was booby-trapped with a 12 gauge shotgun that blows your head off! Game over small brain!")
            sys.exit()
        elif command == "three":
            print("As soon as you step through the door, you are impaled by a spike trap! Game over small brain!")
            sys.exit()
        elif command == "four":
            final_room() # go to the next room
            return
        elif command == "five":
            print("As soon as you open the door, a pack of rabid wolves tears you apart! Game over small brain!")
            sys.exit()
        else:
            print("Invalid command! Try help or ? for a list of valid commands.")
            counter -= 1
    print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")

def final_room():
    print("""Congratulations big brain, you made it to the final room!
The door slams behind you. This room is quite large, tnow with 6 doors labled 'one' through 'six'.
What door will you choose? (Type a command like 'look', help.)
""")
    counter = 2 # starting value will decrease with each room
    while counter != 0:
        command = input("enter a command> ").lower()

        if command in ("help", "?"):
            # 5 wrong options in this room
            print("Commands: 'one', 'two', 'three', 'four', 'five', 'six', 'look', and 'help'")
        elif command == "look":
            counter -= 1
            print("There are six doors in front of you labled 'one' through 'six'.")
        elif command == "one":
            print("You step through the door and it slams behind you. The room gets suddenly really cold! You desperately try in vein to open the sealed door before passing out from hypothermia. Game over small brain!")
            sys.exit()
        elif command == "two":
            print("The door was booby-trapped with a 12 gauge shotgun that blows your head off! Game over small brain!")
            sys.exit()
        elif command == "three":
            print("You step through door two and onto a metal grate. The door slams behind you and you are immediately engulfed in flames! Game over small brain!")
            sys.exit()
        elif command == "four":
            print("As soon as you open the door, a pack of rabid wolves tears you apart! Game over small brain!")
            sys.exit()
        elif command == "five":
            print("The door was electrified! Your head catches fire immediately as 50k volts rush through your body! Game over small brain!")
            sys.exit()
        elif command == "six":
            real_final_room() # go to the next room
            return
        else:
            print("Invalid command! Try help or ? for a list of valid commands.")
            counter -= 1
    print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")

def real_final_room():
    print("""Congratulations!! You have arrived at the treasure room!
The door slams behind you. This room is huge, with 7 chests labled 'one' through 'seven'.
What chest do you want to open? (Type a command like 'look', help.)
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
        elif command == "one":
            print("Oh no! The chest was booby trapped! Game over small brain!")
            sys.exit()
        elif command == "two":
            print("Oh no! The chest was booby trapped! Game over small brain!")
            sys.exit()
        elif command == "three":
            print("Oh no! The chest was booby trapped! Game over small brain!")
            sys.exit()
        elif command == "four":
            print("Oh no! The chest was booby trapped! Game over small brain!")
            sys.exit()
        elif command == "five":
            print("Oh no! The chest was booby trapped! Game over small brain!")
            sys.exit()
        elif command == "six":
            print("Oh no! The chest was booby trapped! Game over small brain!")
            sys.exit()
        elif command == "seven":
            print("Oh no! The chest was booby trapped! Game over small brain!")
            sys.exit()
        else:
            print("Invalid command! Try help or ? for a list of valid commands.")
            counter -= 1
    print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")