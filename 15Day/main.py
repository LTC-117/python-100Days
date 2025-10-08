from menu import MENU, resources


user_input = ""
money: float = 0.0


def cash_register(order):
    print("Please, insert coins.")
    result = 0

    try:
        quarters = float(input("how many quarters?: ")) * 0.25
        dimes = float(input("how many dimes?: ")) * 0.10
        nickles = float(input("how many nickles?: ")) * 0.05
        pennies = float(input("how many pennies?: ")) * 0.01
        result = (quarters) + (dimes) + (nickles) + (pennies)
    except ValueError:
        print("Error: Invalid value! Input must be a numeric value! Try again!")

    return result


def coffee_machine(order, cash: float):
    if order not in MENU:
        print("Error: Invalid order! Try again!")
        return
    
    for item in MENU[order]['ingredients']:
        if MENU[order]['ingredients'][item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return

    user_cash = cash_register(order)
    change = round(user_cash - MENU[order]["cost"], 2)

    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
        return

    for item in MENU[order]['ingredients']:
        resources[item] -= MENU[order]['ingredients'][item]

    global money

    money += MENU[order]["cost"]
    print(f"Here is your ${change} in change.")
    print("Here is your latte ☕️. Enjoy!")


while 1:
    user_input = input("What would you like? (espresso/latte/capuccino): ")

    match user_input:
        case "off":
            exit(0)
        case "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")
        case _:
            coffee_machine(user_input, money)



