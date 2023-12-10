from typing import List

class Order:
    def refund(self):
        pass

    def add(self, customer_id: str, product_id: str, quantity: int):
        pass

class Customer:
    def __init__(self) -> None:
        self._orders: List[Order] = []

    def login(self, email: str, password: str):
        pass

    def update_profile(self, customer_id: str, name: str):
        pass

    def make_purchase(self, customer_id: str, product_id: str):
        pass

class Product:
    def __init__(self) -> None:
        self._title = ""
        self._price = 0

    def add(self, title: str, price: int):
        pass

    def update(self, product_id: str, title: str, price: int):
        pass

    def remove(self, product_id: str):
        pass

    def get_available_items(self, product_id: str):
        pass

    def restock(self, product_id: str):
        pass
