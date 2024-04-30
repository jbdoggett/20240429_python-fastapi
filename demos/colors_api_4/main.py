# Enable running uvicorn from within python.
from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated
import uvicorn

import models
import schemas
from database import engine
from services.colors_sql_data import ColorsSqlData

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

ColorsSqlDataType = Annotated[ColorsSqlData, Depends(ColorsSqlData)]

@app.get("/colors", response_model=list[schemas.Color])
async def all_colors(
    colors_sql_data: Annotated[ColorsSqlData, Depends(ColorsSqlData)],
                     ) -> list[models.Color]:
    return colors_sql_data.get_colors()

@app.get("colors/{color_id}", response_model=schemas.Color)
async def one_color(
    color_id: int,
    colors_sql_data: ColorsSqlDataType) -> models.Color:
    if color_id < 1:
        raise HTTPException(status_code=400, detail="Invalid color id")
    color_model = colors_sql_data.get_color(color_id)
    if color_model is None:
        raise HTTPException(status_code=404, detail="Color not found")
    return color_model

@app.post("/colors", response_model=schemas.Color)
async def create_color(color: schemas.ColorCreate,
                       colors_sql_data:
                       Annotated[ColorsSqlData, Depends(ColorsSqlData)],
                        ) -> models.Color:
    return colors_sql_data.create_color(color)

# put is a replace
@app.put("colors/{color_id}", response_model=schemas.Color)
async def replace_color(color_id: int,
                        color: schemas.Color,
                        colors_sql_data: ColorsSqlDataType
                        ) -> models.Color:
    if color_id < 1:
        raise HTTPException(status_code=400, detail="Invalid color id")
    if color_id != color.id:
        raise HTTPException(status_code=400, detail="Invalid color mismatch")
    color_model = colors_sql_data.update_color(color)
    if color_model is None:
        raise HTTPException(status_code=404, detail="Color not found")
    return color_model

def main() -> None:
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)

if __name__ == "__main__":
    main()
