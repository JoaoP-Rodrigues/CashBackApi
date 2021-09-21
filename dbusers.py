import sqlite3
import json
import os
os.remove("cashback.db") if os.path.exists("cashback.db") else None


def insertUser(nome, email, senha):
    con = sqlite3.connect('cashback.db')
    sqlite3.Connection
    cur = con.cursor()
    sqlite3.Cursor
    sql_create = 'create table sells' \
                 '(id integer primary key, ' \
                 'customer_cpf varchar(11), ' \
                 'prod_type varchar(20),' \
                 'prod_value float(12)' \
                 'prod_qty integer(100)'

    cur.execute(sql_create)



