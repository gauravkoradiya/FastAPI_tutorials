from fastapi import FastAPI,Query
from typing import Optional
from typing import List

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/items/")
async def read_item(skip : int = 0, limit:int = 10):
    return fake_items_db[skip:skip+limit]


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    print(item)
    if q:
        item.update({"q": q})
    if short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    print(item)
    return item

@app.get("/item_validation/")
async def read_items1(q:Optional[str] = Query("fixedquery",max_length=50)):
    results = {"test" : "a"}
    if q:
        results.update({"test1":q})
    return results

@app.get("/item_list/")
async def list_parameter(q:List[str]=Query(None)):
    query_items = {"q": q}
    print(query_items)
    return query_items
