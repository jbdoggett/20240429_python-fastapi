from pydantic import BaseModel

class BaseCar(BaseModel):
    make: str
    model: str
    year: int
    color: str
    price: float

class CarCreate(BaseCar): ...

class Car(BaseCar):
    id: int

    class Config: # for later
        from_attributes = True
