import re
from dataclasses import dataclass


@dataclass
class Client:
    name: str
    cpf: str
    email: str

    def __post_init__(self):
        Client.verify_name(self.name)
        Client.verify_cpf(self.cpf)
        Client.verify_email(self.email)

    @staticmethod
    def verify_name(name: str) -> str:
        if len(name) <= 2:
            raise Exception("Name must be greater than or equal to 1")
        return name

    #TODO creates a better validation
    @staticmethod
    def verify_cpf(cpf: str) -> str:
        if len(cpf) < 11:
            raise Exception("CPF must have 11 characters")
        return cpf

    @staticmethod
    def verify_email(email: str) -> str:
        regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
        valid_email = re.fullmatch(regex, email)
        if valid_email is None:
            raise Exception("Email invalid")
        return email