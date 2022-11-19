import tkinter


def add(*nums_to_be_summed):
    total = 0
    for n in nums_to_be_summed:
        total += n
    print(nums_to_be_summed)
    return total


print(add(1, 4, 8, 10, 3, -4))

# def calculate(**kwargs):

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.seats = kw.get("seats")
        self.color = kw.get("color")

my_car = Car(make="Nissan")
print(my_car.model)