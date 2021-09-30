from src.main.com.tw.ddd_workshop.domain.price import Price


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = Price(price)

    def get_name(self):
        return self.name

    def __str__(self):
        return "Product: {}".format(self.name)

    def __eq__(self, some_object):
        return type(some_object).__instancecheck__(Product) and some_object.__getattribute__("name") == self.name
