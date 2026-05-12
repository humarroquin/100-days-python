import random

title = """
 _    _                                         
| |  | |                                        
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __   
|  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\  
| |  | | (_| | | | | (_| | | | | | | (_| | | | | 
|_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_| 
                     __/ |                      
                    |___/                       
"""

stage0 = """
  +---+
  |   |
      |
      |
      |
      |
=========
"""

stage1 = """
  +---+
  |   |
  O   |
      |
      |
      |
=========
"""

stage2 = """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
"""

stage3 = """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
"""

stage4 = """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
"""

stage5 = """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
"""

stage6 = """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""

stages = [stage0, stage1, stage2, stage3, stage4, stage5, stage6]
words = ["replace", "index"]
lives = 6
words_guessed = []

# FUNCTIONS
def hide_word(word):
    hidden_word = []
    for letter in word:
        hidden_word.append("_")
    return hidden_word

def check_guess(guess, word_list, hidden_word):
    correct_guess = True
        
    if guess not in word_list:
        correct_guess = False

    for index in range(len(word_list)):
        if word_list[index] == guess:
            hidden_word[index] = guess
    
    return correct_guess

# STEP 1: select a random word
game_word = random.choice(words)
word_list = list(game_word)
#! this is only for testing, erase later
print(word_list) 

# Welcome message
print(title)

# STEP 2: hide the word game
hidden_word = hide_word(game_word)
print("Your word is " + " ".join(hidden_word))
print(stage0)

# STEP 3: check guesses
while lives > 0:
    guess = input("Select a letter: ").lower()

    if guess in words_guessed:
        print("You've already guessed this letter!")
    else:
        words_guessed.append(guess)
        correct_guess = check_guess(guess, word_list, hidden_word)   
        print("Your word is " + " ".join(hidden_word))
        if not correct_guess:
            lives -= 1
            # ? How do I stop this from printing when lives are at 0?
            print(f"Try again! You have {lives} lives left.")
        else:
            print("Nice! You found a letter.")
        index = (len(stages) - 1) - lives
        print(stages[index])

    if lives == 0:
        print("Game Over!")
        break

    if game_word == "".join(hidden_word):
        print("You guessed the word! Great job!")
        break
