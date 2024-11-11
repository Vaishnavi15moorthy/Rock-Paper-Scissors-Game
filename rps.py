import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"


def get_user_choice():
    print("\nRock, Paper, Scissors Game")
    print("Please choose one of the following options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Enter 8, 9, or 3: ")

    if choice == '8':
        return "rock"
    elif choice == '9':
        return "paper"
    elif choice == '3':
        return "scissors"
    else:
        print("Invalid choice, please choose again.")
        return get_user_choice()
def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose {user_choice}, Computer chose {computer_choice}.")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"\nCurrent Score: You - {user_score}, Computer - {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    play_game()
