from http.client import HTTPException

from fastapi import FastAPI

from fastapi_practice.src.schemas import BandCreate
from schemas import BandBase,BandwithID ,GenreURLChoices



from werkzeug.serving import BaseWSGIServer

app = FastAPI()




BANDS = {}
@app.get("/bands")
async def get_BANDS(
        genre:GenreURLChoices | None = None,
        has_albums:bool = False) -> list[BandBase]:

        band_list = [BandBase(**b) for b in BANDS]

        if genre:
            band_list= [
            b for b in band_list if b.genre.value == genre.value
            ]

        if has_albums:
            band_list= [b for b in band_list if len(b.albums) > 0]
        return band_list

@app.get("/bands/{band_id}",status_code=206) #206 is success code
async def get_band(band_id:int) -> BandBase: #returns an object of type dict
    band = next((BandBase(**b) for b in BANDS if b["band_id"]==band_id),None)
    if band is None:
        raise HTTPException(status_code=404,detail="band not found")
    return band

@app.get("/bands /genre/{genre}",status_code=206)
async def get_by_genre(genre:GenreURLChoices) -> list[dict]:
    return [
       b for b in BANDS if b["genre"].lower()==genre.value
   ]

@app.post("/bands/create",status_code=206)
def create_band(band_data:BandCreate) -> BandwithID:
    id = BANDS[-1]["id"] + 1
    band = BandwithID(id=id,**band_data.model_dump()).model_dump()
    BANDS.append(band)
    return band








