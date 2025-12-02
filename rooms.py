import sys

def danger_room():
    print("""You have chosen Danger! Bold choice.
This is placeholder text describing the danger room.
What do you want to do? (Type a command like 'look', help.)
""")
    counter = 5
    while counter != 0:
        command = input("enter a command> ").lower()

        if command in ("help", "?"):
            print("Commands: 'incorrect option', 'correct option', 'look', 'help'")
        if command == "look":
            print("This is placeholder text describing the current room")
        if command == "incorrect option":
            print("Placehold text describing a gruesome death! Game over small brain!")
            sys.exit()
        elif command == "correct option":
            next_room() # go to the next room (where next_room is the next room's function)
        else:
            print("Invalid command! Try help or ? for a list of valid commands.")
            counter -= 1
    print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")