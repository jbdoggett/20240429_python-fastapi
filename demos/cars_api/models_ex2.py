from dataclasses import dataclass

@dataclass
class CarModel:
    id: int
    make: str
    model: str
    year: int
    color: str
    price: float
