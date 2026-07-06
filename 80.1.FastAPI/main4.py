from fastapi import FastAPI
# FastAPI @app.post() Path Operation

# BASIC SYNTAX
# app=FastAPI()
# @app.post("/path")
# def function_name(data:dict):
#     return {"message":"Data recieved","data":data}

from pydantic import BaseModel
app=FastAPI()

class Item(BaseModel):
    name:str
    price:float

@app.post("/items/")
def create_item(item:Item):
    return {"message":"Item created successfully","item":item}