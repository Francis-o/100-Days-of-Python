import my_calculator_ascii

"""
Basic calculator, performs addition, subtraction, multiplication and division
"""

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def calculator():
    print(my_calculator_ascii.calc_ui)
    operations = {"+": add, "-": sub, "*": mult, "/": div}
    result = 0
    first_num = float(input("What's the first number?: "))

    close_calulator = False

    while not close_calulator:
        for key in operations:
            print(key)
        operation = input("Pick an operation: ")
        second_num = float(input("What's the next number?: "))
        result = operations[operation](first_num, second_num)
        print(f"{first_num:.1f} {operation} {second_num:.1f} = {result:.1f}")
        game_status = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation: ")
        if game_status == 'y':
            first_num = result
        elif game_status == 'n':
            print("\n" * 30)
            calculator()
        else:
            print("Exiting calculator...")
            return
 
calculator()
