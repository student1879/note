from fastapi import FastAPI

app = FastAPI(title="Note API")

@app.get("/")
def root():
    return {"message": ""}