import random

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("Rock, Paper, Scissors")
        print("Enter your choice (rock, paper, scissors) or 'quit' to exit: ")
        user_choice = input().lower()
        if user_choice == 'quit':
            break

        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'scissors' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')
        ):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print("Your score:", user_score)
        print("Computer score:", computer_score)
        print()
