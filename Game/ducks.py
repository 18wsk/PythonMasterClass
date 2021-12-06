# Python dynamic typing only cares what can be done with an object not what type it is
# "If it walks and talks like a duck it is a duck"

# Composition is a concept that models a has a relationship. It enables creating complex types by combining objects of
# other types. This means that a class Composite can contain an object of another class Component . This relationship
# means that a Composite has a Component .

class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Wee, this is fun")
        elif self.ratio == 1:
            print("this is hard work, but im flying")
        else:
            print("Ill just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, Waddle, Waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack Quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print("Waddle, waddle, I waddle to")

    def swim(self):
        print("Come on in, but its a bit chilly this far south")

    def quack(self):
        print("Are you have a laugh, Im a penguin")

    def aviate(self):
        print("I won the lottery and bought a learjet")


class Mallard(Duck):
    pass


class Flock(object):

    def __int__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        fly_method = getattr(duck, 'fly', None)
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError("Cannot add duck, are you sure it's not a " + str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                raise AttributeError("Testing Exception Handler in Migrate")    # TODO remove this before release
            except AttributeError as e:
                print("One Duck Down")
                problem = e
        if problem:
            raise problem


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
    # percy = Penguin()
    # test_duck(percy)    # test function takes percy in like a duck





