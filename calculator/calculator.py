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
def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def divide(num_1, num_2):
    return num_1 / num_2

def multiply(num_1, num_2):
    return num_1 * num_2

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
    result = do_calc(first_num, operation, next_num)
    return result

# start function
def start_calc():
    calculation = get_result()
    print(calculation)

    is_continue = True
    while is_continue:
        continue_calc = input("Continue calculation? Yes or No: ").lower()
        
        if continue_calc == "yes":
            new_calc = get_result(calculation)
            calculation = new_calc
            print(new_calc)
        else:
            is_continue = False
            print("Calculation completed")

start_calc()