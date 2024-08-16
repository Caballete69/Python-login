from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import csv
from dotenv import load_dotenv

def crear_app():
    app = Flask(__name__)


    @app.route("/", methods=["GET","POST"])
    def homepage():
            datos = []
            respuesta = False
            Registrado = False
            if request.method == "GET":
                return render_template('index.html')
            if request.method == "POST":
                datos.append(request.form.get("usu"))
                datos.append(request.form.get("contra"))
                basedatos = pd.read_csv("Flask/login/base_de_datos.csv")
                for i in range(len(basedatos)):
                    if datos[0] == basedatos.iloc[i][0]:
                        Registrado = True
                        if datos[1] == basedatos.iloc[i][1]:
                            respuesta = True
                            break
                        else:
                            respuesta = False
                    else:
                        Registrado == False
                        respuesta = False
                if respuesta == True:
                    return f"Hola {datos[0]}"
                else:
                    if Registrado == False:
                        return redirect(url_for('no_regis'))
                    else:
                        return render_template("index.html")

    @app.route("/no_register")
    def no_regis():
        return render_template("no_regis.html")
                
    @app.route("/registrar", methods=["GET","POST"])
    def registrarse():
        datos_registro = []
        validacion = False
        if request.method == "GET":
            return render_template("registrarse.html")
        if request.method == "POST":
            basedatos = pd.read_csv("Flask/login/base_de_datos.csv")
            datos_registro.append(request.form.get("usux"))
            datos_registro.append(request.form.get("contrax"))
            for i in range(len(basedatos)):
                if datos_registro[0] == basedatos.iloc[i][0]:
                    validacion = True
                else:
                    validacion = False
            if validacion == True:
                return render_template("registrarse.html")
            else:
                with open("Flask/login/base_de_datos.csv","a") as base_de_datos:
                    writer = csv.writer(base_de_datos)
                    writer.writerow(datos_registro)
                return redirect(url_for('homepage'))
    return app
            

if __name__ == '__main__':
    app = crear_app()
    app.run()