import fastapi


class BaseAPIRouter:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = fastapi.APIRouter()
        return cls._instance
