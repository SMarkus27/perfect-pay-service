import pytest

from src.domain.entities.client import Client


def test_correct_client():
    client = {
        "name": "John Doe",
        "cpf": "10134578963",
        "email": "test@test.br",
    }
    Client(**client)


def test_invalid_name():
    client = {
        "name": "Jo",
        "cpf": "10134578963",
        "email": "test@test.br",
    }
    with pytest.raises(Exception) as e:
        Client(**client)


def test_invalid_cpf():
    client = {
        "name": "John Doe",
        "cpf": "1134578963",
        "email": "test@test.br",
    }
    with pytest.raises(Exception) as e:
        Client(**client)


def test_invalid_email():
    client = {
        "name": "John Doe",
        "cpf": "10134578963",
        "email": "test#test.br",
    }
    with pytest.raises(Exception) as e:
        Client(**client)

