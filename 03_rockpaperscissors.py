import random

#putting in a loop so we can play until we get bored (one game is simply not enough)
while True:

    #let's get our inputs
    user = input("What's your choice? r (rock), p (paper), s (scissors): ")
    playable = ["r", "p", "s"]
    computer = random.choice(playable)

    #adding this here in case you are like me and want to see what the computer chose (otherwise we don't believe in the results)
    print(f"\nYou choice: {user}, computer's choice {computer}.\n")

    #now let's get to defining rules of the game
    if user == computer:
        print(f"You both selected {user}. It's a tie!")

    elif user == "r":
        if computer == "s":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")

    elif user == "p":
        if computer == "r":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")

    elif user == "s":
        if computer == "p":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    #and the last thing is the option to play again or quit the game
    play_again = input("\nPress y is you wanna try again. Good luck! ")
    if play_again.lower() != "y":
        break