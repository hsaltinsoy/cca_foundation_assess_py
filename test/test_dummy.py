import unittest
from src.product import Product
from src.warehouse import Entry, Warehouse
from src.address import Address
from src.order import Order, Item


class DummyTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def setUp(self):
        self.product1 = Product(id=1, description="Product1", price=10.99)
        self.product2 = Product(id=2, description="Product2", price=20.99)
        self.address = Address(house="10", street="Baker", city="London", postcode="NW3 5AS", country="Albania")
        self.order = Order(shipping_address=self.address, items=[])
        self.warehouse = Warehouse([
            Entry(self.product1, 20),
            Entry(self.product2, 30)
        ])

    def test_check_stock_existing_product(self):
        self.assertEqual(self.warehouse.check_stock(self.product1), 20)
        self.assertEqual(self.warehouse.check_stock(self.product2), 30)

    def test_check_stock_non_existing_product(self):
        non_existing_product = Product(id=3, description="NonExistingProduct", price=5.99)
        self.assertEqual(self.warehouse.check_stock(non_existing_product), 0)

    def test_check_stock_empty_warehouse(self):
        empty_warehouse = Warehouse([])
        self.assertEqual(empty_warehouse.check_stock(self.product1), 0)

    def test_adjust_stock_when_stock_bigger(self):
        self.warehouse.adjust_stock(self.product1, 10)
        self.assertEqual(self.warehouse.check_stock(self.product1), 10)

    def test_adjust_stock_when_stock_and_qua_equal(self):
        self.warehouse.adjust_stock(self.product1, 20)
        self.assertEqual(self.warehouse.check_stock(self.product1), 0)

    def test_adjust_stock_when_stock_lower(self):
        self.warehouse.adjust_stock(self.product1, 30)
        self.assertEqual(self.warehouse.check_stock(self.product1), 20)

    def test_receive_stock_for_existing_prod(self):
        self.warehouse.receive_stock(self.product1, 10)
        self.assertEqual(self.warehouse.check_stock(self.product1), 30)

    def test_receive_stock_for_non_existing_prod(self):
        non_existing_product = Product(id=3, description="NonExistingProduct", price=5.99)
        self.warehouse.receive_stock(non_existing_product, 30)
        self.assertEqual(self.warehouse.check_stock(non_existing_product), 30)

    def test_add_item_to_order_when_quantity_enough(self):
        item = Item(product=self.product1, quantity=10)
        self.order.add_item(item=item, wh=self.warehouse)
        self.assertEqual(self.warehouse.check_stock(self.product1), 10)

    def test_add_item_to_order_when_quantity_bigger(self):
        item = Item(product=self.product1, quantity=30)
        self.order.add_item(item=item, wh=self.warehouse)
        self.assertEqual(self.warehouse.check_stock(self.product1), 20)

    def test_add_item_to_order_when_quantity_equal(self):
        item = Item(product=self.product1, quantity=20)
        self.order.add_item(item=item, wh=self.warehouse)
        self.assertEqual(self.warehouse.check_stock(self.product1), 0)


if __name__ == '__main__':
    unittest.main()
