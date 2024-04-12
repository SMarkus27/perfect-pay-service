from src.application.usecases.dtos.sales import SalesDto
from src.controllers.sales import SalesController
from src.infra.web.http.base import BaseAPIRouter

router = BaseAPIRouter.get_instance()


@router.post("/sales/", tags=["sales"])
async def create_product(sales: SalesDto):
    return await SalesController.create(sales)


@router.get("/sales/", tags=["sales"])
async def find_all_sales():
    return await SalesController.find_all()


@router.get("/sales/{id}", tags=["sales"])
async def find_one_sales(sales_id: int):
    return await SalesController.find_one(sales_id)


@router.put("/sales/{id}", tags=["sales"])
async def update_sales(sales_id: int, sales: SalesDto):
    return await SalesController.update(sales_id, sales)


@router.delete("/sales/{id}", tags=["sales"])
async def delete_sales(sales_id: int):
    return await SalesController.delete(sales_id)
