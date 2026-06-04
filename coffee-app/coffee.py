available_resources = {
    "water": 100,
    "milk": 0,
    "coffee":0,
    "money": 0
}

coffee_options = {
    "cappuccino": {"water": 30, "milk": 10, "coffee": 10, "money": 2.5},
    "latte": {"water": 30, "milk": 20, "coffee": 10, "money": 1.5},
    "espresso": {"water": 300, "milk": 0, "coffee": 10, "money": 1.75}
}

def get_variables(coffee_choice, available_resources):
    water_needed = coffee_choice["water"]
    coffee_needed = coffee_choice["coffee"]
    milk_needed = coffee_choice["milk"]
    water_available = available_resources["water"]
    coffee_available = available_resources["coffee"]
    milk_available = available_resources["milk"]
    return water_needed, coffee_needed, milk_needed, water_available, coffee_available, milk_available

def check_resources(coffee_choice, available_resources):
    water_needed, coffee_needed, milk_needed, water_available, coffee_available, milk_available = get_variables(coffee_choice, available_resources)

    missing_ingredients = []
    can_make_drink = True
    if water_available < water_needed:
        missing_ingredients.append("Not enough water")
        can_make_drink = False
    if coffee_available < coffee_needed:
        missing_ingredients.append("Not enough coffee")
        can_make_drink = False
    if milk_available < milk_needed:
        missing_ingredients.append("Not enough milk")
        can_make_drink = False

    return can_make_drink, missing_ingredients

def update_resources(coffee_choice, available_resources):
    water_needed, coffee_needed, milk_needed, water_available, coffee_available, milk_available = get_variables(coffee_choice, available_resources)

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
is_on = True
available_options = ["espresso", "latte", "cappuccino", "off", "report"]

while is_on:
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice in available_options:
            break
        
        print("Please select one of the available choices.")

    if choice == "off":
        print("Machine turning off...")
        is_on = False
    elif choice == "report":
        print(available_resources)
    else:
        selected_drink = coffee_options[choice]
        has_resources, message = check_resources(selected_drink, available_resources)
        if has_resources:
            quarters = int(input("Insert total quarters: "))
            nickels = int(input("Insert total nickels: "))
            dimes = int(input("Insert total dimes: "))
            pennies = int(input("Insert total pennies: "))
            money_inserted = sum_money(quarters, nickels, dimes, pennies)

            coffee_price = selected_drink["money"]
            if coffee_price > money_inserted:
                print(f"Insufficient funds. Coffee is ${coffee_price}. You inserted ${round(money_inserted, 2)}.")
            else:
                print(f"""Your {choice} will be ready soon.
Printing receipt:
>> Coffee is ${coffee_price}. 
>> You inserted ${round(money_inserted, 2)}. 
>> Your change is ${round(money_inserted - coffee_price, 2)}""")
                available_resources["money"] += coffee_price

                # update resources
                update_resources(selected_drink, available_resources)
        else:
            print(f"Coffee option not available at the moment.")
            for item in message:
                print(item)
