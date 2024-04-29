from fastapi import FastAPI

from schemas_ex2 import Car, CarCreate
from models_ex2 import CarModel

app = FastAPI()

@app.post("/cars", response_model=Car)
async def create_car(car: CarCreate) -> CarModel:
    print(car)
    return CarModel(1, car.make, car.model, car.year, car.color, car.price)
