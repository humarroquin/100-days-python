def get_data():
    first_number = float(input("Enter first number: "))
    operation_type = input("Enter operation(- + * /): ")
    next_number = float(input("Enter next number: "))
    return first_number, operation_type, next_number

def calculator(first, operation, second):
    if operation == "-":
        return first - second
    elif operation == "+":
        return first + second
    elif operation == "*":
        return first * second
    elif operation == "/":
        return first / second

def default_calculation():
    first_number, operation_type, next_number = get_data()
    result = calculator(first_number, operation_type, next_number)
    print(result)

saved_calc = 0
