import uuid


class ShoppingCart:

    def __init__(self):
        self.id = uuid.uuid4()
        self.items = []
        self.removed_items = []

    def get_items(self):
        return self.items

    def get_removed_items(self):
        return self.removed_items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.removed_items.append(item)
        self.items.remove(item)

    def __eq__(self, some_object):
        return type(some_object).__instancecheck__(ShoppingCart) and some_object.__getattribute__("id") == self.id
