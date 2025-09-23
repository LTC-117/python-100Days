import art

print(art.logo)

def calculate(first_number):
    print("+\n-\n*\n/")

    operation = input("Pick an operation: ")
    if operation not in ['+', '-', '*', '/']:
        operation = "undefined"

    second_number = float(input("What's the next number? "))

    match operation:
        case "+":
            result = float(first_number + second_number)
        case "-":
            result = float(first_number - second_number)
        case "*":
            result = float(first_number * second_number)
        case "/":
            result = float(first_number / second_number)
        case _:
            result = 0.0

    print(f"{first_number} {operation} {second_number} = {result}")

    user_result = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    if user_result == 'y':
        calculate(result)

while 1:
    first_number = float(input("What's the first number? "))

    calculate(first_number)
