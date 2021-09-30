import unittest

from src.main.com.tw.ddd_workshop.domain.shopping.item import Item
from src.main.com.tw.ddd_workshop.domain.shopping.price import Price
from src.main.com.tw.ddd_workshop.domain.shopping.shopping_cart import ShoppingCart
from src.main.com.tw.ddd_workshop.domain.shopping.product import Product


class TestCart(unittest.TestCase):

    def test_should_add_product_with_default_quantity(self):
        cart = ShoppingCart()
        ipad_pro = Item(Product("ipad pro", Price(1)), 1)
        cart.add_item(ipad_pro)
        self.assertEqual(cart.get_items(), [ipad_pro])

    def test_should_add_product_with_specified_quantity(self):
        cart = ShoppingCart()
        cricket_bats = Item(Product("Reebok Cricket bat", Price(1)))
        cart.add_item(cricket_bats)
        self.assertEqual(cart.get_items(), [cricket_bats])

    def test_should_remove_item(self):
        cart = ShoppingCart()

        ipad_pro = Product("ipad pro", Price(1))
        ipad_pro_item = Item(ipad_pro, 1)
        cart.add_item(ipad_pro_item)

        cricket_bats = Product("Reebok Cricket bat", Price(1))
        cricket_bats_item = Item(cricket_bats, 2)
        cart.add_item(cricket_bats_item)

        self.assertEqual(cart.get_items(), [ipad_pro_item, cricket_bats_item])

        cart.remove_item(ipad_pro_item)

        self.assertEqual(cart.get_items(), [cricket_bats_item])

    def test_should_show_removed_items(self):
        cart = ShoppingCart()

        ipad_pro_item = Item(Product("ipad pro", Price(1)))
        cart.add_item(ipad_pro_item)

        cricket_bats_item = Item(Product("Reebok Cricket bat", Price(1)))
        cart.add_item(cricket_bats_item)

        cart.remove_item(ipad_pro_item)

        self.assertEqual(cart.get_removed_items(), [ipad_pro_item])

    def test_differentiate_carts_with_the_same_items(self):
        cart1 = ShoppingCart()
        ipad_pro_item = Item(Product("ipad pro", Price(1)))
        cart1.add_item(ipad_pro_item)

        cart2 = ShoppingCart()
        ipad_pro_item = Item(Product("ipad pro", Price(1)))
        cart2.add_item(ipad_pro_item)

        self.assertNotEqual(cart1, cart2)


if __name__ == '__main__':
    unittest.main()
