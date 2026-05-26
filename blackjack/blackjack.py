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

def print_player_score(player_cards, player_score):
    print(f'Player Cards: {" ".join(map(str, player_cards))} | Score: {player_score}')

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
            print("You win!")
            print_player_score(player_cards, current_player_score)
            return

        elif current_player_score > 21:
            print("\nYou lose!")
            print_player_score(player_cards, current_player_score)
            print_computer_score(house_cards, house_score)
            return

    if current_player_score < house_score:
        print("House wins!")
    else:
        print("You win!")
        print_player_score(player_cards, current_player_score)
        print_computer_score(house_cards, house_score)
    
    continue_playing = input("Play again? Yes or No? ").lower()
    if continue_playing == "yes":
        game_logic()
    else:
        print("Thank you for playing!")

game_logic()
