# up till now == imperative style
# imperative == providing a series of instructions for a pc to follow in a defined order

class Kettle(object):
    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("KenWood", 8.99)
print(kenwood)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.50)
print(hamilton.make)
print(hamilton.price)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""""
# Class: template for creating objects. All objects created using the same class will have the same characteristics
# Object: an instance of a class
# Instantiate: create an instance of a class
# Method: a function defined in a class
# Attribute: a variable bound to an instance of a class

# instances == another name for an object made from class definition
"""

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)
print()
# passing instance kenwood as self attribute for method switched_on() of class Kettle
print(kenwood.on)
Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

print("*" * 40)

# creating a data attribute for kenwood instance
kenwood.power = 1.5
print(kenwood.power)

print("Switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)
print(hamilton.power_source)

print("Switch kenwood to gas")
kenwood.power_source = "gas"
print(kenwood.power_source)


print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
