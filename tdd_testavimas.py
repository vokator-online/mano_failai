import unittest
from gui_loan import loan

class TestLoanCalculator(unittest.TestCase):
    def test_loan_payment(self):
        principal = 1000
        interest_rate = 0.05
        months = 12
        result = test_loan_payment(principal, interest_rate, months)
        self.assertEqual(result, 1051.16)

if __name__ == '__main__':
    unittest.main()