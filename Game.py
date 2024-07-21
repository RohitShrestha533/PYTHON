import sys
import random

# Rock Scissors Paper Game
choices = ["rock", "scissors", "paper"]
user_score = 0
computer_score = 0

def stop_game():
    if computer_score == user_score:
        print(f"The game is a tie: computer score: {computer_score} and your score: {user_score}")
    elif computer_score > user_score:
        print(f"The winner of this game is the computer: Score {computer_score} - {user_score}")
    else:
        print(f"Congratulations! You are the winner of this game. Score: {user_score} - {computer_score}")
    sys.exit()

def start_game():
    global user_score, computer_score
    while True:
        user = input("Enter rock, scissors, paper or 'exit' to stop the game: ").lower()
        computer = random.choice(choices)
        
        if user == "exit":
            stop_game()
        elif user not in choices:
            print("Invalid choice. Please enter again.\n")
        elif user == computer:
            print(f"Tie \nYour choice: {user} \nComputer choice: {computer} \nScore: You {user_score} - Computer {computer_score}")
        elif (user == "rock" and computer == "scissors") or (user == "scissors" and computer == "paper") or (user == "paper" and computer == "rock"):
            user_score += 1
            print(f"You win this round \nYour choice: {user} \nComputer choice: {computer} \nScore: You {user_score} - Computer {computer_score}")
        else:
            computer_score += 1
            print(f"Computer wins this round \nComputer choice: {computer} \nYour choice: {user} \nScore: Computer {computer_score} - You {user_score}")

start_game()
