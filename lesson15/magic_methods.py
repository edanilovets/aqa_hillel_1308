class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.__transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.__transactions.append(f"Deposit ${amount}")
        else:
            raise ValueError("Amount can't be negative")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance...")
        self.balance -= amount
        self.__transactions.append(f"Withdraw ${amount}")

    def __str__(self):
        return f"Bank account of '{self.owner}' with balance ${self.balance}"

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"

    def __add__(self, other):
        if isinstance(other, BankAccount):
            return BankAccount(self.owner, self.balance + other.balance)
        raise TypeError("Can only add BankAccount object")

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.owner == other.owner and self.balance == other.balance
        return False

    def __gt__(self, other):
        if isinstance(other, BankAccount):
            return self.balance > other.balance
        return False

    def __len__(self):
        return len(self.__transactions)

    def __contains__(self, item):
        return item in self.__transactions

#################################################################
account1 = BankAccount(owner='Eugene', balance=100)
print(account1)
account_str = str(account1)
account_repr = repr(account1)

#################################################################
account1 = BankAccount(owner='Eugene', balance=100)
account2 = BankAccount(owner='Jane', balance=200)

# str + str
# int + int
account3 = account1 + account2  # account1.__add__(account2) == +
account3 += account1
print(account3)  # account3

account4 =  account2 + account1
print(account4)

#################################################################
# ==
account1 = BankAccount(owner='Eugene', balance=10000)
print(id(account1))
account2 = BankAccount(owner='Eugene', balance=1000)
print(id(account2))
print("Is equal:", account1 == account2)
#################################################################

# >=, >, <, <=
print("Is greater than:", account1 > account2)
#################################################################
account1 = BankAccount(owner='Eugene', balance=10000)
account1.deposit(200)
account1.deposit(200)
account1.deposit(200)
print("Length of transactions:", len(account1))
#################################################################
# in
account1.deposit(233)
print("Check transaction:", "Deposit $233" in account1)
#################################################################