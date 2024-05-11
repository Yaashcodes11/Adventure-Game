import time

def intro():
    print("Welcome to the Adventure Game!")
    print("You wake up in a mysterious forest. Your goal is to find your way out.")
    time.sleep(2)
    print("You see two paths ahead of you.")

def choose_path():
    path = input("Which path will you take? Left or right? ").lower()
    if path == "left":
        print("You chose the left path.")
        time.sleep(1)
        left_path()
    elif path == "right":
        print("You chose the right path.")
        time.sleep(1)
        right_path()
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")
        choose_path()

def left_path():
    print("You encounter a river.")
    time.sleep(1)
    choice = input("Do you swim across or look for a bridge? Swim or bridge? ").lower()
    if choice == "swim":
        print("You attempt to swim across the river.")
        time.sleep(2)
        print("Oh no! You were caught by the river's strong current and swept away.")
        game_over()
    elif choice == "bridge":
        print("You find a sturdy bridge and cross the river safely.")
        time.sleep(2)
        print("You continue on your journey.")
        time.sleep(1)
        print("You see a cave up ahead.")
        time.sleep(1)
        cave()
    else:
        print("Invalid choice. Please enter 'swim' or 'bridge'.")
        left_path()

def right_path():
    print("You come across a pack of wolves.")
    time.sleep(1)
    choice = input("Do you try to fight them or run away? Fight or run? ").lower()
    if choice == "fight":
        print("You bravely fight the wolves.")
        time.sleep(2)
        print("You defeat them and continue on your journey.")
        time.sleep(1)
        print("You find a hidden treasure chest!")
        time.sleep(1)
        print("Congratulations, you win!")
    elif choice == "run":
        print("You run away from the wolves.")
        time.sleep(2)
        print("You manage to escape and continue on your journey.")
        time.sleep(1)
        print("You find a beautiful meadow.")
        time.sleep(1)
        meadow()
    else:
        print("Invalid choice. Please enter 'fight' or 'run'.")
        right_path()

def cave():
    print("You enter the cave.")
    time.sleep(1)
    print("It's dark and damp inside.")
    time.sleep(1)
    print("You hear a growling noise.")
    time.sleep(1)
    print("A bear appears!")
    time.sleep(1)
    choice = input("Do you try to fight the bear or run away? Fight or run? ").lower()
    if choice == "fight":
        print("You bravely fight the bear.")
        time.sleep(2)
        print("Unfortunately, the bear is too strong and defeats you.")
        game_over()
    elif choice == "run":
        print("You run away from the bear.")
        time.sleep(2)
        print("You manage to escape and continue on your journey.")
        time.sleep(1)
        print("You find a beautiful meadow.")
        time.sleep(1)
        meadow()
    else:
        print("Invalid choice. Please enter 'fight' or 'run'.")
        cave()

def meadow():
    print("You rest in the peaceful meadow.")
    time.sleep(1)
    print("You feel refreshed and ready to continue your adventure.")
    time.sleep(1)
    print("You see a path leading out of the meadow.")
    time.sleep(1)
    print("You follow the path and eventually find your way out of the forest.")
    time.sleep(2)
    print("Congratulations, you made it out of the forest!")
    time.sleep(1)
    print("Thanks for playing!")

def game_over():
    print("Game over. Would you like to play again?")
    play_again = input("Enter 'yes' to play again or 'no' to quit: ").lower()
    if play_again == "yes":
        start_game()
    elif play_again == "no":
        print("Thanks for playing!")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        game_over()

def start_game():
    intro()
    choose_path()

# Start the game
start_game()