from typing import Optional
from fastapi import FastAPI,Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    description:Optional[str] = None
    price : float
    tax : Optional[float] = None

class User(BaseModel):
    usename : str
    fulll_name : Optional[str] = None


@app.put('/items/{item_id}')
async def update_item(item_id:int, item:Item ,user: User, importance:int = Body(...)):
    results = {"item_id" : item_id,
               "item" : item,
               "user" : user,
               "importance" : importance}
    return results