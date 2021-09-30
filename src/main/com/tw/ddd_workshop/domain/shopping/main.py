from src.main.com.tw.ddd_workshop.domain.shopping.catalog import Catalog
from src.main.com.tw.ddd_workshop.domain.shopping.price import Price
from src.main.com.tw.ddd_workshop.domain.shopping.shopping_cart import ShoppingCart


def run():

    competitor_products = {
        "ipad pro": Price(10),
        "Hero ink Pen": Price(16),
        "Reebok Cricket bat": Price(19),
    }

    catalog = Catalog()
    catalog.add_products(competitor_products)
    catalog.process_discount()

    cart = ShoppingCart()
    # add these from catalog
    cart.add_item(ipad_pro)

    cart.add_item(ink_pen)

    cart.add_item(cricket_bats)

    cart.remove_item(ink_pen)

    print("we got this in our cart: ", cart.get_items())


if __name__ == '__main__':
    run()
