from pydantic import BaseModel


class UpInfo(BaseModel):
    uuid: str
    name: str

    model_config = {"frozen": True}
