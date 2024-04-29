from fastapi import FastAPI
from typing import Any, TypedDict

from schemas import Color
from models import ColorDict


app = FastAPI()

@app.get("/colors", response_model=list[Color])
async def root() -> list[ColorDict]:
    return [
        {"id": 1, "name": "red", "hex_code": "ff0000"},
        {"id": 2, "name": "green", "hex_code": "00ff00"},
        {"id": 3, "name": "blue", "hex_code": "0000ff"}]

@app.get("/stars")
async def all_stars() -> list[str]:
    return ["mwc560", "m45", "vega"]
