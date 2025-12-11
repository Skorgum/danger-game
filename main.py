import sys
import time
from rooms import first_room
def main(time_limit):

    print('''       WELCOME TO DANGER GAME!
You are in an empty room with two doors.
One is marked "Exit" and the other "Danger".
What door will you choose? (Type a command like 'exit', 'danger', 'look', or 'help'.)
''')
    
    while True:
        print(f"(You have {time_limit:.0f} seconds to choose.)")

        start = time.time()
        command = input("enter a command> ").strip().lower()
        elapsed = time.time() - start

        if elapsed > time_limit:
            print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")
            return "dead", time_limit

        if command in ("help", "?"):
            print("Commands: 'exit', 'danger', 'look', 'help'")
            
        elif command == "look":
            print("You are in an empty room with two doors labeled 'Exit' and 'Danger'.")
            
        elif command == "exit":
            print("A wise choice! You safely exit and win the game! Congratulations big brain!")
            sys.exit()
        elif command == "danger":
            next_time_limit = max(2, time_limit - 2)
            return first_room(next_time_limit) # go to the next room
        else:
            print("Invalid command! Try help or ? for a list of valid commands.")
            
if __name__ == "__main__":
    time_limit = 10
    while True:
        outcome, time_limit = main(time_limit)
        if outcome == "dead":
            print("\nRestarting the game...\n")
            time_limit = 10
            continue