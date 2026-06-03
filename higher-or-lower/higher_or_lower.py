from game_data import data
from random import choice

def get_random_choice(data_list):
    return choice(data_list)

def start_game():
    while True:
        option_a = get_random_choice(data)
        option_b = get_random_choice(data)
        
        if option_a != option_b:
            return option_a, option_b
        
def show_vs_screen(option_a, option_b):
    print("\n==================================================\n")
    print(f"A: {option_a['name']} is a {option_a['description']} from the {option_a['country']}.")
    print("-VS-")
    print(f"B: {option_b['name']} is a {option_b['description']} from the {option_b['country']}.")
    print("\n==================================================")

def play(option_a, option_b, score):

    followers_a = option_a["followers"]
    followers_b = option_b["followers"]
    name_a = option_a["name"]
    name_b = option_b["name"]

    show_vs_screen(option_a, option_b)
    user_choice = input("\nWho has more followers, A or B? \n").lower()
    
    if followers_a > followers_b:
        correct_option = "a"
        round_winner = option_a
    else:
        correct_option = "b"
        round_winner = option_b
    
    if user_choice == correct_option:
        score += 100
        print(f"That's correct! Your score is {score}")
    else:
        print(f"Game Over! Final Score: {score}")
    
    active = user_choice == correct_option
    print(f"{name_a} has {followers_a} and {name_b} has {followers_b}.")

    return active, round_winner, score

# initial game logic
score = 0
initial_a, initial_b = start_game()
active_game, winner, score = play(initial_a, initial_b, score)

# active game logic
while active_game:
    opt_b = get_random_choice(data)
    while opt_b == winner:
        opt_b = get_random_choice(data)

    active_game, winner, score = play(winner, opt_b, score)