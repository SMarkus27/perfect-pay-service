from src.application.usecases.dtos.client import ClientDto
from src.controllers.client import ClientController
from src.infra.web.http.base import BaseAPIRouter

router = BaseAPIRouter.get_instance()


@router.post("/client/", tags=["client"])
async def create_product(client: ClientDto):
    return await ClientController.create(client)


@router.get("/client/", tags=["client"])
async def find_all_client():
    return await ClientController.find_all()


@router.get("/client/{id}", tags=["client"])
async def find_one_client(client_id: int):
    return await ClientController.find_one(client_id)


@router.put("/client/{id}", tags=["client"])
async def update_client(client_id: int, client: ClientDto):
    return await ClientController.update(client_id, client)


@router.delete("/client/{id}", tags=["client"])
async def delete_client(client_id: int):
    return await ClientController.delete(client_id)
