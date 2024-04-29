from typing import Any, TypedDict
from dataclasses import dataclass

class ColorDict(TypedDict):
    id: int
    name: str
    hex_code: str

@dataclass
class ColorDataClass:
    id: int
    name: str
    hex_code: str

