import sqlite3
import os
#os.remove("cashback.db") if os.path.exists("cashback.db") else None

con = sqlite3.connect("cashback.db")

def createDB():
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

    sql_create_cashreqs = '''CREATE TABLE IF NOT EXISTS cashreqs(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                           createdAt date(20),
                           message varchar(100),
                           document varchar(11),
                           cashback double(100))'''

    cur.execute(sql_create_cashreqs)


def lecture():
    c = con.cursor()
    c.execute("SELECT * FROM sells")
    for linha in c.fetchall():
        print(linha)


def insertCashBack(dict_cash_datas):
    con_cash = sqlite3.connect("cashback.db")
    conect = con_cash.cursor()

    createdAt = dict_cash_datas["createdAt"]
    message = dict_cash_datas["message"]
    document = dict_cash_datas["document"]
    cashback = dict_cash_datas["cashback"]
    try:
        conect.execute("INSERT INTO cashregs (createdAt, message, document, cashback) VALUES (?, ?, ?, ?)", (createdAt, message, document, cashback))
    except:
        return False

createDB()

