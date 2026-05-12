import string
import random

letters = list(string.ascii_lowercase + string.ascii_uppercase)
numbers = list(string.digits)
symbols = list("!@#$%^&*()")

def get_list_items(total_items, source_list):
    selected_items = []
    for i in range(total_items):
        selected_item = random.choice(source_list)
        selected_items.append(selected_item)
    return selected_items

def generate_new_password():
    print("Welcome to Password Generator!")

    # get user input
    requested_letters = int(input("How many letters? \n"))
    requested_numbers = int(input("How many numbers? \n"))
    requested_symbols = int(input("How many symbols? \n"))

    #get random characters/numbers
    returned_letters = get_list_items(requested_letters, letters)
    returned_numbers = get_list_items(requested_numbers, numbers)
    returned_symbols = get_list_items(requested_symbols, symbols)

    new_password = returned_letters + returned_numbers + returned_symbols
    random.shuffle(new_password)
    print("Your password is: " + "".join(new_password))

generate_new_password()
