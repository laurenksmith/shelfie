import mysql.connector
from mysql.connector import Error


def create_connection():  # to connect to the database on MySQL
    try:
        connection = mysql.connector.connect(  # the user would insert their credentials here in order to connect
            host="localhost",
            user="root",  # to use, I shall replace with my actual credentials
            password="password",
            database="book_tracker"
        )
        if connection.is_connected():  # I want it to return a message to let me know if it has been successful
            print("Successfully connected to the database.")
            return connection
    except Error as e:  # I also want it to let me know if it hasn't worked, and why.
        print(f"Error: {e}")
        return None
