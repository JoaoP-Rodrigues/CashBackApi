from flask import Flask, request
import json
from dbusers import insertUser

def cpfValidate(cpfNotValidate):

    # take only numbers from cpf input
    cpf = [int(char) for char in cpfNotValidate if char.isdigit()]

    # verify if the CPF contain exactly 11 digits
    if len(cpf) != 11:
        return False

    # test if the cpf contain a same number in 11 digits
    # this will pass in validate
    if cpf == cpf[::-1]:
        return False

    # verify the verifying digit
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True

app = Flask("CashBack")

@app.route("/api/cashback", methods=["POST"])
def getCashBack():
    body = request.get_json()
    customer_cpf = body["customer"]["document"]

    if not cpfValidate(customer_cpf):
        response = {}
        response["message"] = "CPF Inválido!"
        return response

    #customer_name = body["customer"]["name"]
    #products = body["products"]

    return

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
