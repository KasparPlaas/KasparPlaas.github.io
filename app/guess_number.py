import random

def play_guess_number(guess):
    secret_number = random.randint(1, 20)
    
    if guess == secret_number:
        return f"Congratulations! You guessed the correct number: {secret_number}."
    elif guess < secret_number:
        return "Too low! Try a higher number."
    else:
        return "Too high! Try a lower number."