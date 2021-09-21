from flask import Flask, request
import json
from dbusers import insertUser

app = Flask("CashBack")

@app.route("/api/cashback", methods=["POST"])
def getCashBack():
    body = request.get_json()
    customer_cpf = body["customer"]["document"]
    customer_name = body["customer"]["name"]

    return customer_name


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
