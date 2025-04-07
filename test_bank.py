import unittest



class TestBankAccount(unittest.TestCase):
    
    def test_initial_balance(self):
        account = BankAccount()
        self.assertEqual(account.get_balance(), 0)

    def test_deposit(self):
        account = BankAccount()
        account.deposit(100)
        self.assertEqual(account.get_balance(), 100)

    def test_withdraw(self):
        account = BankAccount()
        account.deposit(200)
        account.withdraw(100)
        self.assertEqual(account.get_balance(), 100)

    def test_withdraw_more_than_balance(self):
        account = BankAccount()
        account.deposit(50)
        with self.assertRaises(ValueError):
            account.withdraw(100)

    def test_check_balance_after_multiple_transactions(self):
        account = BankAccount()
        account.deposit(200)
        account.withdraw(50)
        account.deposit(100)
        self.assertEqual(account.get_balance(), 250)

if __name__ == '__main__':
    unittest.main()
