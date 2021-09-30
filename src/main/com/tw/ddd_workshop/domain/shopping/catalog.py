from src.main.com.tw.ddd_workshop.domain.shopping.product import Product


# separate cclas
def discount(price):
    return price * 0.9


class Catalog:

    def __init__(self):
        self.products = []

    def add_products(self, competitor_products):
        self.products = [Product(name, price) for name, price in competitor_products.items()]

    def process_discount(self):
        self.products = [Product(name, discount(price)) for name, price in self.products]

