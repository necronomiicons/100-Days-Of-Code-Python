espresso = {
    "price": 1.50,
    "water" : 50,
    "coffee" : 18,
    "milk" : 0
}

latte = {
    "price" : 2.50,
    "water" : 200,
    "coffee" : 24,
    "milk" : 150,
}

cappuccino = {
    "price" : 3.00,
    "water" : 250,
    "coffee" : 24,
    "milk" : 100,
}

resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
    "money" : 0
}

payment = {
    "quarters" : 0,
    "dimes" : 0,
    "nickels" : 0,
    "pennies" : 0,
}

def total(p):
    return (p["quarters"] * .25) + (p["dimes"] * .1) + (p["nickels"]*.05) + (p["pennies"] * .01)

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def calculate_payment():
    payment["quarters"] = int(input("How many quarters?: "))
    payment["dimes"] = int(input("How many dimes?: "))
    payment["nickels"] = int(input("How many nickles?: "))
    payment["pennies"] = int(input("How many pennies?: "))

def check_resources(drink):
    if resources['water'] < drink['water']:
        return "Water"
    if resources['coffee'] < drink['coffee']:
        return "Coffee"
    if resources['milk'] < drink['milk']:
        return "Milk"
    return ""

def buy_drink(drink, p):
    if total(p) < drink['price']:
        return False
    resources["water"] -= drink["water"]
    resources["coffee"] -= drink["coffee"]
    resources["milk"] -= drink["milk"]
    change = total(p) - drink["price"]
    resources['money'] += drink['price']
    if change > 0:
        print(f"Here is ${round(change,2)} in change.")
    return True

def make_selection():
    selection = str(input("What would you like? (espresso/latte/cappuccino): "))
    drink = espresso
    match selection:
        case "report":
            print_report()
            return
        case "latte":
            drink = latte
        case "cappuccino":
            drink = cappuccino
    if check_resources(drink) == "":
        calculate_payment()
        if buy_drink(drink, payment):
            print(f"Here is your {selection}. Enjoy!")
        else:
            print(f"Insufficient funds.")
    else:
        print(f"Insufficient {check_resources(drink)}")


while True:
    make_selection()