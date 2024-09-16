
from fastapi import  FastAPI,Path
import uvicorn
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    price:float
    brand:Optional[str] = None #this is now optional

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

inventory = {

}

@app.get("/")
def home():
    return {"Data": "Testing"}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description="the id of the item you would like to view",gt=0)):
    return inventory[item_id]

@app.get("/get-by-name") #querying ?=name
def get_item(*,test:int,name: Optional[str] = None): #name param is optional and can take a None value
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Error":"Item not found"}

@app.post("/create-item/{item_id}")
def create_item(item_id:int,item:Item):
    if item_id in inventory:
        return {"Error":"Item already exists"}
    inventory[item_id] = item

    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id:int,item:UpdateItem):
    if not item_id in inventory:
        return {"item doesnt exist"}

    if item.name != None:

        inventory[item_id].name = item.name

    if item.price != None:
        inventory[item_id].price = item.price

    if item.brand != None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]



