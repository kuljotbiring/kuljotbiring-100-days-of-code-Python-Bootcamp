def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key, value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


# using get with kwargs makes the arguments optional
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", model="GTR")
print(my_car.make)
