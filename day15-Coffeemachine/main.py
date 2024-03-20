MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money": 0,
}


def resource_reduction(coffee_choice):
    resources['water'] = resources['water'] - MENU[coffee_choice]['ingredients']['water']
    if coffee_choice != 'espresso':
        resources['milk'] = resources['milk'] - MENU[coffee_choice]['ingredients']['milk']
    resources['coffee'] = resources['coffee'] - MENU[coffee_choice]['ingredients']['coffee']
    resources['Money'] = resources['Money'] + MENU[coffee_choice]['cost']
    return True


def is_resource_sufficient(drink):
    for item in drink:
        if drink[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def process_coins():
    print('Please insert coins.')
    total_cost = int(input('How many quarters?:')) * 0.25
    total_cost += int(input('How many dimes?:')) * 0.10
    total_cost += int(input('How many nickles?:')) * 0.05
    total_cost += int(input('How many pennies?:')) * 0.01
    return total_cost


def is_transaction_success(coffee_cost, total_cost):
    if total_cost < coffee_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        remaining = total_cost - coffee_cost
        remaining_cost = round(remaining, 2)
        print(f"Here is ${remaining_cost} dollars in change.")
        return True


def coffee_machine():
    is_true = True
    while is_true:
        coffee_choice = input("What would you like? (espresso/latte/cappuccino):")
        if coffee_choice == 'report':
            print(
                f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['milk']}g\nMoney: ${resources['Money']}")
        elif coffee_choice == 'off':
            return
        else:
            drink = MENU[coffee_choice]
            if is_resource_sufficient(drink['ingredients']):
                total_cost = process_coins()
                if is_transaction_success(drink['cost'], total_cost):
                    if resource_reduction(coffee_choice):
                        print(f'Here is your {coffee_choice}. Enjoy!')


coffee_machine()
