from unittest.mock import patch, Mock

import pytest

from src.application.usecases.sales.create_sales import CreateSales
from src.infra.repositories.client import ClientRepository
from src.infra.repositories.product import ProductRepository
from src.infra.repositories.sales import SalesRepository


@pytest.mark.asyncio
@patch.object(ClientRepository, "find_one_by_id")
@patch.object(SalesRepository, "create")
@patch.object(ProductRepository, "find_one_by_id")
async def test_create_sales(find_one_by_id_patch: Mock, create_patch: Mock, find_one_by_id_client_patch: Mock):
    sales_repository = SalesRepository()
    product_repository = ProductRepository()
    client_repository = ClientRepository()

    sales = {
        "product": 2,
        "client": 1,
        "sales_date": "2024-02-02",
        "quantity": 5,
        "discount": 0.5,
        "status": True
    }

    sales_id = [{"id": 1}]
    client_id = [{"id: 1"}]

    find_one_by_id_client_patch.return_value = client_id
    find_one_by_id_patch.return_value = sales_id

    sales_with_id = sales.copy()
    sales_with_id["id"] = 1

    expected = {
        "success": True,
        "message": "sales created successfully",
        "data": sales_with_id,
    }

    create_patch.return_value = sales_with_id
    result = await CreateSales(sales_repository, product_repository, client_repository).execute(sales)

    assert result == expected


@pytest.mark.asyncio
@patch.object(ClientRepository, "find_one_by_id")
async def test_create_sales_product_not_found(find_one_by_id_client_patch: Mock):
    sales_repository = SalesRepository()
    product_repository = ProductRepository()
    client_repository = ClientRepository()

    sales = {
        "product": 2,
        "client": 1,
        "sales_date": "2024-02-02",
        "quantity": 5,
        "discount": 0.5,
        "status": True
    }

    find_one_by_id_client_patch.return_value = []

    expected = {
        "success": False,
        "message": "Client not found",
    }

    result = await CreateSales(sales_repository, product_repository, client_repository).execute(sales)

    assert result == expected


@pytest.mark.asyncio
@patch.object(ClientRepository, "find_one_by_id")
@patch.object(ProductRepository, "find_one_by_id")
async def test_create_sales_product_not_found(find_one_by_id_patch: Mock, find_one_by_id_client_patch: Mock):
    sales_repository = SalesRepository()
    product_repository = ProductRepository()
    client_repository = ClientRepository()

    sales = {
        "product": 2,
        "client": 1,
        "sales_date": "2024-02-02",
        "quantity": 5,
        "discount": 0.5,
        "status": True
    }

    product_id = []
    client_id = [{"id: 1"}]

    find_one_by_id_client_patch.return_value = client_id
    find_one_by_id_patch.return_value = product_id

    expected = {
        "success": False,
        "message": "Product not found",
    }

    result = await CreateSales(sales_repository, product_repository, client_repository).execute(sales)

    assert result == expected


