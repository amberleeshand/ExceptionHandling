import random

# print(random.randint(100, 999))

class InsufficientFundsError(Exception):
    def init(self, msg):
        super().__init__(msg)

class CannotDepositNegativeAmountError(Exception):
    def init(self, msg):
        super().__init__(msg)


class InvalidUserInputError(Exception):
    def init(self, msg):
        super().__init__(msg)


class Account:

    def __init__(self, firstname, surname, age, balance=0):
        self._firstname = firstname
        self._surname = surname
        self._name = f"{self._firstname} {self._surname}"
        self._age = age
        self._balance = balance

    @property
    def generate_onetime_passcode(self):
        return f"{self._firstname[0]}{random.randint(100,999)}"


    def deposit(self, amount):
        try:
            if amount < 0:
                raise CannotDepositNegativeAmountError("Cannot deposit negative amount")
            else:
                self._balance += amount
                return f"Your new balance is: £{self._balance}"
        except CannotDepositNegativeAmountError:
            return "Cannot deposit negative amount"



    def withdraw(self, amount):
        try:
            if self._balance < amount:
                raise InsufficientFundsError("Insufficient Funds")
            else:
                self._balance -= amount
        except InsufficientFundsError:
            return "Insufficient Funds"

        try:
            if amount < 0:
                raise CannotDepositNegativeAmountError("Cannot Deposit Negative Amount")
            else:
                return f"Funds remaining: £{self._balance}"
        except CannotDepositNegativeAmountError:
            return "Cannot Deposit Negative Amount"


    def getbalance(self):
        return f"£{self._balance}"

    def user_input(self):
        user_input = int(
            input("What do you want to do today? Please select 1 for withdraw, 2 for deposit, or 3 to view your "
                  "balance: "))
        try:
            if user_input == 1:
                withdraw_amount = int(input("Please enter the amount you wish to withdraw: "))
                return self.withdraw(withdraw_amount)
            elif user_input == 2:
                deposit_amount = int(input("Please enter the amount you wish to deposit: "))
                return self.deposit(deposit_amount)
            elif user_input == 3:
                return self.getbalance()
            else:
                raise InvalidUserInputError("Not a valid user input")
        except InvalidUserInputError:
            return "Not a valid user input"