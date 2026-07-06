from fastapi import FastAPI
# FastAPI @app.get() Path Operation

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id:int):
    return {"item_id": item_id, "name": "Sample Item"}
# Access URL: /items/5

@app.get("/search/")
def search_items(name: str = None):
    return {"search_query": name}
