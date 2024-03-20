from pydantic import BaseModel


# Basic user model to define attribute;
class User(BaseModel):
    username: str
    password: str
