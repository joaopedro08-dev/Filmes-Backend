from pydantic import BaseModel, Field
from typing import List, Optional

# Collection Model
class Film(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    name: str
    description: str
    director: str
    gender: List[str]
    img: str
    notes: float
    year: int

# Update Model
class FilmUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    director: str | None = None
    gender: List[str] | None = None
    img: str | None = None
    notes: float | None = None
    year: int | None = None