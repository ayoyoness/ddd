
class Product:

    def __init__(self, name):
        self.name = name
        self.quantity = 1

    def get_name(self):
        return self.name

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def __str__(self) -> str:
        return "Product: {}".format(self.name)
