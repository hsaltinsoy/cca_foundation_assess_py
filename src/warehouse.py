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

