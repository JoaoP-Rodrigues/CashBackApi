# imports
from flask import Flask, request
from db import *
from validations import *
import requests

# create API with Flask
app = Flask("CashBack")


# main function.
# here is the all call functions and returns to frontend
@app.route("/api/cashback", methods=["POST"])
def getCashBack():
    # get all input informations from frontend by request function and add in body variable(dictionary).
    body = request.get_json()

    # get All Data from customer and API Key from seller
    try:
        customer_cpf = body["customer"]["document"]
        api_key_user = body["apikey"]
        datePurchase = body["sold_at"]
        totalPurchase = body["total"]
        allProducts = body["products"]
    except:
        response = {"message": "Existe um erro no formato do arquivo. Certifique de que ele esteja correto!"}
        return response

    # call the function to validate API Key
    if not validateKey(api_key_user):
        response = {"message": "A Chave da API está incorreta!"}
        return response

    # call the function to validate CPF
    if not cpfValidate(customer_cpf):
        response = {"message": "CPF Inválido!"}
        return response

    # get all cashbacks values of all products
    # so, add this values and the respective product in a dictionary for control.
    dict_percent_prods = {}
    for p in allProducts:
        percent = checkProds(p["type"])
        t = p["type"]
        dict_percent_prods[t] = percent

    # call function do check if values of each product in order are equal than total order
    if not checkValues(totalPurchase, allProducts):
        response = {"message": "O valor da compra não corresponde a soma dos valores dos produtos!"}
        return response

    # call function to check input date.
    # two validates are made here, if the date is in the future, and if is format valid
    if not checkDate(datePurchase):
        response = {"message": "A data informada é inválida!"}
        return response

    # call function to get the value from products
    # this will calculate the value * quantity
    list_total_prods = getSums(allProducts)

    # call function to calculate the total value from cashback
    total_cashback = calculateCashbacks(dict_percent_prods, list_total_prods)

    # this bellow part will use the extern api from Owner of this code
    # it will send to a url one json with two elements; CPF from customer and the total cashback calculated above
    base_url = 'https://5efb30ac80d8170016f7613d.mockapi.io/api/mock/Cashback'
    parameters = {'document': customer_cpf, 'cashback': total_cashback}

    # get a request from the API
    req_api_mt = requests.post(base_url, params=parameters)

    # and convert the json format to a dictionary from Python
    data_register = req_api_mt.json()

    # create a dictionary to store data's of execution.
    # same are take from functions, others are take from input
    # this dictionary will send to other function to insert in database
    req_cashback = {
        "createdAt": data_register['createdAt'],
        "id": data_register['id'],
        "message": data_register['message'],
        "document": customer_cpf,
        "cashback": total_cashback
    }

    # try insert the above data's in database using a function.
    get_return_db = insertCashBack(req_cashback)
    if not get_return_db:
        response = {"message": "Não foi possível gravar no Banco de Dados!"}
        return response

    return req_cashback


app.run()
