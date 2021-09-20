from flask import Flask, request

from dbusers import insertUsuario

app = Flask("CashBack")

@app.route("/olamundo", methods=["GET"])
def olaMundo():
    return {"ola": "mundo"}


@app.route("/cadastra/usuario", methods=["POST"])
def cadastraUsuario():

    body = request.get_json()

    user = insertUsuario(body["nome"], body["email"], body["senha"])

    return user

app.run()
