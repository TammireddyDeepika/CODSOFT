import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_input = input("Enter your choice (rock, paper, scissors): ").strip().lower()
        if user_input in choices:
            return user_input
        print("Invalid input! Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    print("----- ROCK-PAPER-SCISSORS GAME -----")
    
    user_score = 0
    computer_score = 0
    round_number = 1
    
    while True:
        print(f"\nRound {round_number}:")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "user":
            print("You win this round!")
            user_score += 1
        elif winner == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("This round is a tie!")
        
        print(f"Score -> You: {user_score} | Computer: {computer_score}")
        
        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("\nFinal Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break
        
        round_number += 1

# Start the game
if __name__ == "__main__":
    play_game()
