from dataclasses import dataclass

@dataclass
class CarData:
    id: int
    make: str
    model: str
    year: int
    color: str
    price: float
