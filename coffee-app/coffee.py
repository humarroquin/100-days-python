available_resources = {
    "water": 100,
    "milk": 50,
    "coffee":76,
    "money": 0
}

coffee_options = {
    "cappuccino": {"water": 30, "milk": 10, "coffee": 10, "money": 2.5},
    "latte": {"water": 30, "milk": 20, "coffee": 10, "money": 1.5},
    "espresso": {"water": 30, "milk": 0, "coffee": 10, "money": 1.75}
}

def check_resources(coffee_choice, available_resources):
    water_needed = coffee_choice["water"]
    coffee_needed = coffee_choice["coffee"]
    milk_needed = coffee_choice["milk"]
    water_available = available_resources["water"]
    coffee_available = available_resources["coffee"]
    milk_available = available_resources["milk"]

    return water_needed <= water_available and coffee_needed <= coffee_available and milk_needed <= milk_available
        
def update_resources(coffee_choice, available_resources):
    water_needed = coffee_choice["water"]
    coffee_needed = coffee_choice["coffee"]
    milk_needed = coffee_choice["milk"]
    water_available = available_resources["water"]
    coffee_available = available_resources["coffee"]
    milk_available = available_resources["milk"]

    available_resources["water"] = water_available - water_needed
    available_resources["coffee"] = coffee_available - coffee_needed
    available_resources["milk"] = milk_available - milk_needed
    
def sum_money(quarters, dimes, nickels, pennies):
    q_money_inserted = quarters * 0.25
    d_money_inserted = dimes * 0.1
    n_money_inserted = nickels * 0.05
    p_money_inserted = pennies * 0.01
    
    return q_money_inserted + d_money_inserted + n_money_inserted + p_money_inserted

# logic starts
print(available_resources)

available_options = ["espresso", "latte", "cappuccino", "off", "report"]
choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
while True:
    if choice not in available_options:
        print("Please select one of the available choices.")
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    else:
        break

if choice == "off":
    print("Machine turning off...")
else:
    has_resources = check_resources(coffee_options[choice], available_resources)
    if has_resources:
        quarters = int(input("Insert total quarters: "))
        nickels = int(input("Insert total nickels: "))
        dimes = int(input("Insert total dimes: "))
        pennies = int(input("Insert total pennies: "))
        money_inserted = sum_money(quarters, nickels, dimes, pennies)
        # print(round(money_inserted, 2))

        coffee_price = coffee_options[choice]["money"]
        if coffee_price > money_inserted:
            print(f"Insufficient funds. Coffee is ${coffee_price}. You inserted ${round(money_inserted, 2)}.")
        else:
            print(f"""Coffee will be ready soon.
Printing receipt:
>> Coffee is ${coffee_price}. 
>> You inserted ${round(money_inserted, 2)}. 
>> Your change is ${round(money_inserted - coffee_price, 2)}""")
            available_resources["money"] += coffee_price

            # update resources
            update_resources(coffee_options[choice], available_resources)
    else:
        print("Coffee option not available at the moment.")

print(available_resources)