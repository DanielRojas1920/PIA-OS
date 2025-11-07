from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)

# "Base de datos" temporal (lista)


# Página principal - leer
@app.route("/")
def index():

    tasks = requests.get("http://backend:8000/get_data").json()

    return render_template("index.html", tasks=tasks)

# Crear
@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    if title:
        new_id = requests.get("http://backend:8000/new_id").json()['new_id']

        payload = {'id': new_id, 'title': title}

        requests.post("http://backend:8000/save", json = payload)

    return redirect(url_for("index"))


# No útiles

# Editar
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    try:
        
        response = requests.get("http://backend:8000/get_data")
        os.sleep(3)
        print("Código de respuesta:", response.status_code)
        print("Contenido:", response.text)
        tasks = response.json()
    except Exception as e:
        print("Error al obtener tasks:", e)
        tasks = []

    task = next((t for t in tasks if t["id"] == id), None)
    if not task:
        return redirect(url_for("index"))

    if request.method == "POST":
        task["title"] = request.form.get("title")
        request.post(f"http://backend:8000/edit/", payload = task)
        return redirect(url_for("index"))

    return render_template("edit.html", task=task)

# Eliminar
@app.route("/delete/<int:id>", methods = ["POST"])
def delete(id):
    
    payload = {'id': id}

    request.post(f"http://backend:8000/delete/", payload = payload)


    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
