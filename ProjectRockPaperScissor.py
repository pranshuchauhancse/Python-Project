print("Welcome to Rock, Paper, Scissors!")

# Define valid choices
choices = ["rock", "paper", "scissors"]


# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"


# Initialize scores
user_score = 0
computer_score = 0

while True:
    print("\n=== Rock, Paper, Scissors Menu ===")
    print("Choose your option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    user_input = input("Enter your choice (1-4): ")

    if user_input in ["1", "2", "3"]:  # User chooses rock, paper, or scissors
        user_choice = choices[int(user_input) - 1]
        print(f"You chose: {user_choice}")

        # Simulate computer's choice manually
        print("To generate computer's choice, enter a number between 0 and 2:")
        computer_index = int(input("(0 for rock, 1 for paper, 2 for scissors): "))
        computer_choice = choices[computer_index % 3]
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        # Display scores
        print(f"Score: You {user_score} - {computer_score} Computer")

    elif user_input == "4":  # Exit
        print("Thanks for playing! Final Score:")
        print(f"You: {user_score}, Computer: {computer_score}")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")