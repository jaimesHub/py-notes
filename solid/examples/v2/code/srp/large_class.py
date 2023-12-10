class OnlineShop:
    """This class has multiple responsibilities
    As defined the SRP, which is not talking about 
    whether a class might be doing work on both a product and a customer
    Instead, in the context of this principle, it is actually meant to refer to different business areas, 
    this code might be related to 
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

    def make_purchase(self, customer_id: str, product_id: str):
        """customers, orders, offeredProducts"""
        pass

    def add_order(self, customer_id: str, product_id: str, quantity: int):
        """customers, orders, offeredProducts"""
        pass

    def refund(self, orderId: str):
        """customers, orders"""
        pass

    def update_customer_profile(self, customer_id: str, name: str):
        """customers"""
        pass

    # ...