import sqlite3
import json
import os

os.remove("cashback.db") if os.path.exists("cashback.db") else None


def createDB():
    con = sqlite3.connect("cashback")
    # sqlite3.Connection
    cur = con.cursor()
    # sqlite3.Cursor
    sql_create_prod = 'create table products' \
                      '(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, ' \
                      'prod_type varchar(20),' \
                      'prod_value float(12)' \
                      'prod_cash integer(100))'
    cur.execute(sql_create_prod)

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


# def insertUser(nome, cpf, products, percentcash):
#    con = sqlite3.connect('cashback.db')

# this code must be run only time, for insert products in database
# if you need add new products, update below datas and so execute the code.
def insertProds():
    con = sqlite3.connect("cashback")
    cur = con.cursor()
    sql_insert = 'insert into products values (?, ?, ?)'
    rec_prods = [("Electronics", 1000, 5),
                 ("Food", 100, 15),
                 ("Games", 200, 12)]

    for rec in rec_prods:
        cur.execute(sql_insert, rec)


def lecture():
    conn = sqlite3.connect('cashback')
    c = conn.cursor()
    c.execute("SELECT * FROM PRODUTOS")
    for linha in c.fetchall():
        print(linha)


createDB()
insertProds()
lecture()

