from fastapi import FastAPI
app=FastAPI(
    title="my first FastAPI",
    description="Learning FastAPI step by step",
    version="1.0.0"
)
@app.get("/")
def root():
    return  {"message": "FastAPI app created successfully!"}