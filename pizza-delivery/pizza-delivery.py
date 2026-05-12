print("Welcome to the pizza delivery app")
total_price = 0

size = input("What size pizza do you want: S M L? ").lower()
if size == "s":
    total_price = 15
elif size == "m":
    total_price = 20
elif size == "l":
    total_price = 25

pepperoni = input("Do you want pepperoni: Y or N? ").lower()
if pepperoni == "y":
    if size == "s":
        total_price += 2
    else:
        total_price += 3

extra_cheese = input("Do you want extra cheese: Y or N? ").lower()
if extra_cheese == "y":
    total_price += 1

print(f"Your total is {total_price}")