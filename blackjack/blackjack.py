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

def print_cards_and_score(cards, user, score="**"):
    print(f"{user} Cards:")
    
    all_cards = []
    for card in cards:
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

    print(f"Score: {score}\n")

def initialize_game(player_cards, house_cards):
    for i in range(2):
        draw_card(player_cards)
        draw_card(house_cards)
    
    player_sum = sum_numbers(player_cards)
    house_sum = sum_numbers(house_cards)

    print_cards_and_score(player_cards, "Player", player_sum)

    initial_house_display = [house_cards[0], "HIDDEN"]
    print_cards_and_score(initial_house_display, "House")

    return player_sum, house_sum

# === game logic starts ===
def game_logic():
    print(game_assets.BLACKJACK_SCREENS["title"])
    player_cards = []
    house_cards = []

    current_player_score, current_house_score = initialize_game(player_cards, house_cards)
    game_status = ""

    # player starts turn
    active_game = True
    while active_game:
        hit_me = input("Do you want another card? Yes or No? ").lower()
        
        if hit_me == "yes":
            draw_card(player_cards)
            current_player_score = sum_numbers(player_cards)

            print_cards_and_score(player_cards, "Player", current_player_score)
            initial_house_display = [house_cards[0], "HIDDEN"]
            print_cards_and_score(initial_house_display, "House")

            if current_player_score > 21:
                game_status = "player_bust"
                active_game = False
            elif current_player_score == 21:
                game_status = "player_wins"
                active_game = False

        else:
            active_game = False
    
    if game_status == "player_bust" or game_status == "player_wins":
        print(game_assets.BLACKJACK_SCREENS[game_status])
        print_cards_and_score(player_cards, "Player", current_player_score)
    
    else:
        # dealer starts turn
        while current_house_score < 17:
            draw_card(house_cards)
            current_house_score = sum_numbers(house_cards)
            print_cards_and_score(player_cards, "Player", current_player_score)
            print_cards_and_score(house_cards, "House", current_house_score)

            if current_house_score > 21:
                game_status = "house_bust"

            elif current_house_score == 21:
                game_status = "house_wins"

        if game_status == "house_bust" or game_status == "house_wins":
            print(game_assets.BLACKJACK_SCREENS[game_status])
            print_cards_and_score(house_cards, "House", current_house_score)

        else:
            if current_player_score > current_house_score:
                game_status = "player_wins"
            elif current_player_score == current_house_score:
                game_status = "push"
            else:
                game_status = "house_wins"

            print(game_assets.BLACKJACK_SCREENS[game_status])
            print_cards_and_score(player_cards, "Player", current_player_score)
            print_cards_and_score(house_cards, "House", current_house_score)

    continue_playing = input("Play again? Yes or No? ").lower()
    if continue_playing == "yes":
        game_logic()
    else:
        print("""> blackjack
dealer disconnected.
game terminated.""")

game_logic()