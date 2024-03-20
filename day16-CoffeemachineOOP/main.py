from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    item = input(f"what would you like to have?({menu.get_items()}):")
    if item == "report":
        money_machine.report()
        coffeemaker.report()
    elif item == "off":
        is_on = False
    else:
        drink = menu.find_drink(item)
        if coffeemaker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)



