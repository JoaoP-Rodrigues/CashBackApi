# imports
from flask import Flask, request, redirect, url_for
from datetime import datetime
from db import *
from validations import *

# create API with Flask
app = Flask("CashBack")

# main function.
# here is the all call functions and returns to frontend
@app.route("/api/cashback", methods=["POST"])
def getCashBack():
    
    # get all input informations from frontend by request function and add in body variable(dictionary).
    body = request.get_json()
    
    # get CPF from customer
    customer_cpf = body["customer"]["document"]
    
    # call the function to validate CPF
    if not cpfValidate(customer_cpf):
        response = {"message": "CPF Inválido!"}
        return response
    
    # get all cashbacks values of all products
    # so, add this values and the respective product in a dictionary for control.
    dict_percent_prods = {}
    for p in body["products"]:
        percent = checkProds(p["type"])
        t = p["type"]
        dict_percent_prods[t] = percent
    
    # call function do check if values of each product in order are equal than total order
    if not checkValues(body["total"], body["products"]):
        response = {"message": "O valor da compra não corresponde a soma dos valores dos produtos!"}
        return response
    
    # call function to check input date.
    # two validates are made here, if the date is in the future, and if is format valid
    if not checkDate(body["sold_at"]):
        response = {"message": "A data informada é inválida!"}
        return response
    
    # call function to get the value from products
    # this will calculate the value * quantity
    list_total_prods = getSums(body["products"])
    
    # call function to calculate the total value from cashback
    total_cashback = calculateCashbacks(dict_percent_prods, list_total_prods)
    
    # get datetime from time of call by API
    today = datetime.today()
    today = str(today).split('.')
    today = today[0]

    # create a dictionary to store datas of execution.
    # same are take from functions, others are take from input
    # this dictionary will send to other function to insert in database
    req_cashback = {
        "createdAt": today,
        "message": "Cashback criado com sucesso!",
        "document": body["customer"]["document"],
        "cashback": total_cashback
    }

    # try insert the above datas in database using a function.
    get_return_db = insertCashBack(req_cashback)
    if not get_return_db:
        response = {"message": "Não foi possível gravar no Banco de Dados!"}
        return response

    id_reg_cash = lectureDb(today, customer_cpf)
    req_cashback["id"] = id_reg_cash

    #return req_cashback
    return redirect(url_for('redirExtApi'))



@app.route("/api/redir")
def redirExtApi():
    return "Joao"


app.run()
