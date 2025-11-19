from flask import Flask, render_template, request, redirect, url_for
import requests
import time
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Página principal - leer
@app.route("/")
def index():
    tasks = requests.get("http://backend:8000/get_data").json()
    return render_template("index.html", tasks=tasks)

# Crear
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("create.html")

    title = request.form.get("title")
    date = request.form.get("date")
    description = request.form.get("description")

    payload = {
        "title": title,
        "date": date,
        "description": description
    }

    requests.post("http://backend:8000/save", json=payload)

    return redirect(url_for("index"))

# Editar
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    response = requests.get("http://backend:8000/get_data")
    task = next((t for t in response.json() if t["id"] == id), None)

    if not task:
        return redirect(url_for("index"))

    if request.method == "POST":
        updated_task = {
            "id": id,
            "title": request.form.get("title"),
            "date": request.form.get("date"),
            "description": request.form.get("description")
        }

        requests.post("http://backend:8000/edit", json=updated_task)
        return redirect(url_for("index"))

    return render_template("edit.html", task=task)

# Eliminar
@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    payload = {"id": id}
    requests.post("http://backend:8000/delete", json=payload)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
