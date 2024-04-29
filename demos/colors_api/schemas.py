from pydantic import BaseModel

class BaseColor(BaseModel):
    name: str
    hex_code: str

class ColorCreate(BaseColor): ...

class Color(BaseColor):
    id: int

    class Config: # for later
        from_attributes = True

