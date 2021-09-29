
class ArchivedCart:

    def __init__(self):
        self.content = []

    def get_content(self):
        return self.content

    def add_item(self, item):
        self.content.append(item)

    def remove_item(self, item):
        self.content.remove(item)
