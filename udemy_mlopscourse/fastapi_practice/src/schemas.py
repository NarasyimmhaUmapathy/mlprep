from enum import Enum
from pydantic import BaseModel,validator
from datetime import Date

class GenreURLChoices(str, Enum):  # improves db query efficiency, dont have to scan through the whole db each time
    Rock = "rock",
    Electronic = "electronic",
    Metal = "metal",
    HIP_HOP = "hip-hop"

class GenreChoices(str, Enum):  # improves db query efficiency, dont have to scan through the whole db each time
    Rock = "rock",
    Electronic = "electronic",
    Metal = "metal",
    HIP_HOP = "hip-hop"

class Album(BaseModel):
    title: str
    release_date: Date


class BandBase(BaseModel):

    genre:GenreChoices
    name:str
    albums=list[Album] = [] #defaults to empty list

class BandCreate(BandBase):
    @validator('genre',pre=True)
    def title_case(cls,value):
        return value.title() #r
        # ock -> Rock


class BandwithID(BandBase):
    id: int