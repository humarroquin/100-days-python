ascii_assets = {
    "header": r"""
================================
 🏛️ Welcome to Silent Auction 🏛️
================================
Today's Item: Porsche 2020
"""
}

import os
def clear_screen():
    os.system("clear")

bidder_records = {}
def add_bids():
    get_name = input("What's your name? \n")

    get_bid = int(input("What's your bid? \n$"))
    while get_bid <= 0:
        get_bid = int(input("Bids can't be $0.00 or less. Bid again: \n$"))

    bidder_records[get_name] = get_bid

def check_bids(bids):
    highest_bid = 0
    bid_key = ""
    for key, value in bids.items():
        if value > highest_bid:
            highest_bid = value
            bid_key = key

    return highest_bid, bid_key

while True:
    print(ascii_assets["header"])
    add_bids()
    add_bidders = input("Are there more bidders? 'y' = yes 'n' = no \n")
    clear_screen()

    if add_bidders != "y":
        print(ascii_assets["header"])
        if not bidder_records:
            print("No bids were placed.")
        else:
            bid, bidder = check_bids(bidder_records)
            print(f"🏆 {bidder} is the winner with a bid of ${bid} 🎉")
        break
