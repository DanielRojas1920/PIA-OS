from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

tasks = [
    {"id": 1, "title": "Aprender Flask"},
    {"id": 2, "title": "Hacer un CRUD"},
]


@app.get("/get_data")
def send_data():

    return JSONResponse(content = tasks)

@app.get("/id_new")
def return_new_id():

    new_id = max([t["id"] for t in tasks]) + 1 if tasks else 1

    return JSONResponse(content = {'new_id': new_id})

@app.get("/save")
async def save_data(request: Request):
    data = await request.json()
    id = data.get("id")
    title = data.get('title')

    tasks.append({'id': id, 'title': title})

    return JSONResponse(content={"mensaje": "Tarea guardada existosamente."})

# Ejemplo de endpoint tipo POST
@app.post("/sumar")
def sumar(datos: dict):
    total = datos.get("a", 0) + datos.get("b", 0)
    return JSONResponse(content={"resultado": total})