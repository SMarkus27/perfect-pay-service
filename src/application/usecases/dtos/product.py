from typing_extensions import TypedDict


class ProductDto(TypedDict):
    name: str
    description: str
    price: float
