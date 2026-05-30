import random

print("Guess the number!")
print("I'm thinking of a number from 1-100")

def play_game():
    lives = 0
    number = random.randint(1, 100)

    while True:
        difficulty_level = input("Choose difficulty game: 'easy' or 'hard': ").lower()
        if difficulty_level == "easy":
            lives = 10
            break
        elif difficulty_level == "hard":
            lives = 5
            break
        print("You must choose between EASY or HARD")

    print(f"You have {lives} lives to guess the number.")

    while lives > 0:
        guess = int(input("Guess a number: "))

        if guess < number:
            print("Guess too low.")
        elif guess > number:
            print("Guess to high")
        else:
            print(f"You win! The number was {number}")
            break

        lives -= 1
        if lives > 0:
            print(f"You have {lives} lives left.")
        else:
            print("You lost!")

while True:
    play_game()
    while True:
        play_again = input("Play again? Yes or No: ").lower()
        if play_again == "yes":
            break
        elif play_again == "no":
            print("Thank you for playing!")
            break
        print("Choose between YES or NO")
    
    if play_again != "yes":
        break