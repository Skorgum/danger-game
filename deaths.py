import random

DEATH_MESSAGES = [
    "The door was booby-trapped with a 12 gauge shotgun that blows your head off! Game over small brain!",
    "You step through door two and onto a metal grate. The door slams behind you and you are immediately engulfed in flames! Game over small brain!",
    "As soon as you open the door, a pack of rabid wolves tears you apart! Game over small brain!",
    "As soon as you step through the door, you are impaled by a spike trap! Game over small brain!",
    "You step through the door and it slams behind you. The room gets suddenly really cold! You desperately try in vein to open the sealed door before passing out from hypothermia. Game over small brain!",    
]

def random_death():
    print(random.choice(DEATH_MESSAGES))