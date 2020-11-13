import sqlite3
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
    
def insert1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q1")
    # insert new customer with file input, line by line
    try:
        file = open('input/1.in','r')

        customer = [0,0,0,0]
        for x in range(0,4):
            customer[x] = file.readline().replace('\n','')

        sql ='''INSERT INTO customer(ct_name,ct_address,ct_email,ct_password) 
                VALUES(?, ?, ?, ?);'''
    
        cur = _conn.cursor()
        cur.execute(sql,customer)
        _conn.commit()
    except Error as e:
        print(e)

def insert2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q2")
    # insert new car with input
    try:
        sql ='''INSERT INTO customer(c_custkey,c_price,c_brand,c_year,c_titlestatue,c_milage,c_color) 
                VALUES(?, ?, ?, ?,?,?,?);'''
        ckey = 47
        price = input('Enter the price for the car:')
        brand = input('Enter the car brand: ')
        year = input('Enter the year of the car: ')
        title = input('Enter the title of the car: ')
        mile = input('Enter the milages: ')
        color = input('Enter the color of the car: ')
        car = [ckey,price,brand,year,title,mile,color]
        cur = _conn.cursor()
        cur.execute(sql,car)
        _conn.commit()
    except Error as e:
        print(e)

def insert3(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q3")
    # input
    try:
        sql ='''INSERT INTO services(s_price,s_date,s_term,s_type,s_repair,s_workorder) 
                VALUES(?,?,?,?,?,?);'''
        file = open('input/3.in','r')

        service = [0,0,0,0,0,0]
        for x in range(0,5):
            service[x] = file.readline().replace('\n','')
        cur = _conn.cursor()
        cur.execute(sql,service)
        _conn.commit()
    except Error as e:
        print(e)

def insert4(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q4")
    # input
    try:
        sql ='''INSERT INTO rental(r_price,r_pdate,r_ddate) 
                VALUES(?,?,?);'''
        year = '2020'
        pdate = input('Enter the pickup date(mm-dd):')
        ddate = input('Enter the dropoff date(mm-dd):')

        if(pdate[3]=='0'):
            a0 = pdate[4]
        else:
            a0 = pdate[3:4]
        if(ddate[3]=='0'):
            a1 = ddate[4]
        else:
            a1 = ddate[3:4]
        if(pdate[0]=='0'):
            m0 = pdate[1]
        else:
            m0 = pdate[0:1]
        if(ddate[0]=='0'):
            m1 = ddate[1]
        else:
            m1 = ddate[0:1]
        price = 500*(int(m1)-int(m0))+300*(int(a1)-int(a0))

        rental = [price,year+'-'+pdate,year+'-'+ddate]

        cur = _conn.cursor()
        cur.execute(sql,rental)
        _conn.commit()
    except Error as e:
        print(e)

def insert5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q5")
    # input
    try:
        sql ='''INSERT INTO sales(sp_name) 
                VALUES(?);'''
        name = ['Tyson']
        cur = _conn.cursor()
        cur.execute(sql,name)
        _conn.commit()
        print('pass5')
    except Error as e:
        print(e)

def insert6(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q6")
    # input
    try:
        sql ='''INSERT INTO branch(b_custkey,b_carkey,b_serkey,b_salekey,b_rentkey,b_location) 
                VALUES(?,?,?,?,?,?);'''
        ckey = input('Enter your customer key: ')
        car = input('Enter your car key: ')
        file = open('input/6.in','r')

        branch = [0,0,0,0]
        for x in range(0,3):
            branch[x] = file.readline().replace('\n','')
        B = [ckey,car,branch[0],branch[1],branch[2],branch[3]]
        cur = _conn.cursor()
        cur.execute(sql,B)
        _conn.commit()
        print('pass6')
    except Error as e:
        print(e)

def update7(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q7")
    #update the customer information
    try:
        sql = '''update customer
                set ct_email = ?, ct_password = ?
                where ct_name = ? '''
        arg = ['reprouced123@yahoo.com','12345','Jim']
        cur = _conn.cursor()
        cur.execute(sql,arg)
        _conn.commit()
        
        sql = '''select * from customer where ct_name = 'Jim' '''
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row[0],'\t',row[1],'\t',row[2],'\t',row[3],'\t',row[4])
    except Error as e:
        print(e)

def update8(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q8")
    # update the car, print list all the customer car
    try:
        sql = '''update car
                set c_milage = ?, c_titlestatue = ?
                where c_custkey = ? '''
        ctkey = input("Enter your customer key: ")
        car = input("Enter your car key: ")
        updateCar = ['2000','junk',ctkey]
        cur = _conn.cursor()
        cur.execute(sql,updateCar)
        _conn.commit()

        sql = '''select *
                from car
                where c_custkey = ?'''
        cur.execute(sql,ctkey)
        rows = cur.fetchall()
        for row in rows:
            print(row[0],'\t',row[1],'\t',row[2],'\t',row[3],'\t',row[4],row[5],'\t',row[6],'\t',row[7])
        
        print('pass8')
    except Error as e:
        print(e)

def update9(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q9")
    #update the customer information
    try:
        sql = '''update services
                set s_term = ?, s_date = ?
                where s_serkey = ? '''
        arg = ['confirm','2000-01-19',50]
        cur = _conn.cursor()
        cur.execute(sql,arg)
        _conn.commit()
        
        sql = '''select * from services where s_serkey = 50 '''
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row[0],'\t',row[1],'\t',row[2],'\t',row[3],'\t',row[4],'\t',row[5],'\t',row[6])
    except Error as e:
        print(e)

def update10(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q10")
    #update the customer information
    try:
        sql = '''update sales
                set sp_name = ? 
                where sp_salekey = ?'''
        arg = ['Jack', 34]
        cur = _conn.cursor()
        cur.execute(sql,arg)
        _conn.commit()
        
        sql = '''select * from sales where sp_name = 'Jack' '''
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row[0],'\t',row[1])
    except Error as e:
        print(e)

def update11(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q11")
    try:
        cur = _conn.cursor()
        sql = '''select * from rental where r_price < ? '''
        amount = [3000]
        cur.execute(sql,amount)
        rows = cur.fetchall()
        large = 0
        for row in rows:
            print(row[0],'\t',row[1],'\t',row[2],'\t',row[3])
            if(large < row[1]):
                large = row[1]
        
                

        sql = '''update rental
                set r_price = ? 
                where r_price > ? '''
        arg = [large, 2000]
        cur.execute(sql,arg)
        _conn.commit()
    except Error as e:
        print(e)

def update12(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q12")
    try:
        sql = '''update branch
                set b_location = ? 
                where b_carkey = ?  AND b_custkey = ?'''
        location = input('Enter your new location branch: ')
        arg = [location,95,46]
        cur = _conn.cursor()
        cur.execute(sql,arg)
        _conn.commit()
    except Error as e:
        print(e)
        
def delete13(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q13")
    try:
        sql = '''delete from customer where ct_name = 'Jim' and ct_custkey = 3 '''
        cur = _conn.cursor()
        cur.execute(sql)
        _conn.commit()
    except Error as e:
        print(e)

def delete14(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q14")
    try:
        sql = '''delete from car where c_carkey = ? and c_custkey = ?'''
        ckey = input('Enter your car key:')
        ctkey = input('Enter your customer key:')
        arg = [ckey,ctkey]
        cur = _conn.cursor()
        cur.execute(sql,arg)
        _conn.commit()
    except Error as e:
        print(e)

def delete15(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q15")
    try:
        sql = '''select ct_custkey, s_serkey, s_price,s_date,s_term,s_type,s_repair,s_workorder
                from customer, branch, services
                where ct_custkey = ?
                    AND ct_custkey = b_custkey
                    AND b_serkey = s_serkey'''
        cur = _conn.cursor()
        ckey = input('Enter your customer key:')
        arg = [ckey]
        cur.execute(sql,arg)
        rows = cur.fetchall()
        for row in rows:
            print(row[0],'\t',row[1],'\t',row[2],'\t',row[3],'\t',row[4],'\t',row[5],'\t',row[6])

        skey = input('Which Service key would you like to delete:')
        sql = '''delete from services where s_serkey = ?''' 
        arg = [skey]
        cur.execute(sql,arg)
        _conn.commit()

        sql = '''select ct_custkey, s_serkey, s_price,s_date,s_term,s_type,s_repair,s_workorder
                from customer, branch, services
                where ct_custkey = ?
                    AND ct_custkey = b_custkey
                    AND b_serkey = s_serkey'''
        cur = _conn.cursor()
        arg = [ckey]
        cur.execute(sql,arg)
        rows = cur.fetchall()
        for row in rows:
            print(row[0],'\t',row[1],'\t',row[2],'\t',row[3],'\t',row[4],'\t',row[5],'\t',row[6])

    except Error as e:
        print(e)

def delete16(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q16")
    try:
        sql1 = '''select ct_custkey, b_location, sp_salekey, sp_name
                from customer, branch, sales
                where ct_custkey = ?
                    AND ct_custkey = b_custkey
                    AND b_serkey = sp_salekey'''
        cur = _conn.cursor()
        ckey = input('Enter your customer key:')
        arg = [ckey]
        cur.execute(sql1,arg)
        rows = cur.fetchall()
        for row in rows:
            print(row[0],'\t',row[1],'\t',row[2],'\t',row[3])

        
        sql2 = '''delete from sales where sp_salekey = ?''' 
        skey = [12]
        cur.execute(sql2,skey)
        _conn.commit()

        print('--------------------------------------------')
        arg = [ckey]
        cur.execute(sql1,arg)
        rows = cur.fetchall()
        for row in rows:
            print(row[0],'\t',row[1],'\t',row[2],'\t',row[3])

    except Error as e:
        print(e)

def delete17(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q17")
    try:
        sql = '''delete from rental where r_pdate LIKE ?'''
        arg = ['%2000-1%']
        cur = _conn.cursor()
        cur.execute(sql,arg)
        _conn.commit()
    except Error as e:
        print(e)

def delete18(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q18")
    try:
        sql = '''delete from branch where b_location = ?'''
        arg = ['Sacramento']
        cur = _conn.cursor()
        cur.execute(sql,arg)
        _conn.commit()
    except Error as e:
        print(e)

def compare(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q19")
    try:
        sql ='''select Q1.c_price, Q1.c_brand, Q1.c_year, Q2.c_price, Q2.c_brand, Q2.c_year
                from (select c_custkey, c_price,c_brand,c_year,c_titlestatue,c_milage,c_color,b_location
                        from car, branch
                        where c_brand = 'Honda'
                            AND c_titlestatue = 'bonded'
                        group by c_year)Q1,
                        (select c_custkey, c_price,c_brand,c_year,c_titlestatue,c_milage,c_color,b_location
                        from car, branch
                        where c_brand = 'Toyota'
                        group by c_year)Q2
                group by Q1.c_year,Q2.c_year'''
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            if row[0] < row[3]:
                print(str(row[0])+'\t'+row[1]+'\t'+str(row[2]))
            else:
                print(str(row[3])+'\t'+row[4]+'\t'+str(row[5]))
    except Error as e:
        print(e)

def listTop3car(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q20")
    try:
        sql ='''select b_custkey, b_carkey, c_brand, c_year, s_price, s_type, s_date, s_term
                from customer, branch, services, car
                where ct_custkey = b_custkey
                    AND b_serkey = s_serkey
                    AND b_carkey = c_carkey
                    AND c_year < 1910
                group by s_price
                order by s_price desc
                limit 3'''
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(str(row[0])+'\t'+str(row[1])+'\t'+row[2]+'\t'+str(row[3])+'\t'+str(row[4])+'\t'+row[5]+'\t'+row[6]+'\t'+row[7])

    except Error as e:
        print(e)

def main():
    database = r"table/table.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:

        insert1(conn) #insert customer
        insert2(conn) #insert car
        insert3(conn) #insert service
        insert4(conn) #insert rental
        insert5(conn) #insert sales
        insert6(conn) #insert branch

        update7(conn) #update customer
        update8(conn) #update car
        update9(conn) #update service
        update10(conn) #update sales
        update11(conn) #update rental
        update12(conn) #update branch

        delete13(conn) #delete customer
        delete14(conn) #delete car
        delete15(conn) #delete service
        delete16(conn) #delete sales
        delete17(conn) #delete rental
        delete18(conn) #delete branch
    
        compare(conn)
        listTop3car(conn)

    closeConnection(conn, database)

if __name__ == '__main__':
    main()