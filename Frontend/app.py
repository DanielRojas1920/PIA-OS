from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# "Base de datos" temporal (lista)
tasks = [
    {"id": 1, "title": "Aprender Flask"},
    {"id": 2, "title": "Hacer un CRUD"},
]

# Página principal - leer
@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

# Crear
@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    if title:
        new_id = max([t["id"] for t in tasks]) + 1 if tasks else 1
        tasks.append({"id": new_id, "title": title})
    return redirect(url_for("index"))

# Editar
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    task = next((t for t in tasks if t["id"] == id), None)
    if not task:
        return redirect(url_for("index"))

    if request.method == "POST":
        task["title"] = request.form.get("title")
        return redirect(url_for("index"))

    return render_template("edit.html", task=task)

# Eliminar
@app.route("/delete/<int:id>")
def delete(id):
    global tasks
    tasks = [t for t in tasks if t["id"] != id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
