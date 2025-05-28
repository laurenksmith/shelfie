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


# search for books by author name
def search_books_by_author(connection, author_name):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM books WHERE author LIKE %s;"
        cursor.execute(query, ('%' + author_name + '%',))
        rows = cursor.fetchall()

        if rows:
            print(f"\nBooks by '{author_name}':")
            for row in rows:
                print(row)
        else:
            print(f"No books found by '{author_name}'.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
