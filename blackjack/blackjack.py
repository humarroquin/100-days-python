import random
import game_assets

def get_random_card():
    return random.choice(game_assets.CARDS)

def draw_card(cards_list):
    card = get_random_card()
    cards_list.append(card)

def sum_numbers(cards_list):
    card_total = 0
    for card in cards_list:
        card_total += game_assets.CARD_VALUES[card]
    return card_total

def print_player_score(player_cards, player_score):
    print("Player Cards:")
    
    #todo: turn this into a reusable function
    all_cards = []
    for card in player_cards:
        split_card = game_assets.CARD_ART[card].splitlines()
        cleaned_split_card = []
        for i in split_card:
            if i != "": 
                cleaned_split_card.append(i)
        all_cards.append(cleaned_split_card)

    for row in range(3):
        for card in all_cards:
            print(card[row], end=" ")
        print()

    print(f"Score: {player_score}\n")

def print_computer(computer_cards):
    print("Computer Cards:")
 
    all_cards = []
    first_card = computer_cards[0]
    
    # Card 1
    split_card = game_assets.CARD_ART[first_card].splitlines()
    cleaned_card = []
    for i in split_card:
            if i != "": 
                cleaned_card.append(i)
    all_cards.append(cleaned_card)

    # Hidden card
    card_hidden = game_assets.CARD_ART["HIDDEN"].splitlines()
    card_cleaned_hidden = []
    for i in card_hidden:
            if i != "": 
                card_cleaned_hidden.append(i)
    all_cards.append(card_cleaned_hidden)

    for row in range(3):
        for card in all_cards:
            print(card[row], end=" ")
        print()

def initialize_game(player_cards, house_cards):
    for i in range(2):
        draw_card(player_cards)
        draw_card(house_cards)
    
    player_sum = sum_numbers(player_cards)
    house_sum = sum_numbers(house_cards)

    print_player_score(player_cards, player_sum)
    print_computer(house_cards)
    return player_sum, house_sum

# === game logic starts ===
def game_logic():
    print(game_assets.BLACKJACK_SCREENS["title"])
    player_cards = []
    house_cards = []

    current_player_score, house_score = initialize_game(player_cards, house_cards)
    
    while current_player_score < 21:
        hit_me = input("Do you want another card? Yes or No? ").lower()
        
        if hit_me == "yes":
            draw_card(player_cards)
            current_player_score = sum_numbers(player_cards)
            print_player_score(player_cards, current_player_score)
        else:
            break
    
        if current_player_score == 21:
            print(game_assets.BLACKJACK_SCREENS["win"])
            print_player_score(player_cards, current_player_score)
            return

        elif current_player_score > 21:
            print(game_assets.BLACKJACK_SCREENS["bust"])
            print_player_score(player_cards, current_player_score)
            print_computer_score(house_cards, house_score)
            return

    if current_player_score < house_score:
        print(game_assets.BLACKJACK_SCREENS["bust"])
    elif current_player_score == house_score:
        print(game_assets.BLACKJACK_SCREENS["push"])
    else:
        print(game_assets.BLACKJACK_SCREENS["win"])
        print_player_score(player_cards, current_player_score)
        print_computer_score(house_cards, house_score)
    
    continue_playing = input("Play again? Yes or No? ").lower()
    if continue_playing == "yes":
        game_logic()
    else:
        print("Thank you for playing!")

game_logic()
