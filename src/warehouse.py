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
        for entry in self.catalogue:
            if entry.product == product:
                return entry.stock
        return 0

    def adjust_stock(self, product: Product, quantity: int):
        for entry in self.catalogue:
            if entry.product == product:
                if entry.stock >= quantity:
                    entry.stock = entry.stock - quantity
                else:
                    return "There is not enough stock for this product!"
        return None

    def receive_stock(self, product: Product, quantity: int):
        for entry in self.catalogue:
            if entry.product == product:
                entry.stock += quantity
        else:
            self.catalogue.append(Entry(product, quantity))

