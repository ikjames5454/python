import unittest
from account import Account


class TestAccount(unittest.TestCase):

    def test_that_account_exist(self):
        self.accounts = Account("1234", "james", "1237")
        self.assertTrue(self.accounts)


    def test_i_can_deposit(self):
        self.accounts = Account("1234", "james", "1237")
        self.accounts.i_can_deposit(0)
        self.assertEquals(0, self.accounts.check_balance("1237"))
        self.accounts.i_can_deposit(500)
        self.assertEquals(500, self.accounts.check_balance("1237"))
        self.accounts.i_can_deposit(-60)
        self.assertEquals(500, self.accounts.check_balance("1237"))


    def test_i_can_withdraw(self):
        self.accounts = Account("1234", "james", "1237")
        self.accounts.i_can_deposit(5000)
        self.assertEquals(5000, self.accounts.check_balance("1237"))
        self.accounts.i_can_withdraw(3000)
        self.assertEquals(2000, self.accounts.check_balance("1237"))

    def test_i_can_validate(self):
        self.accounts = Account("1234", "james", "1237")
        self.accounts.i_can_deposit(6000)
        self.assertEquals(6000, self.accounts.check_balance("1238"))


    def test_that_i_can_change_pin(self):
        self.accounts = Account("1234", "james", "1237")
        self.accounts.i_can_deposit(6000)
        self.assertEquals(6000, self.accounts.check_balance("1237"))
        self.accounts.i_can_withdraw(3000,"1237")
        self.accounts.i_can_change_pin("1237","3456")
        self.assertEquals(300,self.accounts.check_balance("3456"))




