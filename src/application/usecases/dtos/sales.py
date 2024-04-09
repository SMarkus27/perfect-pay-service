from typing_extensions import TypedDict


class SalesDto(TypedDict):
    product: int
    sales_date: str
    quantity: int
    discount: float
    status: bool
