from fastapi import FastAPI
from typing import Any

app = FastAPI()

@app.get("/planets")
async def root() -> list[dict[str,str]]:
    return [{"name": "Hollywood", "nearest_star": "Cher"},
            {"name": "Fitness", "nearest_star": ":Arnold"},
            {"name": "Ork", "nearest_star": "Robin"}]
