import random

def get_computer_choice():
    choices = ['Snake', 'Water', 'Gun']
    return random.choice(choices)

def get_user_choice():
    user_input = input("Enter your choice (Snake, Water, Gun): ")
    while user_input not in ['Snake', 'Water', 'Gun']:
        print("Invalid choice. Please choose again.")
        user_input = input("Enter your choice (Snake, Water, Gun): ")
    return user_input

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Snake' and computer_choice == 'Water') or \
         (user_choice == 'Water' and computer_choice == 'Gun') or \
         (user_choice == 'Gun' and computer_choice == 'Snake'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to the Snake Water Gun Game!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
