import uuid


class Customer:

    def __init__(self, accounts, address):
        self.id = uuid.uuid4()
        self.accounts = accounts
        self.address = address

    def get_address(self):
        return self.address

    def update_address(self, new_address):
        self.address = new_address
        for account in self.accounts:
            account.update_address(new_address)
