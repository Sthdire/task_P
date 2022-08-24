import psycopg2
from psycopg2 import OperationalError

con = psycopg2.connect(
    database="t_db",
    user="postgres",
    password="rEtyuol44",
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
  message text,
  date_time_start DATE, 
  phone_N INTEGER,
  date_time_close DATE,
  id_message INTEGER
)
"""
create_client_table = """
CREATE TABLE IF NOT EXISTS client (
  id_client SERIAL PRIMARY KEY,
  phone_N INTEGER,
  timezone text
)
"""
create_message_table = """
CREATE TABLE IF NOT EXISTS message (
  id_message SERIAL PRIMARY KEY,
  date_time_create DATE, 
  status text,
  id_send INTEGER,
  id_client INTEGER,
  message text
)
"""

execute_query(con, create_mailingList_table)
execute_query(con, create_client_table)
execute_query(con, create_message_table)
