import art
# add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(art.logo)
    # get the first number
    num1 = float(input("What's the first number?: "))
    # display the operations available
    for symbol in operations:
        print(symbol)

    use_calc = True

    while use_calc:
        # prompt user to pick an operation
        operation_symbol = input("Pick an operation: ")
        # get the next number
        num2 = float(input("What's the next number?: "))
        # find the user choice as key in dictionary
        calculation_function = operations[operation_symbol]
        # use the value which is a function on the two numbers and store in answer
        answer = calculation_function(num1, num2)

        # format and display the output
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # see if user wants to continue:
        more_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' "
                          f"to start a new calculation. or type q to quit: ").lower()
        # if user chose to quit - exit loop
        if more_calc == 'n':
            use_calc = False
            calculator()
        # if user wants to quit program
        elif more_calc == 'q':
            break
        # other-wise update num1 with the current answer to continue operations
        else:
            num1 = answer


calculator()