from fastapi import FastAPI

app = FastAPI()

@app.get("/") #Decorator
async def root():
    return {"message": "Hello, World!"}