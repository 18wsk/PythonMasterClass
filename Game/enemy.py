import random
# Inheritance creates a "is a" relationship ==> child class is a type of the parent class ==> vampire is an enemy


class Enemy(object):    # parent class Enemy
    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage     # local variable
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self._hit_points))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} lost a life".format(self))
            else:
                print("{0._name} Is Dead".format(self))
                self._alive = False

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)
        # returning the attributes of the enemy to not have to rewrite long print statements to check if they good


class Troll(Enemy):     # troll inherits properties from enemy
    def __init__(self, name, colour="Green"):
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)       # same thing as below
        super(Troll, self).__init__(name=name, lives=1, hit_points=23)  # MUST use super for multiple inheritance
        self._colour = colour

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}, Colour: {0._colour}".format(self)

    def grunt(self):
        print("Me {0._name}. {0._name} stomp you".format(self))


class Vampire(Enemy):
    def __init__(self, name):
        super(Vampire, self).__init__(name=name, lives=3, hit_points=12)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("**** {0._name} dodges ****".format(self))
            return True
        else:
            return False

    # Overriding --> Python cannot do overloading
    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)  # THIS CALLS THE PARENT take_damage method


class VampireKing(Vampire):
    def __init__(self, name):
        super().__init__(name)  # super() same as super(VampireKing, self)
        self._hit_points = 140  # hitpoints are 140

    def take_damage(self, damage):
        super().take_damage(damage//4)  # takes 1/4 the damage



