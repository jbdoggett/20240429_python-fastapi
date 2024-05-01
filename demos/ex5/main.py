from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated
import uvicorn

from services.cars_sql_data import CarsSqlData
import models
import schemas
# from database import engine

# ensures all tables are created
# models.Base.metadata.create_all(bind=engine)


app = FastAPI()

CarsSqlDataType = Annotated[CarsSqlData, Depends(CarsSqlData)]


@app.get("/cars", response_model=list[schemas.Car])
async def all_cars(
    cars_sql_data: CarsSqlDataType,
) -> list[models.Car]:
    return cars_sql_data.get_cars()


# Common Http Status Codes
# 200-level - Success
#   200 - Ok
#   201 - Created
#   204 - No Content
# 400-level - User Error
#   400 - Bad Request
#   404 - Not Found
# 500-level - Server Error
#   500 - Internal Server Error


@app.get("/cars/{car_id}", response_model=schemas.Car)
async def one_car(
    car_id: int,
    cars_sql_data: CarsSqlDataType,
) -> models.Car:
    if car_id < 1:
        raise HTTPException(status_code=400, detail="Invalid car id")

    car_model = cars_sql_data.get_car(car_id)

    if car_model is None:
        raise HTTPException(status_code=404, detail="Car not found")

    return car_model


@app.post("/cars", response_model=schemas.Car)
async def create_car(
    car: schemas.CarCreate,
    cars_sql_data: CarsSqlDataType,
) -> models.Car:
    return cars_sql_data.create_car(car)


@app.put("/cars/{car_id}", response_model=schemas.Car)
async def replace_car(
    car_id: int, car: schemas.Car, cars_sql_data: CarsSqlDataType
) -> models.Car:
    if car_id < 1:
        raise HTTPException(status_code=400, detail="Invalid car id")

    if car_id != car.id:
        raise HTTPException(status_code=400, detail="Car id mismatch")

    car_model = cars_sql_data.update_car(car)

    if car_model is None:
        raise HTTPException(status_code=404, detail="Car not found")

    return car_model


@app.delete("/cars/{car_id}", response_model=schemas.Car)
async def delete_car(
    car_id: int,
    cars_sql_data: CarsSqlDataType,
) -> models.Car:
    if car_id < 1:
        raise HTTPException(status_code=400, detail="Invalid car id")

    car_model = cars_sql_data.delete_car(car_id)

    if car_model is None:
        raise HTTPException(status_code=404, detail="Car not found")

    return car_model


def main() -> None:
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)


if __name__ == "__main__":
    main()
