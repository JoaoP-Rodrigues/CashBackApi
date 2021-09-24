from flask import Flask, request
import json
from db import *
from validations import *

app = Flask("CashBack")

@app.route("/api/cashback", methods=["POST"])
def getCashBack():
    body = request.get_json()
    customer_cpf = body["customer"]["document"]

    if not cpfValidate(customer_cpf):
        response = {"message": "CPF Inválido!"}
        return response

    dict_percent_prods = {}
    for p in body["products"]:
        percent = checkProds(p["type"])
        t = p["type"]
        dict_percent_prods[t] = percent

    if not checkValues(body["total"], body["products"]):
        response = {"message": "O valor da compra não corresponde a soma dos valores dos produtos!"}
        return response

    if not checkDate(body["sold_at"]):
        response = {"message": "A data informada é inválida!"}
        return response

    list_total_prods = getSums(body["products"])

    total_cashback = calculateCashbacks(dict_percent_prods, list_total_prods)
    return_cashback = {
        "createdAt": "2021-07-26T22:50:55.740Z",
        "message": "Cashback criado com sucesso!",
        "id": "NaN",
        "document": "33535353535",
        "cashback": "10"
    }

    return return_cashback


def createResponse(status, message, name_of_content=False, content=False):
    response = {}
    response["status"] = status
    response["message"] = message

    if(name_of_content and content):
        response[name_of_content] = content
    return response

app.run()
