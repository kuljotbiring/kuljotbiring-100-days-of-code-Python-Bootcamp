from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create objects for classes
menu = Menu()
make_drink = CoffeeMaker()
funds = MoneyMachine()


def make_coffee():
    run_machine = True

    while run_machine:
        drink_choice = input(f"What would you like? ({menu.get_items()}): ").lower()
        # if off is chosen machine turned off - exit program
        if drink_choice == "off":
            run_machine = False
        # print out machine reports if user wants report
        elif drink_choice == "report":
            make_drink.report()
            funds.report()
        else:
            # check if drink entered exist. other-wise re-prompt user
            find_drink = menu.find_drink(drink_choice)
            if find_drink is None:
                continue
            drink = ""
            # check what user entered and make set it to object to pass to MenuItem
            if drink_choice == "latte":
                drink = menu.menu[0]
            if drink_choice == "espresso":
                drink = menu.menu[1]
            if drink_choice == "cappuccino":
                drink = menu.menu[2]
            # call function to see if enough resources to make drink
            if make_drink.is_resource_sufficient(drink):
                # ask user for money and check if enough funds. will refund excess money
                if not funds.make_payment(drink.cost):
                    continue
                # if enough money was given make drink
                make_drink.make_coffee(drink)


# call function to run program
make_coffee()
