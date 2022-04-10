"""
Prime numbers are numbers that can only be cleanly divided by themselves and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.
"""
# Write your code below this line 👇


def prime_checker(number):
    num_factors = 0
    for num in range(1, number + 1):
        if number % num == 0:
            num_factors += 1

    if num_factors == 2:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# Write your code above this line 👆

# Do NOT change any of the code below👇


n = int(input("Check this number: "))
prime_checker(number=n)