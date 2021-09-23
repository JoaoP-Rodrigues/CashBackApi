from datetime import datetime

# this function will validade the consumer CPF
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


# this function will receive on input a product type
# if the product exist in dict, will return the cashback percent, if not, return "0"
def checkProds(product):
    list_products = {"A": 15, "B": 5, "C": 10, "D": 12, "E": 3}
    if product not in list_products:
        return 0
    else:
        return list_products[product]


def checkValues(totalSell, prods_values):
    totalSell = float(totalSell)
    sumValues = 0.0
    sumProds = {}
    for p in prods_values:
        temp_sum = float(p["value"]) * p["qty"]
        sumValues += float(temp_sum)
        prod = p["type"]
        sumProds[prod] = temp_sum

    if sumValues != totalSell:
        return False
    else:
        return True


def checkDate(date):
    today = datetime
    return today


def getSums(prod_value):
    sumProds = {}
    for v in prod_value:
        temp_sum = float(v["value"]) * v["qty"]
        prod = v["type"]
        sumProds[prod] = temp_sum

    return sumProds


def calculateCashbacks(dict_cashs, dict_sums):
    total_cash = 0

    for k, v in dict_sums.items():
        convert_to_percent = dict_cashs[k] / 100
        temp_cash = v * convert_to_percent
        total_cash += temp_cash

    return total_cash
