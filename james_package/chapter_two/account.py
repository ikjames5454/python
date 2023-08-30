class Account:



    def __init__(self,account_number, account_name, pin):
        self.__account_number = account_number
        self.__account_name = account_name
        self.__pin = pin
        self.__balance = 0


    def i_can_deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("amount to be deposited must be greater than zero")



    def check_balance(self,pin):
        if self.__pin == pin:
            return self.__balance
        else:
            raise ValueError("wrong pin")



    def i_can_withdraw(self, amount,pin):
        if amount > 0:
            if self.check_balance(pin):
                if amount < self.__balance:
                    self.__balance -= amount
                else:
                    raise ValueError("return insufficient fund")
            else:
                raise ValueError("wrong pin input")
        else:
            raise ValueError("amount must not be a negative value")

    def i_can_change_pin(self, old_pin, new_pin):
        if self.__pin == old_pin:
            self.__pin = new_pin
            return self.__pin

