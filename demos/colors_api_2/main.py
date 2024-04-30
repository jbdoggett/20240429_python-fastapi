from fastapi import FastAPI

from schemas import Color, ColorCreate
from models import ColorDict, ColorDataClass


app = FastAPI()

@app.get("/colors", response_model=list[Color])
async def all_colors() -> list[ColorDict]:
    return [
        {"id": 1, "name": "red", "hex_code": "ff0000"},
        {"id": 2, "name": "green", "hex_code": "00ff00"},
        {"id": 3, "name": "blue", "hex_code": "0000ff"}]

@app.get("/stars")
async def all_stars() -> list[str]:
    return ["mwc560", "m45", "vega"]

@app.get("/colors2", response_model=list[Color])
async def all_colors2() -> list[ColorDataClass]:
    return [
        ColorDataClass(1, "red", "ff0000"),
        ColorDataClass(2, "green", "00ff00"),
        ColorDataClass(3, "blue", "0000f")]

@app.post("/colors", response_model=Color)
async def create_color(color: ColorCreate) -> ColorDataClass:
    print(color)
    return ColorDataClass(1, color.name, color.hex_code)
