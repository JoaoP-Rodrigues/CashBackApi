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

    test_dict = {}
    for p in body["products"]:
        percent = checkProds(p["type"])
        t = p["type"]
        test_dict[t] = percent

    if not checkValues(body["total"], body["products"]):
        response = {"message": "O valor da compra não corresponde a soma dos valores dos produtos!"}
        return response

    #hoje = {"Hoje": checkDate(body["sold_at"])}
    list_total_prods = getSums(body["products"])
    

    return list_total_prods


def createResponse(status, message, name_of_content=False, content=False):
    response = {}
    response["status"] = status
    response["message"] = message

    if(name_of_content and content):
        response[name_of_content] = content
    return response

app.run()
