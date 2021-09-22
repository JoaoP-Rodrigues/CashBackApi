import sqlite3
import os

#os.remove("cashback.db") if os.path.exists("cashback.db") else None
con = sqlite3.connect("cashback")

def createDB():
    cur = con.cursor()
    sql_create_sells = 'create table sells' \
                       '(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, ' \
                       'sell_date date(20),' \
                       'user_cpf varchar(20),' \
                       'user_name varchar(100),' \
                       'prod_type varchar(20),' \
                       'prod_value float(12)' \
                       'prod_qty float(12)' \
                       'prod_cash integer(100))'

    cur.execute(sql_create_sells)

def lecture():

    c = con.cursor()
    c.execute("SELECT * FROM PRODUTOS")
    for linha in c.fetchall():
        print(linha)


createDB()
lecture()

