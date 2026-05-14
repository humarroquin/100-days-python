def validate_data():
    first_num = float(input("Enter first number: "))
    operation = input("Enter operation(- + * /): ")
    second_num = float(input("Enter first number: "))
    return first_num, operation, second_num

# calculations
def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def divide(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        print("You can't divide by zero")

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

def get_result():
    first_num, operation, next_num = validate_data()
    result = do_calc(first_num, operation, next_num)
    return result

def continue_result(saved_calculation):
    second_num = float(input("Enter next number: "))
    operation = input("Enter operation(- + * /): ")
    result = do_calc(saved_calculation, operation, second_num)
    return result

# start function
def start_calc():
    calculation = get_result()
    print(calculation)

    is_continue = True
    while is_continue:
        continue_calc = input("Continue calculation? Yes o No: ").lower()
        
        if continue_calc == "yes":
            new_calc = continue_result(calculation)
            calculation = new_calc
            print(new_calc)
        else:
            is_continue = False
            print("Calculation completed")

start_calc()