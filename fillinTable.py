#!/usr/bin/env python3
import sqlite3
import random
from sqlite3 import Error

def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def dropTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")
    try:
        sql = "DROP TABLE customer;"
        _conn.execute(sql)
        sql = "DROP TABLE car;"
        _conn.execute(sql)
        sql = "DROP TABLE branch;"
        _conn.execute(sql)
        sql = "DROP TABLE sales;"
        _conn.execute(sql)
        sql = "DROP TABLE rental;"
        _conn.execute(sql)
        sql = "DROP TABLE services;"
        _conn.execute(sql)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def createTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")
    try:
        sql ="""create table customer(
                ct_custkey INTEGER,
                ct_name TEXT, 
                ct_address TEXT, 
                ct_email TEXT, 
                ct_password TEXT, 
                PRIMARY KEY(ct_custkey)
                );"""
        _conn.execute(sql)
        sql ="""create table car(
                c_carkey INTEGER,
                c_custkey INTEGER,
                c_price INTEGER,
                c_brand TEXT,
                c_year INTEGER,
                c_titlestatue TEXT,
                c_milage INTEGER,
                c_color TEXT,
                PRIMARY KEY(c_carkey)
                );"""
        _conn.execute(sql)
        sql ="""create table branch(
                b_branchkey INTEGER,
                b_custkey INTEGER,
                b_carkey INTEGER,
                b_serkey INTEGER,
                b_salekey INTEGER,
                b_rentkey INTEGER,
                b_location TEXT,
                PRIMARY KEY(b_branchkey)
                );"""
        _conn.execute(sql)
        sql ="""create table sales(
                sp_salekey INTEGER,
                sp_name TEXT,
                PRIMARY KEY(sp_salekey)
                );"""
        _conn.execute(sql)
        sql ="""create table rental(
                r_rentkey INTEGER,
                r_price INTEGER,
                r_pdate NUMERIC,
                r_ddate NUMERIC,
                PRIMARY KEY(r_rentkey)
                );"""
        _conn.execute(sql)
        sql ="""create table services(
                s_serkey INTEGER,
                s_price INTEGER,
                s_date TEXT,
                s_term TEXT,
                s_type TEXT,
                s_repair TEXT,
                s_workorder TEXT,
                PRIMARY KEY(s_serkey)
                );"""
        _conn.execute(sql)
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def populateCar(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Car")

    try:
        sql ='''INSERT INTO car(c_custkey,c_price,c_brand,c_year,c_titlestatue,c_milage,c_color) 
                VALUES( ?, ?, ?, ?, ?, ?, ?);'''
        cur = _conn.cursor()
        
        for ckey in range (1,201):
            print(ckey)
            ctkey = random.randint(1,100)
            cPrice = random.randint(10000,50000)

            brand = ['Acura','Audi','BMW','Chevorlet','Dodge','Fiat','Ford','GMC','Honda','Hyundai','Infinit','Jeep','Kia','Lexus','Mazda','Nissian', 'Mitsubishi', 'Ram','Subaru','Tesla','Toyota','Volkswagen','Volvo']
            cBrand = random.choice(brand)

            cYear = random.randint(1900,2020)

            title = ['clean','salvage','junk','bonded','reconstucted','rebuilt']
            cStat = random.choice(title)

            cMile = random.randint(30000,150000)

            color = ['red','blue','green','light blue','silver','black','white','yellow','orange','purple']
            cColor = random.choice(color)

            args = [ctkey, cPrice, cBrand, cYear, cStat, cMile, cColor]
            cur.execute(sql, args)
            _conn.commit()

        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def populateBranch(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Branch")

    try:
        sql ='''INSERT INTO branch(b_custkey,b_carkey,b_serkey,b_salekey,b_rentkey,b_location) 
                VALUES( ?, ?,?,?, ?, ?);'''
        cur = _conn.cursor()
        
        for bkey in range (1,401):
            print(bkey)
            ckey = random.randint(1,100)
            carkey = random.randint(1,200)
            serkey = random.randint(1,50)
            salekey = random.randint(1,100)
            rkey = random.randint(1,100)
            l = ['Merced','Fresno','Atwater','Los Angeles','Riverside','Madera','Sonoma','San Diego','Chowchilla','Cerritos','Long Beach','Clovis','Colfax','Elk Grove','San Jose','Sacramento','Hayward','Hemet','Hercules','Mailbu']
            location = random.choice(l)

            args = [ ckey, carkey, serkey,salekey, rkey, location]
            cur.execute(sql, args)
            _conn.commit()

        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def populatesales(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate sales")

    try:
        sql ='''INSERT INTO sales(sp_name) 
                VALUES(?);'''
        cur = _conn.cursor()
        
        for skey in range (1,101):
            print(skey)
            sName = ['Liam','Noah','William','James','Logan','Ben','Mason','Elijah','Oliver','Jacob'
                    'Micheal', 'Ethan','Daniel','Matthew','Adien','Henry','Joseph','Jackson','Samuel','Sebastian'
                    'Amy','David','Carter','Wyatt','Jayden','John','Owen','Dylan','Luke','Gabriel','Anothny',
                    'Isaac', 'Grayson','Jack','Julian','Levi','Christopher','Joshua','Andrew']
            name = random.choice(sName)
            args = [name]
            cur.execute(sql, args)
            _conn.commit()

        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def populateRent(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate sales")

    try:
        sql ='''INSERT INTO rental(r_price,r_pdate, r_ddate) 
                VALUES(?,?,?);'''
        cur = _conn.cursor()
        
        for rkey in range (1,101):
            print(rkey)

            year = 2000
            day = random.randint(1,15)
            day2 = random.randint(16,31)
            month = random.randint(1,12)
            pdate = str(year)+'-'+str(month)+'-'+str(day)
            ddate = str(year)+'-'+str(month)+'-'+str(day2)
            amount = day2-day
            price = random.randint(100,300)
            pPrice = price*amount
            args = [pPrice,pdate,ddate]
            cur.execute(sql, args)
            _conn.commit()

        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def populateService(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate sales")

    try:
        sql ='''INSERT INTO services(s_price,s_date,s_term,s_type,s_repair,s_workorder) 
                VALUES(?,?,?,?,?,?);'''
        cur = _conn.cursor()
        
        for skey in range (1,51):
            print(skey)
            price = random.randint(100,1000)
            month = random.randint(1,12)
            day = random.randint(1,31)
            date = '2000-'+str(month)+'-'+str(day)
            sterm = ['confirm','unconfirm']
            term = random.choice(sterm) 
            stype = ['oil change','transmission change','coolant change','other problems']
            type = random.choice(stype)
            srepair = ['yes', 'no']
            repair = random.choice(srepair)
            order = 'no ordering of new parts'
            if(repair == 'yes'):
                price +=2000
                order = 'ordering new parts'
        
            args = [price,date,term,type,repair,order]
            cur.execute(sql, args)
            _conn.commit()

        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def main():
    database = r"table.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTable(conn)
        createTable(conn)
        populateCustomer(conn)
        populateCar(conn)
        populateBranch(conn)
        populatesales(conn)
        populateRent(conn)
        populateService(conn)

    closeConnection(conn, database)

if __name__ == '__main__':
    main()