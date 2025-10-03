from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    match choice:
        case "report":
            coffee_maker.report()
            money_machine.report()
            continue
        case "off":
            is_on = False
            continue
    if not menu.find_drink(choice):
        continue
    if coffee_maker.is_resource_sufficient(menu.find_drink(choice)):
        money_machine.make_payment(menu.find_drink(choice).cost)
        coffee_maker.make_coffee(menu.find_drink(choice))

