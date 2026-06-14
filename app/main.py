from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    """_summary_

    Args:
        item_id (int): _description_
        q (str | None, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """_summary_

    Args:
        item_id (int): _description_
        item (Item): _description_

    Returns:
        _type_: _description_
    """
    return {"item_name": item.name, "item_id": item_id}
