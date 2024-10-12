from fastapi import FastAPI

app = FastAPI()

@app.post("/")
async def post():
    return {"message": "hello from post route!"}
@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.put("/{id}")
async def put():
    return {"message": "hello from put route!"}

@app.get("/items")
async def list_item():
    return {"Message": "Hello fron items!!"}