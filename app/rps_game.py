import random

def play_rps(player_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    if player_choice not in choices:
        return "Invalid choice! Choose among 'rock', 'paper', or 'scissors'."
    
    if player_choice == computer_choice:
        return f"It's a tie! Both chose {player_choice}."
    
    if (player_choice == 'rock' and computer_choice == 'scissors') or \
       (player_choice == 'paper' and computer_choice == 'rock') or \
       (player_choice == 'scissors' and computer_choice == 'paper'):
        return f"You win! Computer chose {computer_choice}."
    
    return f"You lose! Computer chose {computer_choice}."