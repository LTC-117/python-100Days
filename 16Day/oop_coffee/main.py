from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


running = 1

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while running != 0:
    user_input = input(f"What would you like? ({coffee_menu.get_items()}): ")

    match user_input:
        case "off":
            running = 0
        case "report":
            coffee_maker.report()
            money_machine.report()
        case _:
            order = coffee_menu.find_drink(user_input)
            if(order != None and coffee_maker.is_resource_sufficient(order) == True):
                order_cost = coffee_menu.get_drink_cost(user_input)
                if(money_machine.make_payment(order_cost) == True):
                    coffee_maker.make_coffee(order)
