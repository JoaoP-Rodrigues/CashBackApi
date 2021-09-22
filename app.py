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
        response = {}
        response["message"] = "CPF Inválido!"
        return response
    list_cashback_prods = []
    test_dict = {}
    i = 0
    for p in body["products"]:
        percent = checkProds(p[i]["type"])
        t = p[i]["type"]
        list_cashback_prods.append(percent)
        test_dict[t] = percent
        i += 1

    return test_dict

'''@app.route("/register/user", methods=["POST"])
def registerUser():

    body = request.get_json()

    user = insertUser(body["nome"], body["email"], body["senha"])

    return createResponse(200, "User Created", "user", user)
'''
def createResponse(status, message, name_of_content=False, content=False):
    response = {}
    response["status"] = status
    response["message"] = message

    if(name_of_content and content):
        response[name_of_content] = content
    return response

app.run()
