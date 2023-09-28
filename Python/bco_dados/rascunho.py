import os
os.system('cls')

import mysql.connector 
from mysql.connector import Error
import pandas as pd
pw = '12345678'

def create_db_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database='teste'
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

connection = create_db_connection("localhost", "root", "")

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

create_table_Aluno = """
CREATE TABLE Aluno(
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50),
    idade INT,
    Cpf VARCHAR(14),
    PRIMARY KEY (id)
)engine=InnoDB;
"""

connection = create_db_connection("localhost", "root", pw)
teste = execute_query(connection, create_table_Aluno)

