import mysql.connector

from mysql.connector import Error

import pandas as pd

 

def create_db_connection(host_name, user_name, user_password, db_name):

    connection = None

    try:

        connection = mysql.connector.connect(

            host=host_name,

            user=user_name,

            passwd=user_password,

            database=db_name

        )

        print("MySQL Database connection successful")

    except Error as err:

        print(f"Error: '{err}'")

 

    return connection

 

connection = create_db_connection("localhost", "root", "", "alunos")

 

def execute_query(connection, query):

    cursor = connection.cursor()

    try:

        cursor.execute(query)

        connection.commit()

        print("Query successful")

    except Error as err:

        print(f"Error: '{err}'")

 

def read_query(connection, query):

    cursor = connection.cursor()

    result = None

    try:

        cursor.execute(query)

        result = cursor.fetchall()

        return result

    except Error as err:

        print(f"Error: '{err}'")

 

 

comando_select = """

select * from produtos;

"""

 

comandos_alter = str(input("Digite o comando: "))

 

executar_comando = execute_query(connection, comandos_alter)

 

executar_comando_02 = read_query(connection, comando_select)

 

for linhas in executar_comando_02:

  print(linhas)