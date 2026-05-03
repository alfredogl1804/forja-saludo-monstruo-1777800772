from fastapi import FastAPI

app = FastAPI(title="Hola Monstruo")


@app.get("/")
def root():
    return {"mensaje": "hola desde el Monstruo"}
