from pydantic import BaseModel


class Save(BaseModel):
    number: int
    password: str