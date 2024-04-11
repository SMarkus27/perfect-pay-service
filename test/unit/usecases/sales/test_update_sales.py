from unittest.mock import patch, Mock

import pytest

from src.application.usecases.sales.update_sales import UpdateSales
from src.infra.repositories.client import ClientRepository
from src.infra.repositories.product import ProductRepository
from src.infra.repositories.sales import SalesRepository


@pytest.mark.asyncio
@patch.object(ProductRepository, "find_one_by_id")
@patch.object(ClientRepository, "find_one_by_id")
@patch.object(SalesRepository, "update")
@patch.object(SalesRepository, "find_one_by_id")
async def test_update_sales(find_one_by_id_patch: Mock, update_patch: Mock,
                            find_one_by_id_client_patch: Mock, find_one_by_id_product_patch: Mock):

    sales_repository = SalesRepository()
    client_repository = ClientRepository()
    product_repository = ProductRepository()

    sales_id = 1

    new_sales = {
        "product": 2,
        "client": 1,
        "sales_date": "2024-02-03",
        "quantity": 50,
        "discount": 0.65,
        "status": False
    }

    client_id = [{"id": 1}]
    product_id = [{"id": 1}]

    find_one_by_id_client_patch.return_value = client_id
    find_one_by_id_product_patch.return_value = product_id
    find_one_by_id_patch.return_value = new_sales

    expected = {"success": True, "message": "Sales updated", "data": new_sales}
    update_patch.return_value = new_sales
    result = await UpdateSales(sales_repository,client_repository, product_repository ).execute(sales_id, new_sales)

    assert result == expected


@pytest.mark.asyncio
@patch.object(ClientRepository, "find_one_by_id")
async def test_update_sales_client_not_found(find_one_by_id_client_patch: Mock):
    sales_repository = SalesRepository()
    client_repository = ClientRepository()
    product_repository = ProductRepository()

    sales_id = 1

    new_sales = {
            "product": 2,
            "client": 1,
            "sales_date": "2024-02-03",
            "quantity": 50,
            "discount": 0.65,
            "status": True
        }

    client_id = []

    find_one_by_id_client_patch.return_value = client_id

    expected = {"success": False, "message": "Client not found"}

    result = await UpdateSales(sales_repository, client_repository, product_repository).execute(sales_id, new_sales)

    assert result == expected


@pytest.mark.asyncio
@patch.object(ProductRepository, "find_one_by_id")
@patch.object(ClientRepository, "find_one_by_id")
async def test_update_sales_product_not_found(find_one_by_id_client_patch: Mock, find_one_by_id_product_patch: Mock):
    sales_repository = SalesRepository()
    client_repository = ClientRepository()
    product_repository = ProductRepository()

    sales_id = 1

    new_sales = {
            "product": 2,
            "client": 1,
            "sales_date": "2024-02-03",
            "quantity": 50,
            "discount": 0.65,
            "status": True
        }

    client_id = [{"id": 1}]
    product_id = []

    find_one_by_id_client_patch.return_value = client_id
    find_one_by_id_product_patch.return_value = product_id

    expected = {"success": False, "message": "Product not found"}

    result = await UpdateSales(sales_repository, client_repository, product_repository).execute(sales_id, new_sales)

    assert result == expected


@pytest.mark.asyncio
@patch.object(ProductRepository, "find_one_by_id")
@patch.object(ClientRepository, "find_one_by_id")
@patch.object(SalesRepository, "find_one_by_id")
async def test_update_sales_sales_not_found(find_one_by_id_patch: Mock, find_one_by_id_client_patch: Mock, find_one_by_id_product_patch: Mock):
    sales_repository = SalesRepository()
    client_repository = ClientRepository()
    product_repository = ProductRepository()

    sales_id = 100

    new_sales = {
            "product": 2,
            "client": 1,
            "sales_date": "2024-02-03",
            "quantity": 50,
            "discount": 0.65,
            "status": True
        }

    client_id = [{"id": 1}]
    product_id = [{"id": 1}]

    find_one_by_id_client_patch.return_value = client_id
    find_one_by_id_product_patch.return_value = product_id

    find_one_by_id_patch.return_value = []

    expected = {"success": False, "message": "Sales not found"}

    result = await UpdateSales(sales_repository, client_repository, product_repository).execute(sales_id, new_sales)

    assert result == expected
