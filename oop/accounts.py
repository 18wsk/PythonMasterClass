import pytz
import datetime


class Account:
    """Simple class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transactions_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transactions_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            self.show_balance()
            self._transactions_list.append((Account._current_time(), -amount))
        else:
            print("Amount must be greater than 0 and less than your amount balance")
            self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transactions_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == "__main__":
    will = Account("Will", 0)
    will.show_balance()

    will.deposit(1000)
    will.withdraw(500)
    will.withdraw(2000)
    print()
    print(will.show_transactions())
    print("*"*40)
    steph = Account("Steph", 800)
    steph.__balance = 200
# Python mangles names of class attributes that start with __
# balance attribute in class is automatically mangled to _Account__balance
    steph.deposit(100)
    steph.withdraw(200)
    print()
    steph.show_transactions()
    steph.show_balance()
    print(steph.__dict__)

    steph._Account__balance = 40    # Accessing mangled attribute to actually change balance value
    steph.show_balance()
