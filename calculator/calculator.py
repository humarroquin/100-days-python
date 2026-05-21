def get_numbers():
    while True:
        try:
            num = float(input("Enter number: "))
            return num
        except ValueError:
            print("The calculator only works with numbers.")

def get_operation():
    valid_operations = ["-", "+", "*", "/"]
    while True:
        operation = input("Enter operation(- + * /): ")
        if operation in valid_operations:
            return operation
        else:
            print("Not a valid operator")

# calculations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

# call the calculation
def do_calc(first_num, operation, second_num):
    operations = {
         "+": add,
         "-": subtract,
         "/": divide,
         "*": multiply
    }
    return operations[operation](first_num, second_num)

def get_result(saved_calculation=None):
    if saved_calculation is None:
        first_num = get_numbers()
    else:
        first_num = saved_calculation
    operation = get_operation()
    next_num = get_numbers()
    try:
        result = do_calc(first_num, operation, next_num)
        return result
    except ZeroDivisionError:
        print("Can't divide by zero")
        return first_num

def get_user_choice():
    valid_options = ["yes", "no"]
    while True:
        user_choice = input("Continue calculation? Yes or No: ").lower()
        if user_choice in valid_options:
            return user_choice
        else:
            print("This is not a valid option")

# start function
def start_calc():
    calculation = get_result()
    print(calculation)

    while True:
        user_choice = get_user_choice()
        if user_choice == "yes":
            new_calc = get_result(calculation)
            calculation = new_calc
            print(new_calc)
        else:
            print("Calculation completed")
            break

start_calc()