from src.application.usecases.dtos.product import ProductDto
from src.controllers.product import ProductController
from src.infra.web.http.base import BaseAPIRouter

router = BaseAPIRouter.get_instance()


@router.post("/products/", tags=["products"])
async def create_product(product: ProductDto):
    return await ProductController.create(product)


@router.get("/products/", tags=["products"])
async def find_all_products():
    return await ProductController.find_all()


@router.get("/products/{id}", tags=["products"])
async def find_one_product(product_id: int):
    return await ProductController.find_one(product_id)


@router.put("/products/{id}", tags=["products"])
async def update_product(product_id: int, product: ProductDto):
    return await ProductController.update(product_id, product)


@router.delete("/products/{id}", tags=["products"])
async def delete_product(product_id: int):
    return await ProductController.delete(product_id)
