#Calculator
import art

print(art.calculator)
continue_calculation = 'n'
result: int = 0
def add(a, b):
    print(f"{a} + {b} = {a + b}")
    return a + b

def subtract(a, b):
    print(f"{a} - {b} = {a - b}")
    return a - b

def multiply(a, b):
    print(f"{a} * {b} = {a * b}")
    return a * b

def divide(a, b):
    print(f"{a} / {b} = {a / b}")
    return a / b

def determine_output(a, b, o):
    match o:
        case "+":
            return add(a, b)
        case "-":
            return subtract(a, b)
        case "*":
            return multiply(a, b)
        case "/":
            return divide(a, b)



while True:
    if continue_calculation == 'n':
        num_1 = int(input("What's the first number?"))
    else:
        num_1 = result
    num_2 = int(input("What's the second number?"))
    operation = str(input("What's the operation? \n+\n-\n*\n/\n"))
    result = determine_output(num_1, num_2, operation)
    continue_calculation = input(f"Type 'y' to continue working with {result}, or type 'n' to start a new calculation.")


