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
    "money": 0,
}


# print items in resources dictionary
def report(resources_left):
    for key, value in resources_left.items():
        print(f"{key}: {value}")


# look at the item and the amount of its ingredients in MENU dict. Check if there are enough
# resources via resources dict. If any resource is lacking let the user know.
def sufficient(ingredients, item, drink):
    lack_of = ""
    # check if enough to make expresso
    if drink == "espresso":
        if item[drink]["ingredients"]["water"] > ingredients["water"]:
            lack_of = "water"
        if item[drink]["ingredients"]["coffee"] > ingredients["coffee"]:
            lack_of = "coffee"
    # check if enough to make latte
    elif drink == "latte":
        if item[drink]["ingredients"]["water"] > ingredients["water"]:
            lack_of = "water"
        if item[drink]["ingredients"]["milk"] > ingredients["milk"]:
            lack_of = "milk"
        if item[drink]["ingredients"]["coffee"] > ingredients["coffee"]:
            lack_of = "coffee"
    # check if enough to make cappuccino
    elif drink == "cappuccino":
        if item[drink]["ingredients"]["water"] > ingredients["water"]:
            lack_of = "water"
        if item[drink]["ingredients"]["milk"] > ingredients["milk"]:
            lack_of = "milk"
        if item[drink]["ingredients"]["coffee"] > ingredients["coffee"]:
            lack_of = "coffee"

    # show the ingredient lacking and return T/F if sufficient resources
    if lack_of == "":
        return True
    else:
        print(f"Sorry there is not enough {lack_of}")
        return False


# get the change from the user by looking up the cost in the MENU dict based on user drink choice
def get_money(menu, selection, supply):
    # get the cost of the item selected
    price = menu[selection]["cost"]
    funds = 0
    while price > funds:
        # prompt user to enter money in coins
        print("Please insert coins")
        quarters = float(input("How many quarters? :"))
        dimes = float(input("How many dimes? :"))
        nickels = float(input("How many nickels? :"))
        pennies = float(input("How many pennies? :"))
        # calculate the total money use entered into the machine
        funds = ((quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01))
        # if user  didn't enter enough money repeat loop and return the change
        if price > funds:
            print(f"You did not enter enough change. Retry. Change returned: ${funds}")

    # calculate the change due if they added enough money
    change_due = round(funds - price, 2)
    # add the money count to the machine
    supply["money"] += price
    if change_due > 0:
        print(f"Here is ${change_due} in change.")


def make_drink(supply, beverage, order):
    # check the drink and subtract from resources the ingredient cost of the drink
    if beverage == "espresso":
        supply["water"] -= order[beverage]["ingredients"]["water"]
        supply["coffee"] -= order[beverage]["ingredients"]["coffee"]
    elif beverage == "latte":
        supply["water"] -= order[beverage]["ingredients"]["water"]
        supply["milk"] -= order[beverage]["ingredients"]["milk"]
        supply["coffee"] -= order[beverage]["ingredients"]["coffee"]
    elif beverage == "cappuccino":
        supply["water"] -= order[beverage]["ingredients"]["water"]
        supply["milk"] -= order[beverage]["ingredients"]["milk"]
        supply["coffee"] -= order[beverage]["ingredients"]["coffee"]


def run_machine():
    make_coffee = True

    while make_coffee:
        # get the user selected drink
        drink_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        # if off is chosen machine turned off - exit program
        if drink_choice == "off":
            make_coffee = False
        # if report is chosen - show remaining machine resources
        elif drink_choice == "report":
            report(resources)
        # other-wise they picked a drink
        else:
            # check if enough resources to make chosen drink
            has_resources = sufficient(resources, MENU, drink_choice)
            # if enough resources
            if has_resources:
                # collect the money
                get_money(MENU, drink_choice, resources)
                # subtract the used resources
                make_drink(resources, drink_choice, MENU)
                # display message for drink served
                print(f"Here is your {drink_choice} ☕")


run_machine()
