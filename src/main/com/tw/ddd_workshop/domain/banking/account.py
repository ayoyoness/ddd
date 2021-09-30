import uuid


class Account:

    def __init__(self, account_type, address):
        self.id = uuid.uuid4()
        self.address = address
        self.account_type = account_type

    def get_address(self):
        return self.address

    def update_address(self, new_address):
        self.address = new_address
