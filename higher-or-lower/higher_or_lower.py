from game_data import data
from random import choice

def get_random_choice(data_list):
    return choice(data_list)

def get_game_data():
    while True:
        option_a = get_random_choice(data)
        option_b = get_random_choice(data)
        
        if option_a != option_b:
            return option_a, option_b

def check_winner(option_a, option_b):
    won_round = False

    print(f"A: {option_a['name']} is a {option_a['description']} from the {option_a['country']}.")
    print("-VS-")
    print(f"B: {option_b['name']} is a {option_b['description']} from the {option_b['country']}.")

    users_choice = input("\nWho has more followers, A or B? ").lower()
    
    correct_choice = ""
    winner = ""
    if option_a["followers"] > option_b["followers"]:
        correct_choice = "a"
        winner = option_a
    else:
        correct_choice = "b"
        winner = option_b
    
    if users_choice == correct_choice:
        print("That's correct")
        won_round = True
    else:
        print("That's not correct. Game Over!")
    
    print(f"{option_a['name']} has {option_a['followers']} and {option_b['name']} has {option_b['followers']}.")

    return won_round, winner

a, b = get_game_data()
game_status, winner = check_winner(a, b)
if game_status:
    opt_b = get_random_choice(data)
    check_winner(winner, opt_b)