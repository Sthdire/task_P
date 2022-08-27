import psycopg2
from psycopg2 import OperationalError, sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

db_password = 'rEtyuol44'


def create_database(name_Database, password):
    connect = psycopg2.connect(dbname='postgres',
                               user='postgres',
                               host='localhost',
                               password=password)

    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    try:
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(name_Database)))
        print('successfully created database')
    except:
        print('Database already exists')
    pass


create_database('t_db', db_password)

con = psycopg2.connect(
    database="t_db",
    user="postgres",
    password=db_password,
    host="localhost",
    port="5432"
)
cur = con.cursor()


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


create_mailingList_table = """
CREATE TABLE IF NOT EXISTS mailing_list (
  id_send SERIAL PRIMARY KEY,
  ml_name text,
  message text,
  date_time_start text, 
  phone_N text,
  date_time_close text,
)
"""
create_client_table = """
CREATE TABLE IF NOT EXISTS client (
  id_client SERIAL PRIMARY KEY,
  phone_N text,
  timezone text
)
"""
create_message_table = """
CREATE TABLE IF NOT EXISTS message (
  id_message SERIAL PRIMARY KEY,
  date_time_create text, 
  status text,
  ml_name text,
  phone_n text,
  message text
)
"""

execute_query(con, create_mailingList_table)
execute_query(con, create_client_table)
execute_query(con, create_message_table)
