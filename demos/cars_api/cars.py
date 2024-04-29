from fastapi import FastAPI

from schemas import CarModel
from models import CarData

app = FastAPI()

@app.get("/cars", response_model=list[CarModel])
async def cars() -> list[CarData]:
    return [
        CarData(1, "Dodge", "Colt", 1977, "metallic blue", 10000.0),
        CarData(1, "Dodge", "Colt", 1977, "metallic blue", 10000.0)]


