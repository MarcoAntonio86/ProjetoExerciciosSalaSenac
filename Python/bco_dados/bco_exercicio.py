
import os
os.system('cls')

import mysql.connector as mysql
#from mysql import Error
import pandas as pd


pw = '12345678'
def create_server_connection():
    connection = None
    try:
        connection = mysql.connect(
        host = 'localhost',
        user = 'root',
        passwd = '12345678',
        database = 'bco_dados'
        )
        print("MySQL Database connection successful")
    except mysql.Error as err:
        print(f"Error: '{err}'")
    return connection



connection = create_server_connection('localhost', 'root', pw, 'bco_dados')

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except mysql.Error as err:
        print(f"Error: '{err}'")


