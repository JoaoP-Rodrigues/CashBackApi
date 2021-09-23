from datetime import datetime

# this function will validade the consumer CPF
def cpfValidate(cpfNotValidate):

    # take only numbers from cpf input
    try:
        cpf = [int(char) for char in cpfNotValidate if char.isdigit()]
    except:
        return False

    # verify if the CPF contain exactly 11 digits
    if len(cpf) != 11:
        return False

    # test if the cpf contain a same number in 11 digits
    # this will pass in first validate
    if cpf == cpf[::-1]:
        return False

    # check and validate the verifying digit
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True


# this function will receive on input a product type
# if the product exist in dict, will return the cashback percent, if not, return "0"
# if necessary, you could add new category products, just add new elements in the dictionary 
def checkProds(product):
    list_products = {"A": 15, "B": 5, "C": 10, "D": 12, "E": 3}
    if product not in list_products:
        return 0
    else:
        return list_products[product]

# this function will validate the total value from sell
def checkValues(totalSell, prods_values):
    # take and convert the value from sell provided on input "json" to float format
    try:
        totalSell = float(totalSell)
        sumValues = 0.0

        # this for loop will take the quantity and value from all products
        # so, it is increment this value in a sum
        # next, compares sell's total and sum taked from values
        for p in prods_values:
            temp_sum = float(p["value"]) * p["qty"]
            sumValues += float(temp_sum)
            prod = p["type"]
    except:
        return False

    if sumValues != totalSell:
        return False
    else:
        return True


def checkDate(date):
    today = datetime
    return today

# simple function to get the sum values of all products in purchase
def getSums(prod_value):
    sumProds = {}
    for v in prod_value:
        temp_sum = float(v["value"]) * v["qty"]
        prod = v["type"]
        sumProds[prod] = temp_sum

    return sumProds

# this function will calculate the total of cashback
# in input, it's get two dictionarys; first one have the percent of cashback from each product, and second one have the total'sum from values of each product. 
def calculateCashbacks(dict_cashs, dict_sums):
    total_cash = 0

    for k, v in dict_sums.items():
        # below, it's convert value of cashback to percent
        # Ex.: 10 / 100 = 0.1 | Value Product = 50 | 50 * 0.1 = 5(10% from 50)
        convert_to_percent = dict_cashs[k] / 100
        temp_cash = v * convert_to_percent
        total_cash += temp_cash

    return total_cash
