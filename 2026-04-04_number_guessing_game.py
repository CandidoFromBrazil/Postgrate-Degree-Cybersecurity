import random

def play_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("--- Welcome to the Number Guessing Game! ---")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            # Get user input
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Correct! You found the number in {attempts} attempts.")
                break # Exit the loop
                
        except ValueError:
            print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    play_guessing_game()