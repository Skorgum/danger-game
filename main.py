import sys
from rooms import first_room
def main():

    print('''       WELCOME TO DANGER GAME!
You are in an empty room with two doors.
One is marked "Exit" and the other "Danger".
What door will you choose? (Type a command like 'exit', 'danger', 'look', help.)
''')
    counter = 5
    while counter != 0:
        command = input("enter a command> ").lower()

        if command in ("help", "?"):
            print("Commands: 'exit', 'danger', 'look', 'help'")
        elif command == "look":
            counter -= 1
            print("You are in an empty room with two doors labled 'Exit' and 'Danger'.")
        elif command == "exit":
            print("A wise choice! You safely exit and win the game! Congratulations big brain!")
            sys.exit()
        elif command == "danger":
            first_room() # go to the next room
            return
        else:
            print("Invalid command! Try help or ? for a list of valid commands.")
            counter -= 1
    print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")
    
if __name__ == "__main__":
    main()