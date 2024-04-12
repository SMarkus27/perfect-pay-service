from dataclasses import dataclass


@dataclass
class Product:
    name: str
    description: str
    price: float

    def __post_init__(self):
        Product.verify_name(self.name)
        Product.verify_price(self.price)
        Product.verify_description(self.description)

    @staticmethod
    def verify_name(name: str) -> str:
        if len(name) <= 4:
            raise Exception("Name must be greater than 4 characters")
        return name

    @staticmethod
    def verify_description(description: str) -> str:
        if len(description) <= 4:
            raise Exception("Description must be greater than 4 characters")
        return description

    @staticmethod
    def verify_price(price: float) -> float:
        if price <= 0:
            raise Exception("Price must be greater than 0")
        return price
