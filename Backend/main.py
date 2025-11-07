from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import mysql.connector
import time

app = FastAPI()

for i in range(10):
    try:
        conn = mysql.connector.connect(
            host="db",
            user="user",
            password="SO.S7",
            database="tasks_db",
            port=3306,
        )
        if conn.is_connected():
            print("Conexión exitosa a MySQL")
            break
    except Error as e:
        print(f"Intento {i+1}: MySQL no disponible todavía ({e})")
        time.sleep(3)
else:
    print("No se pudo conectar a MySQL después de varios intentos")



@app.get("/get_data")
def send_data():

    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tasks;")

    tasks = cursor.fetchall()

    cursor.close()

    return JSONResponse(content = tasks)

    

@app.post("/save")
async def save_data(request: Request):

    cursor = conn.cursor(dictionary=True)

    data = await request.json()

    query = "INSERT INTO tasks (title) VALUES (%s);"
    values = (data['title'], )

    cursor.execute(query, values)
    conn.commit()

    cursor.close()

    return JSONResponse(content={"mensaje": "Tarea guardada existosamente."})


@app.post("/edit/")
async def edit_data(request: Request):
    new_data = await request.json()

    index = next((i for i in range(len(tasks)) if tasks[i]['id'] == new_data['id']), 0)

    tasks[index] = new_data

    return JSONResponse(content={"mensaje": "Tarea modificada existosamente."})

@app.post("/delete/")
async def delete_data(request: Request):
    response = await request.json()

    index = next((i for i in range(len(tasks)) if tasks[i]['id'] == response['id']), 0)

    tasks.pop(index)

    return JSONResponse(content={"mensaje": "Tarea removida existosamente."})

# Ejemplo de endpoint tipo POST
@app.post("/sumar")
def sumar(datos: dict):
    total = datos.get("a", 0) + datos.get("b", 0)
    return JSONResponse(content={"resultado": total})