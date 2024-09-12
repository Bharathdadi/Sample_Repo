import random

def number_guess_game():
    """A simple number guessing game."""
    # Define the range for the random number
    min_number = 1
    max_number = 100
    
    # Generate a random number between min_number and max_number
    number_to_guess = random.randint(min_number, max_number)
    
    print(f"Guess the number between {min_number} and {max_number}.")

    attempts = 0
    while True:
        try:
            # Get the user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < min_number or guess > max_number:
                print(f"Please enter a number between {min_number} and {max_number}.")
                continue

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    number_guess_game()
