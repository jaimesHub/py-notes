class OnlineShop:
    """THis class doesn't have a great cohesion
    because almost all methods use only one of the 3 properties
    """
    def __init__(self) -> None:
        self._order = ''
        self._offered_productions = ''
        self._customers = ''

    def add_product(self, title: str, price: int):
        """offeredProducts"""
        pass

    def update_product(self, product_id: str, title: str, price: int):
        """offeredProducts"""
        pass

    def remove_product(self, product_id: str):
        """offeredProducts"""
        pass

    def get_available_items(self, product_id: str):
        """offeredProducts"""
        pass

    def restock_product(self, product_id: str):
        """offeredProducts"""
        pass

    def create_customer(self, email: str, password: str):
        """customers"""
        pass

    def login_customer(self, email: str, password: str):
        """customers"""
        pass

    def makePurchase(self, customer_id: str, product_id: str):
        """customers, orders, offeredProducts"""
        pass

    def addOrder(self, customer_id: str, product_id: str, quantity: int):
        """customers, orders, offeredProducts"""
        pass

    def refund(self, orderId: str):
        """customers, orders"""
        pass

    def update_customer_profile(self, customer_id: str, name: str):
        """customers"""
        pass

    # ...