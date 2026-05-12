# PATTERNS
treasure = """
   _________
  /         \\
 / TREASURE! \\
|   💰 💰 💰   |
|             |
|_____________|
"""

hole = """
      #######
    ##       ##
   #   #####   #
  #   ##   ##   #
  #   ##   ##   #
   #   #####   #
    ##       ##
      #######
     YOU FELL
"""

island = """
        🌴
       🌴🌴
   ~~~~~~~~~~~
  ~           ~
 ~    🏝️     ~
  ~           ~
   ~~~~~~~~~~~
"""

trout = """
      /\"*._         _
  .-*'`    `*-.._.-'/ 
 < * ))     ,       ( 
  `*-._`._(__.--*\"`.\\
        TROUT
"""

doors = """
   _______     _______     _______
  |  __   |   |  __   |   |  __   |
  | |  |  |   | |  |  |   | |  |  |
  | |  |  |   | |  |  |   | |  |  |
  | |__|  |   | |__|  |   | |__|  |
  |   __  |   |   __  |   |   __  |
  |  |  | |   |  |  | |   |  |  | |
  |__|__|_|   |__|__|_|   |__|__|_|
     1            2            3
"""

fire = """
     (  )
    (    )
   (      )
    \\    /
     \\  /
      \\/
      /\\
     /  \\
    FIRE
"""

gold = """
   _______
  /       \\
 |  GOLD!  |
 |  💰💰💰  |
  \\_______/
"""

beasts = """
   /\\_/\\
  ( o o )
  /  V  \\
 /(  _  )\\
   ^^ ^^
  BEASTS
"""

def treasure_island_game():
    print("Welcome to Treasure Island!\nYour mission is to find the treasure.")
    print(treasure)

    first_question = input('You are at a crossroad. Where do you want to go? "Left" or "Right"? ').lower()

    if first_question == "right":
        print("You fell into a hole. You're dead!")
        print(hole)
        return
    
    print("You have come to a lake. There is an island in the middle of the lake.")
    print(island)
    second_question = input('Do you want to "SWIM" or "WAIT" for a boat? ').lower()
    
    if second_question == "swim":
        print("You get attacked by an angry trout! You're dead")
        print(trout)
        return

    print("You arrive to the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.")
    print(doors)
    third_question = input("Which color do you choose? ").lower()

    if third_question == "red":
        print("It's a room full of fire! You're dead")
        print(fire)
        return
    elif third_question == "yellow":
        print("You found the treasure. You win!")
        print(treasure)
        return
    elif third_question == "blue":
        print("You enter a rooms of beasts! You are dead!")
        print(beasts)
        return

while True:
    treasure_island_game()

    player_choice = input('Do you want to play again: "YES" or "NO"? ').lower()
    if player_choice != "yes":
        print("Thanks for playing.")
        break
