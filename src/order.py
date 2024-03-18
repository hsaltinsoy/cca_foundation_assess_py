from typing import List
from dataclasses import dataclass

from src.address import Address
from src.product import Product
from src.warehouse import Warehouse


@dataclass
class Item:
    product: Product
    quantity: int


@dataclass
class Order:
    shipping_address: Address
    items: List[Item]

    def add_item(self, item: Item, wh: Warehouse):
        stock = wh.check_stock(product=item.product)
        if stock >= item.quantity:
            self.items.append(item)
            wh.adjust_stock(item.product, item.quantity)
        else:
            return ValueError("There is not enough stock for this product!")





