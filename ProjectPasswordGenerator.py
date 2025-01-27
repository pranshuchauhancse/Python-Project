print("Welcome to the Password Generator!")

# Define character sets manually
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special_characters = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

all_characters = lowercase + uppercase + digits + special_characters

# Manual random selection using user input for index
def manual_random_choice(sequence):
    index = int(input(f"Enter a number between 0 and {len(sequence) - 1}: ")) % len(sequence)
    return sequence[index]

# Shuffle a list manually
def manual_shuffle(sequence):
    for i in range(len(sequence)):
        swap_index = int(input(f"Enter a number to shuffle index {i} (0 to {len(sequence) - 1}): ")) % len(sequence)
        sequence[i], sequence[swap_index] = sequence[swap_index], sequence[i]

while True:
    print("\n=== Password Generator Menu ===")
    print("1. Generate Password")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":  # Generate Password
        try:
            length = int(input("Enter the desired password length (minimum 6): "))
            if length < 6:
                print("Error: Password length must be at least 6 for better security.")
                continue

            # Ensure at least one character from each set
            password = [
                manual_random_choice(lowercase),
                manual_random_choice(uppercase),
                manual_random_choice(digits),
                manual_random_choice(special_characters)
            ]

            # Fill the rest of the password with random choices
            for _ in range(length - 4):
                password.append(manual_random_choice(all_characters))

            # Shuffle manually
            manual_shuffle(password)

            # Join the list into a string
            final_password = ''.join(password)
            print(f"\nGenerated Password: {final_password}")
        except ValueError:
            print("Error: Please enter a valid number.")

    elif choice == "2":  # Exit
        print("Goodbye! Stay secure with strong passwords.")
        break

    else:
        print("Invalid choice! Please try again.")