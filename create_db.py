
import mysql.connector
from mysql.connector import Error


# Connect to mysql through python
def create_server_connection(host_name, user_name, user_password):
    connections = None
    try:
        connections = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connections


pw = "Themainp1zza!"  # IMPORTANT! Put your MySQL Terminal password here.
db = "login_lc"  # This is the name of the database we will create in the next step - call it whatever you like.

connection = create_server_connection("localhost", "root", pw)


# create mysql database through python
def create_database(connections, query):
    cursor = connections.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


create_database_query = "CREATE DATABASE login_lc"
create_database(connection, create_database_query)


# connect to database
def create_db_connection(host_name, user_name, user_password, db_name):
    connections = None
    try:
        connections = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connections


# create query execute
def execute_query(connections, query):
    cursor = connections.cursor()
    try:
        cursor.execute(query)
        connections.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


# create tables
# Assign our SQL command to a python variable using triple quotes to create a multi-line string
create_users_table = """
CREATE TABLE users (
  id INT UNSIGNED NOT NULL auto_increment PRIMARY KEY,
  id_num VARCHAR(13) NOT NULL UNIQUE KEY,
  username VARCHAR(25) NOT NULL UNIQUE KEY,
  password VARCHAR(25) NOT NULL,
  name VARCHAR(25) NOT NULL,
  surname VARCHAR(25) NOT NULL,
  email VARCHAR(40) NOT NULL,
  cell VARCHAR(10) NOT NULL,
  role VARCHAR(8) NOT NULL
  );
 """


create_next_of_kin_table = """
CREATE TABLE next_of_kin (
  id INT UNSIGNED auto_increment NOT NULL,
  user_id VARCHAR(13) NOT NULL UNIQUE KEY,
  name VARCHAR(25) NOT NULL,
  surname VARCHAR(25) NOT NULL,
  cell VARCHAR(10) NOT NULL,
  PRIMARY KEY (id)
);
 """

create_login_table = """
CREATE TABLE login (
  id INT UNSIGNED auto_increment NOT NULL,
  username VARCHAR(25) NOT NULL,
  date_login DATE,
  login TIME,
  logout TIME,
  PRIMARY KEY (id)
);
 """

connection = create_db_connection("localhost", "root", pw, db)  # Connect to the Database
execute_query(connection, create_users_table)  # Execute our defined query
execute_query(connection, create_next_of_kin_table)
execute_query(connection, create_login_table)


alter_next_of_kin_table = """
ALTER TABLE next_of_kin
ADD FOREIGN KEY(user_id)
REFERENCES users(id_num);
"""

alter_login_table = """
ALTER TABLE login
ADD FOREIGN KEY(username)
REFERENCES users(username);
"""

execute_query(connection, alter_next_of_kin_table)
execute_query(connection, alter_login_table)
