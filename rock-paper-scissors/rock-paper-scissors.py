import random

WARNING_MESSAGE = """
============================
Invalid Input! Try again.
============================
"""
hands = ("rock", "paper", "scissors")

hands_art = {
            "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

def user_computer_hands():
    while True:
        try:
            user = int(input("Type 1=Rock, 2=Paper, 3=Scissors:\n"))
            if user in {1, 2, 3}:
                break
            print(WARNING_MESSAGE)
        except ValueError:
            print(WARNING_MESSAGE)
    computer = random.choice(hands)
    return select_winner(hands[user - 1], computer)

def select_winner(player, computer):
    if player == "paper" and computer == "rock":
        return f"""{hands_art[player]}
    {hands_art[computer]}
    You win!"""
    elif player == "rock" and computer == "scissors":
        return f"""{hands_art[player]}
    {hands_art[computer]}
    You win!"""
    elif player == "scissors" and computer == "paper":
        return f"""{hands_art[player]}
    {hands_art[computer]}
    You win!"""
    elif player == computer:
        return f"""{hands_art[player]}
    {hands_art[computer]}
    It's a draw!"""
    else:
        return f"""{hands_art[player]}
    {hands_art[computer]}
    You lose!"""

def play_game():
    message = user_computer_hands()
    if message:
        print(message)

while True:
    play_game()
    play_again = input("Play again?\n").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
