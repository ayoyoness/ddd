import unittest

from src.main.com.tw.ddd_workshop.domain.banking.account import Account
from src.main.com.tw.ddd_workshop.domain.banking.address import Address
from src.main.com.tw.ddd_workshop.domain.banking.customer import Customer


class TestCart(unittest.TestCase):

    def test_should_update_address_in_acccounts_when_customer_address_updated(self):
        address = Address("berlin")
        current_account = Account("Current", address)
        savings_account = Account("Savings", address)
        accounts = [current_account, savings_account]

        customer = Customer(accounts, address)

        new_address = Address("london")
        customer.update_address(new_address)

        self.assertEqual(customer.get_address(), new_address)
        self.assertEqual(current_account.get_address(), new_address)
        self.assertEqual(savings_account.get_address(), new_address)


if __name__ == '__main__':
    unittest.main()
