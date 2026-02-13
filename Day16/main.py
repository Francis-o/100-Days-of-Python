from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_menu = Menu()
my_money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

turned_off = False

while not turned_off:
    available_drinks = my_menu.get_items()
    choice = input(f"What would you like? ({available_drinks}): ")
    drink = my_menu.find_drink(choice)
    if choice == "off":
        turned_off = True
    elif choice in available_drinks:
        if coffee_maker.is_resource_sufficient(drink=drink) and my_money_machine.make_payment(cost=drink.cost):
            coffee_maker.make_coffee(drink)
    elif choice == "report":
        coffee_maker.report()
        my_money_machine.report()
    else:
        print("You entered an incorrect value!")


