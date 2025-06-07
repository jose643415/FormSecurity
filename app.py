from flask import Flask, render_template, request, redirect
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

cred = credentials.Certificate("formulario-db-647f4-firebase-adminsdk-fbsvc-f94f505f2e.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route("/", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        datos = {
            "nombre": request.form["nombre"],
            "telefono": request.form["telefono"],
            "ciudad": request.form["ciudad"],
            "pais": request.form["pais"],
            "observaciones": request.form["observaciones"]
        }
        db.collection("registros").add(datos)
        return "✅ Datos guardados en Firestore db"
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)

