import random
import game_assets

CARDS = [
    "A",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K"
]

def get_random_card():
    return random.choice(CARDS)

def draw_card(cards_list):
    card = get_random_card()
    cards_list.append(card)

def sum_numbers(cards_list):
    card_total = 0
    for card in cards_list:
        card_total += game_assets.CARD_VALUES[card]
    return card_total

def print_player_score(player_cards, player_score):
    print(f"Score: {player_score}")
    for i in player_cards:
        print(game_assets.CARD_ART[i])

def print_computer_score(computer_cards, computer_score):
    print(f'Computer Cards: {" ".join(map(str, computer_cards))} | Score: {computer_score}')

def initialize_game(player_cards, house_cards):
    for i in range(2):
        draw_card(player_cards)
        draw_card(house_cards)
    
    player_sum = sum_numbers(player_cards)
    house_sum = sum_numbers(house_cards)

    print_player_score(player_cards, player_sum)
    print(f"House cards: {house_cards[0]}")
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
            print("\nYou lose!")
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
