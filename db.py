import sqlite3

# os.remove("cashback.db") if os.path.exists("cashback.db") else None

def createDB():
    con = sqlite3.connect("cashback.db")
    cur = con.cursor()
    sql_create_sells = '''CREATE TABLE IF NOT EXISTS sells(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                       sell_date date(20),
                       user_cpf varchar(20),
                       user_name varchar(100),
                       prod_type varchar(20),
                       prod_value float(12),
                       prod_qty float(12),
                       prod_cash integer(100))'''

    cur.execute(sql_create_sells)

    sql_create_cashreqs = '''CREATE TABLE IF NOT EXISTS cashregs(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                           createdAt TEXT,
                           message TEXT,
                           document varchar(11),
                           cashback double(100))'''

    cur.execute(sql_create_cashreqs)
    cur.close()
    con.close()


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


def insertCashBack(dict_cash_datas):
    con_cash = sqlite3.connect("cashback.db")
    conect_cash = con_cash.cursor()

    createdAt = dict_cash_datas["createdAt"]
    message = dict_cash_datas["message"]
    document = dict_cash_datas["document"]
    cashback = dict_cash_datas["cashback"]

    try:
        conect_cash.execute("INSERT INTO cashregs (createdAt, message, document, cashback) VALUES (?, ?, ?, ?)",
                            (createdAt, message, document, cashback))
        con_cash.commit()

        conect_cash.close()
        con_cash.close()

        return True

    except:

        return False

createDB()
