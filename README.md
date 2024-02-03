# CashBack_Api
Code created for an API example that returns Cash Back.
This API was created to calculate the value of cashback from retailers that uses the services of Owner of this API.

_________________________________
REQUIREMENTS:
    For correct functioning, will be necessary have install the functions bellow:
    ------------------------------------------------------------------------------------------------------
    - FLASK 
        This is the micro framework to create and use APIs in Python.
    - SQLite3
        This is the database to store datas.
        Note*: other databases can be used, of your choice, but here I use SQLite only as an example.
        
    - All internal and external functions from python are imported in the start of code.
    ------------------------------------------------------------------------------------------------------
    
    For use it, will be necessary send a JSON file similar to informed bellow:
        
        "apikey": "NUMBERofApiKey",
        "sold_at": "2021-09-23 00:00:00",
        "customer": {
           "document": "00000000000",
           "name": "Catarina Da Silva"
        },
        "total": "100.00",
        "products": [
           {
              "type": "A",
              "value": "20.00",
              "qty": 3
           },
           {
              "type": "B",
              "value": "10.00",
              "qty": 4
           }
     If a different format is informed, the function will return a error message.
     Ps.: The quantity of products is unlimited
_________________________________

DETAILS OF FILES

It have three python files:
    routes.py
    validations.py
    db.py
    
    -------------------------------------------------------------------------------------------------------
routes.py
    This file is the main code from API. Here is executed the all functions, include the functions that are in outhers files.
    Here have only one route ("/api/cashback"), that run in function "getCashBack".
    This function receive data (JSON format) from frontend and run the all functions in a logical sequence.
     
    In start, it will check and validate the informed data (CPF, Dates and APIKey).
    So, it will call functions to validate product's values, and save their sum.
    Next, will send to extern API from Owner the necessary data to request a creation date and save cashback value
    In the last, it will insert all necessary data in a local database (SQLite) and return this same data from FrontEnd
    
    -------------------------------------------------------------------------------------------------------
    
validations.py
    This file will check and validate all data send by routes.py
    For this, there are seven functions.
        -- validateKey (It will check and validate the ApiKey from retailer)
        -- cpfValidate (it will validate if the CPF from customer is valid)
        -- checkProds (It will check the recpective cashback's values from each category of product and return to routes.py)
        -- checkValues (it will check if the total value from purchase is equal to sum of all products)
        -- checkDate (this will validate the input date from retailer. If the date is in future, for example)
        -- getSums (it will calculate and return one dictionary with the all sums of products in the purchase (quatity * unit value))
        -- calculateCashback (this function will calculate the value of cashback to each product.
 
    -------------------------------------------------------------------------------------------------------
 db.py
    This file will create and insert data in the local database using the SQLite
    Basically, there are two functions:
        -- createDB (it will created the database and the table if is not exist)
        -- insertCashBack (it will insert the data send by routes.py in database)
        
        
    
    
    
