import sys
def main():

    print('''       WELCOME TO DANGER GAME!
You are in an empty room with two doors.
One is marked "Exit" and the other "Danger".
What door will you choose? (exit/danger)
''')
    while True:
        choice = input("> ").lower()

        if choice == "exit":
            print("A wise choice! You safely exit and win the game! Congratulations big brain!")
            sys.exit()
        elif choice == "danger":
            print("Oh no! The floor gives out and you fall to your death. Game over small brain!")
            sys.exit()
        else:
            print("Invalid choice!")
    
if __name__ == "__main__":
    main()