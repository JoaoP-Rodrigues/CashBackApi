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
    if product in list_products.items():
        return list_products[product]
    else:
        return 0
