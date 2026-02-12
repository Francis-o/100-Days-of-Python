from coffee_machine_data import MENU, RESOURCES
from coffe_machine_art import ART

def to_dollar(quarters, dimes, nickles, pennies):
    """
    This function converts given coin input and converts to dollar
    returns float to 2 decimal places
    """
    dollar_equiv = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies) 
    return round(dollar_equiv, 2)

def coin_machine(inventory, coffee_type, resources):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    amount = to_dollar(quarters, dimes, nickles, pennies)
    cost = inventory[coffee_type]["cost"] + resources["money"]
    #checks if the amount inputted is enough to buy coffee
    if amount >= cost:
        remainder = amount - cost
        return {"balance":cost, "remainder": remainder, "status": True, "message": "money check passed"} 
    else:
        return {"return_amount": amount, "status": False, "message": f"Sorry that's not enough money to make a {coffee_type}. ${amount} refunded."}

def resource_check(inventory, coffee_type, resources):
    #gets key name of needed ingredients and compare
    #availble resources in the resource dictionary
    updated_resources = resources
    required_resource = inventory[coffee_type]["ingredients"]
    for resource_type in required_resource:
        if resources[resource_type] >= required_resource[resource_type]:
            updated_resources[resource_type] = updated_resources[resource_type] - required_resource[resource_type]
        else:
            return {"status": False, "message": f"You do not have enough {resource_type} for {coffee_type}"}
    return {"updated_resources": updated_resources, "status": True, "message": f"resource check for {coffee_type} passed"}

def show_report(resources):
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${resources["money"]}")


def make_coffee():
    print(ART)
    inventory = MENU
    resources = RESOURCES
    turned_off = False
    while not turned_off:
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
        #exits loop if off in typed
        if coffee_type == "off":
            turned_off == True
            return
        #checks if user inputted valid coffee type
        elif (coffee_type in inventory) and coffee_type != "money":
            coin_machine_data = coin_machine(inventory=inventory, coffee_type=coffee_type, resources=resources)
            resource_check_data = resource_check(inventory, coffee_type, resources)
            if coin_machine_data["status"] == True and resource_check_data["status"] == True:
                resources["money"] = coin_machine_data["balance"]
                print(f"Here is your {coffee_type}☕. Enjoy!")
                remainder = coin_machine_data["remainder"]
                if remainder >  0:
                    print(f"Here is your change of ${remainder:.2f}")
            elif coin_machine_data["status"] == False:
                print(coin_machine_data["message"])
                return
            elif resource_check_data["status"] == False:
                print(resource_check_data["message"])
                return
        elif coffee_type == "report":
            show_report(resources) 
        else:
            print("You entered an invalid coffee type")
        order_again = input("Would you like to order again? 'y' or 'n': ").lower()
        if order_again == 'y':
            continue
        else:
            return


make_coffee()
