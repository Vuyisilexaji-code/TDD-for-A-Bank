import unittest


class TestBankAccount(unittest.TestCase):

    def test_deposit(self):
        account = BankAccount()
        account.deposit(100)
        self.assertEqual(account.get_balance(), 100)

    def test_withdraw(self):
        account = BankAccount()
        account.deposit(100)
        account.withdraw(50)
        self.assertEqual(account.get_balance(), 50)

    def test_insufficient_balance(self):
        account = BankAccount()
        account.deposit(50)
        with self.assertRaises(ValueError):
            account.withdraw(100)


if __name__ == "__main__":
    unittest.main()