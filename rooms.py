import time
import random
from deaths import random_death

def first_room(time_limit):
    print("""You have chosen Danger! Bold choice.
The door slams behind you. You find yourself in a room with three doors, but are only marked as 'one', 'two', and 'three'.
What door will you choose? (Type your door choice or a command like 'look' or 'help'.)
""")
    
    correct_door = random.choice(["one", "two", "three"])

    while True:
        print(f"(You have {time_limit:.0f} seconds to choose.)")

        start = time.time()
        command = input("enter a command> ").strip().lower()
        elapsed = time.time() - start

        if elapsed > time_limit:
            print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")
            return "dead", time_limit

        if command in ("help", "?"):
            # 2 wrong options in this room
            print("Commands: 'one', 'two', 'three', 'look', and 'help'")
        elif command == "look":
            print("There are three doors in front of you labeled 'one', 'two', and 'three'.")
        elif command in ("one", "two", "three"):
            if command == correct_door:
                next_time_limit = max(2, time_limit - 2)
                result, final_limit = second_room(next_time_limit)
                return result, final_limit
            else:
                random_death()
                return "dead", time_limit
        else:
            print("Invalid command! Try 'help' or '?' for a list of valid commands.")

def second_room(time_limit):
    print("""Congratulations big brain, you made it to the next room!
The door slams behind you. This room is slightly larger than the one before, with 4 doors labeled 'one' through 'four'.
What door will you choose? (Type your door choice or a command like 'look' or 'help'.)
""")

    correct_door = random.choice(["one", "two", "three", "four"])

    while True:
        print(f"(You have {time_limit:.0f} seconds to choose.)")

        start = time.time()
        command = input("enter a command> ").strip().lower()
        elapsed = time.time() - start

        if elapsed > time_limit:
            print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")
            return "dead", time_limit

        if command in ("help", "?"):
            # 3 wrong options in this room
            print("Commands: 'one', 'two', 'three', 'four', 'look', and 'help'")
        elif command == "look":
            print("There are four doors in front of you labeled 'one' through 'four'.")
        elif command in ("one", "two", "three", "four"):
            if command == correct_door:
                next_time_limit = max(2, time_limit - 2)
                result, final_limit = third_room(next_time_limit)
                return result, final_limit
            else:
                random_death()
                return "dead", time_limit
        else:
            print("Invalid command! Try 'help' or '?' for a list of valid commands.")

def third_room(time_limit):
    print("""Congratulations big brain, you made it to the next room!
The door slams behind you. This room is even larger, this time with 5 doors labeled 'one' through 'five'.
What door will you choose? (Type your door choice or a command like 'look' or 'help'.)
""")

    correct_door = random.choice(["one", "two", "three", "four", "five"])

    while True:
        print(f"(You have {time_limit:.0f} seconds to choose.)")

        start = time.time()
        command = input("enter a command> ").strip().lower()
        elapsed = time.time() - start

        if elapsed > time_limit:
            print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")
            return "dead", time_limit

        if command in ("help", "?"):
            # 4 wrong options in this room
            print("Commands: 'one', 'two', 'three', 'four', 'five', 'look', and 'help'")
        elif command == "look":
            print("There are five doors in front of you labeled 'one' through 'five'.")
        elif command in ("one", "two", "three", "four", "five"):
            if command == correct_door:
                next_time_limit = max(2, time_limit - 2)
                result, final_limit = final_room(next_time_limit)
                return result, final_limit
            else:
                random_death()
                return "dead", time_limit
        else:
            print("Invalid command! Try 'help' or '?' for a list of valid commands.")

def final_room(time_limit):
    print("""Congratulations big brain, you made it to the final room!
The door slams behind you. This room is quite large, now with 6 doors labeled 'one' through 'six'.
What door will you choose? (Type your door choice or a command like 'look' or 'help'.)
""")

    correct_door = random.choice(["one", "two", "three", "four", "five", "six"])

    while True:
        print(f"(You have {time_limit:.0f} seconds to choose.)")

        start = time.time()
        command = input("enter a command> ").strip().lower()
        elapsed = time.time() - start

        if elapsed > time_limit:
            print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")
            return "dead", time_limit

        if command in ("help", "?"):
            # 5 wrong options in this room
            print("Commands: 'one', 'two', 'three', 'four', 'five', 'six', 'look', and 'help'")
        elif command == "look":
            print("There are six doors in front of you labeled 'one' through 'six'.")
        elif command in ("one", "two", "three", "four", "five", "six"):
            if command == correct_door:
                next_time_limit = max(2, time_limit - 2)
                result, final_limit = real_final_room(next_time_limit)
                return result, final_limit
            else:
                random_death()
                return "dead", time_limit
        else:
            print("Invalid command! Try 'help' or '?' for a list of valid commands.")

def real_final_room(time_limit):
    print("""Congratulations!! You have arrived at the treasure room!
The door slams behind you. This room is huge, with 7 chests labeled 'one' through 'seven'.
What chest will you choose? (Type your chest choice or a command like 'look' or 'help'.)
""")
    
    while True:
        print(f"(You have {time_limit:.0f} seconds to choose.)")

        start = time.time()
        command = input("enter a command> ").strip().lower()
        elapsed = time.time() - start

        if elapsed > time_limit:
            print("You have taken too long to choose so the room starts to fill with foul smelling gas. Game over small brain!")
            return "dead", time_limit

        if command in ("help", "?"):
            # 7 options in this room, all resulting in death
            print("Commands: 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'look', and 'help'")
        elif command == "look":
            print("There are seven chests in front of you labeled 'one' through 'seven'.")
        elif command in ("one", "two", "three", "four", "five", "six", "seven"):
            print("Oh no! The chest was booby trapped! Game over small brain!")
            return "dead", time_limit
        else:
            print("Invalid command! Try 'help' or '?' for a list of valid commands.")
