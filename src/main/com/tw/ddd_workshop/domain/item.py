
class Item:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def __str__(self):
        return "%s: %s" % (self.product, self.quantity)

