import sqlite3


# this line code bellow must be used to restart database
# os.remove("cashback.db") if os.path.exists("cashback.db") else None

# this function will create a new database if one is not found
def createDB():
    con = sqlite3.connect("cashback.db")
    cur = con.cursor()
    sql_create_cashreqs = ('CREATE TABLE IF NOT EXISTS cashregs(\n'
                           '                           id varchar, \n'
                           '                           createdAt TEXT,\n'
                           '                           message TEXT,\n'
                           '                           document varchar(11),\n'
                           '                           cashback double(100))')

    cur.execute(sql_create_cashreqs)
    cur.close()
    con.close()


'''
def lectureDb(data_reg, customer_cpf):
    try:
        con_l = sqlite3.connect("cashback.db")
        cur_q = con_l.cursor()
        sql_select_id = "SELECT id FROM cashregs WHERE document == '{}' AND createdAt == '{}'".format(customer_cpf, data_reg)

        cur_q.execute(sql_select_id)
        id_reg = cur_q.fetchone()
        id_reg = id_reg[0]
        cur_q.close()
        con_l.close()

        return id_reg
    except:
        return False
'''


# this function will save all data in the database
def insertCashBack(dict_cash_datas):
    # make a connection with the database created above
    con_cash = sqlite3.connect("cashback.db")
    conect_cash = con_cash.cursor()

    # get all elements  from input dictionary and save each one in a variable
    id_insert = dict_cash_datas["id"]
    createdAt = dict_cash_datas["createdAt"]
    message = dict_cash_datas["message"]
    document = dict_cash_datas["document"]
    cashback = dict_cash_datas["cashback"]

    # try insert data in database
    # if this fail, will return False to main page
    try:
        conect_cash.execute("INSERT INTO cashregs (id, createdAt, message, document, cashback) VALUES (?, ?, ?, ?, ?)",
                            (id_insert, createdAt, message, document, cashback))
        con_cash.commit()
        conect_cash.close()
        con_cash.close()

        return True
    except:
        return False


createDB()
