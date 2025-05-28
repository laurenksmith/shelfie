import mysql.connector
from mysql.connector import Error


# A function to view all books
def view_all_books(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books;")
        rows = cursor.fetchall()

        if rows:
            print("\nAll Books in Shelfie:")
            for row in rows:
                print(row)

        else:
            print("\nNo Books found.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

