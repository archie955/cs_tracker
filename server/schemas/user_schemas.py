from pydantic import BaseModel


class login(BaseModel):
    steam_id: str
