# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 20:30:10 2019

@author: SANIYA
"""

import mysql.connector
from mysql.connector import Error
import petl as etl
try: 
    connection = mysql.connector.connect(host='localhost',database='prachi',user='root',password='root',buffered=True) 
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL database... MySQL Server version on ",db_Info)
        cursor = connection.cursor(buffered=True,dictionary=True)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print ("Your connected to - ", record)
        customer = etl.fromdb(connection, 'SELECT * FROM customer')
        product = etl.fromdb(connection, 'SELECT * FROM product')
        transaction = etl.fromdb(connection, 'SELECT * FROM transaction')
        date = etl.fromdb(connection, 'SELECT * FROM date')
        fact = etl.fromdb(connection, 'SELECT * FROM fact')

        print("CUSTOMER TABLE:")
        print(customer)
        print("PRODUCT TABLE:")
        print(product)
        print("TRANSACTION TABLE:")
        print(transaction)
        print("DATE TABLE:")
        print(date)
        print("FACT TABLE:")
        print(fact)
        
        #OLAP ----> MIN & MAX
        mins, maxs = etl.limits(fact, 'sales')
        print( "Minimum Sales:",mins)
        print("Maximum Sales:",maxs)
        
        #OLAP ---> PIVOT
        table1 = etl.pivot(product, 'category', 'subcategory','quantity', sum)
        print("PIVOT:")
        print(table1)
        
        
        #OLAP OPERATIONS ---> ROLL UP
        table2 = etl.aggregate(customer, 'state', len)
        table3 = etl.aggregate(customer, 'city', len) 
        print("ROLL UP:")
        print(table2)
        print(table3)
        
        #OLAP OPERATIONS ---> SLICING
        print("SLICING:")
        table4= etl.rowslice(table3,3)
        print(table4)
        
        
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
#closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")