from typing import List
from dataclasses import dataclass
from src.product import Product


@dataclass
class Entry:
    product: Product
    stock: int


@dataclass
class Warehouse:
    catalogue: List[Entry]

    def check_stock(self, product: Product) -> int:
        for prod in self.catalogue:
            if prod.product == product:
                return prod.stock
        return 0

    def adjust_stock(self, product: Product, quantity: int) -> None:
        for prod in self.catalogue:
            if prod.product == product:
                if prod.stock >= quantity:
                    prod.stock = prod.stock - quantity
                else:
                    return "There is not enough stock for this product!"
        return None

