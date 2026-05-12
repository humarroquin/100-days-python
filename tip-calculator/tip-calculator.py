# Welcome to the tip calculator!
# What was the total bill? $
# 300
# How much tip would you like to give? 10, 12, or 15? 
# 10
# How many people to split the bill?
# 2
# Each person should pay: $165.00

def validate_tip(percentage):
    VALID_PERCENTAGES = (10, 12, 15)
    if percentage not in VALID_PERCENTAGES:
        raise ValueError("Select the correct percentage\n")
    return percentage

def calculate_tip(bill, tip_percentage):
    return bill * tip_percentage / 100

def total_bill(bill, tip):
    return bill + tip

def divide_total_bill(bill, number_of_people):
    return bill / number_of_people

def tip_calculator():
   while True:
    try:
        bill = float(input("What was the total bill\n"))
        if bill > 0:
            break
        raise ValueError
    except ValueError:
        print("Bill must be more than 0.00")
   while True:
    try:
        tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
        validated_tip = validate_tip(tip)
        break
    except ValueError as e:
           print(e)
   num_people = int(input("How many people to split the bill?\n"))
   tip_cal = calculate_tip(bill, validated_tip)
   bill_total = total_bill(bill, tip_cal)
   total_per_person = divide_total_bill(bill_total, num_people)
   print(f"Each person should pay: ${total_per_person:.2f}")

tip_calculator()

# def tip_calculator():
#     bill = int(input("What was the total bill?\n"))
#     tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15?\n")) / 100
#     number_of_people = int(input("How many people to split the bill?\n"))

#     total_bill = bill + bill * tip_percentage
#     payment_per_person = total_bill / number_of_people

#     print(f"Each person should pay: ${payment_per_person:.2f}")

# tip_calculator()
