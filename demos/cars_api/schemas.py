from pydantic import BaseModel

class CarModel(BaseModel):
    id: int
    make: str
    model: str
    year: int
    color: str
    price: float
