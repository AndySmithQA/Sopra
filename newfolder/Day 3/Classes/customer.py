from person import Person
class Customer(Person):
    _class_version = 4.56
    @classmethod
    def get_class_version(cls):
        return cls._class_version

    def __init__(self,name,initial):
        super().__init__(name)
        self._balance = initial
    def deposit(self,amt):
        self._balance += amt
        return f"You deposited £{amt} - new Balance = £{self._balance}"

    def withdraw(self,amt):
        if self._balance - amt < 0:
            print("you do not have the funds")
        else:
            return f"You Withdrew £{amt} - new Balance = £{self._balance}"

    def getbalance(self):
        return f"Your balance is £{self._balance}"

    def set_balance(self,newamt):
        self._balance = newamt
        return f"Your new balance is £{self._balance}"

cust1 = Customer("Jim",2000)

print(cust1.deposit(500))

print(cust1.getbalance())

print(cust1.withdraw(45000))

print(cust1.set_balance(8))

print(cust1.get_class_version())
