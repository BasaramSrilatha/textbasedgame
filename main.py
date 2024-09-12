import time

def print_pause(message, delay=1):
    print(message)
    time.sleep(delay)

def intro():
    print_pause("You find yourself at the edge of a mystical forest.")
    print_pause("The forest is known for strange occurrences and hidden treasures.")
    print_pause("You have three paths in front of you: left, right, and straight ahead.")

def choose_path():
    path = ''
    while path not in ['left', 'right', 'straight']:
        path = input("Do you go left, right, or straight ahead? (type 'left', 'right', or 'straight'):\n").lower()
    return path

def left_path():
    print_pause("You choose the left path and venture deeper into the forest.")
    print_pause("Suddenly, you encounter a large, enchanted wolf!")
    action = ''
    while action not in ['fight', 'run']:
        action = input("Do you choose to fight or run? (type 'fight' or 'run'):\n").lower()
    if action == 'fight':
        print_pause("You bravely fight the wolf and manage to scare it away!")
        print_pause("You find a hidden treasure behind the trees. You win!")
    elif action == 'run':
        print_pause("You turn and run back to the forest entrance.")
        print_pause("It's safer here, but your adventure is over.")

def right_path():
    print_pause("You take the right path, leading to a dark cave.")
    print_pause("You hear eerie sounds coming from inside.")
    action = ''
    while action not in ['enter', 'leave']:
        action = input("Do you want to enter the cave or leave? (type 'enter' or 'leave'):\n").lower()
    if action == 'enter':
        print_pause("You bravely enter the cave and find an ancient artifact!")
        print_pause("Congratulations! You have found a piece of hidden history!")
    elif action == 'leave':
        print_pause("You decide to leave the cave and head back to the entrance of the forest.")
        print_pause("You leave without any discoveries, but at least you're safe.")

def straight_path():
    print_pause("You walk straight ahead, deeper into the forest.")
    print_pause("The forest grows darker, and suddenly you find yourself in a clearing.")
    print_pause("In the clearing is a mysterious figure offering you a choice between a magical sword and a healing potion.")
    action = ''
    while action not in ['sword', 'potion']:
        action = input("Do you choose the sword or the potion? (type 'sword' or 'potion'):\n").lower()
    if action == 'sword':
        print_pause("You choose the sword and feel a surge of power!")
        print_pause("With the sword, you are prepared to face any danger in the forest.")
        print_pause("Your adventure continues...")
    elif action == 'potion':
        print_pause("You choose the potion and feel rejuvenated.")
        print_pause("With newfound energy, you explore further into the forest.")
        print_pause("But for now, the adventure ends here.")

def adventure_game():
    intro()
    path = choose_path()
    if path == 'left':
        left_path()
    elif path == 'right':
        right_path()
    elif path == 'straight':
        straight_path()
    print_pause("Thank you for playing the adventure game!")

adventure_game()
