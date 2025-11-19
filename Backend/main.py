from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from prometheus_fastapi_instrumentator import Instrumentator
import mysql.connector
import time

app = FastAPI()

# Activar métricas Prometheus para FastAPI
Instrumentator().instrument(app).expose(app)


# --------------------------
#   CONEXIÓN A LA BASE
# --------------------------
def get_connection():
    return mysql.connector.connect(
        host="db",
        user="user",
        password="SO.S7",
        database="tasks_db",
        port=3306,
    )


# --------------------------
#   GET: Leer tareas
# --------------------------
@app.get("/get_data")
def send_data():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tasks;")
    tasks = cursor.fetchall()

    cursor.close()
    conn.close()

    return JSONResponse(content=tasks)


# --------------------------
#   POST: Crear tarea
# --------------------------
@app.post("/save")
async def save_data(request: Request):
    data = await request.json()

    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO tasks (title, date, description) VALUES (%s, %s, %s);"
    values = (data["title"], data["date"], data["description"])

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return JSONResponse(content={"mensaje": "Tarea guardada exitosamente."})


# --------------------------
#   POST: Editar tarea
# --------------------------
@app.post("/edit")
async def edit_data(request: Request):
    data = await request.json()

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE tasks
        SET title = %s, date = %s, description = %s
        WHERE id = %s;
    """

    values = (data["title"], data["date"], data["description"], data["id"])

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return JSONResponse(content={"mensaje": "Tarea modificada exitosamente."})


# --------------------------
#   POST: Eliminar tarea
# --------------------------
@app.post("/delete")
async def delete_data(request: Request):
    data = await request.json()

    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM tasks WHERE id = %s;"
    values = (data["id"],)

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return JSONResponse(content={"mensaje": "Tarea eliminada exitosamente."})
