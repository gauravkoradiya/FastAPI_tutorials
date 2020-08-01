from typing import Optional
from fastapi  import  FastAPI
from pydantic import BaseModel

"""
Run server : uvicorn file_name:app --reload

"""
app = FastAPI()

class Item(BaseModel):
    name:str
    price:float
    is_offer: Optional[bool] = None

@app.get("/")
def hello():
    return {"hello" : "world"}

@app.get("/items/{item_id}")
def read_item(q: Optional[str] = None, item_id:int = None):
    return {"item_id" : item_id, "q":q}

@app.put("/items/{item_id}")
def update_item(item_id:int, item: Item):
    return {"item_name" : item.name,"item_id":item_id}
