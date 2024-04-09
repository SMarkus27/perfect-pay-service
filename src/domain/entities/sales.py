from dataclasses import dataclass


@dataclass
class Sales:
    product: int
    sales_date: str
    quantity: int
    discount: float
    status: bool
    client: int

    def __post_init__(self):
        Sales.verify_product(self.product)
        Sales.verify_quantity(self.quantity)
        Sales.verify_discount(self.discount)
        Sales.verify_status(self.status)
        Sales.verify_client(self.client)

    @staticmethod
    def verify_product(product: int) -> int:
        if product <= 0:
            raise Exception("Product must be greater than or equal to 1")
        return product

    @staticmethod
    def verify_quantity(quantity: int) -> int:
        if quantity <= 0:
            raise Exception("Quantity must be greater than or equal to 1")
        return quantity

    @staticmethod
    def verify_discount(discount: float) -> float:
        if discount < 0:
            raise Exception("Discount must be greater than 0")
        return discount

    @staticmethod
    def verify_status(status: bool) -> bool:
        if type(status) is not bool:
            raise Exception("Status must be greater a boolean")
        return status

    @staticmethod
    def verify_client(client: int) -> int:
        if client <= 0:
            raise Exception("Client must be greater than or equal to 1")
        return client
