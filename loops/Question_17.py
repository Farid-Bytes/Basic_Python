secret_number = 7  # Assume a predefined secret number
guess = None
while guess != secret_number:
    guess = int(input("Guess the number between 1 and 10: "))
    if guess == secret_number:
        print("Correct! You've guessed the number.")
    else:
        print("Wrong guess. Try again.")
