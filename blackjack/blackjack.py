import random

def generate_random_number():
    return random.randint(1, 10)

def draw_card(cards_list):
    card = generate_random_number()
    cards_list.append(card)

def sum_numbers(cards_list):
    card_total = 0
    for card in cards_list:
        card_total += card
    return card_total

def initialize_game(player_cards, house_cards):
    for i in range(2):
        draw_card(player_cards)
        draw_card(house_cards)
    
    player_sum = sum_numbers(player_cards)
    house_sum = sum_numbers(house_cards)

    print(f'Player Cards: {" ".join(map(str, player_cards))} | Current score: {player_sum}')
    print(f"House cards: {house_cards[0]}")
    return player_sum, house_sum

# === game logic starts ===
def game_logic():
    player_cards = []
    house_cards = []
    player_score = 0
    house_score = 0

    player_sum, house_sum = initialize_game(player_cards, house_cards)
    player_score = player_sum
    house_score = house_sum
    
    check = input("Do you want another card? Yes or No? ").lower()
    if check != "yes":
        if player_sum < house_sum:
            print("You lose!")
        else:
            print("You win")
    
    print(player_cards, house_cards, player_score, house_score)

game_logic()

