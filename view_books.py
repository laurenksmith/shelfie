import mysql.connector
from mysql.connector import Error
import db_connect


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


# Prompts the user to view all their saved books or books by a specific author
if __name__ == "__main__":
    connection = db_connect.create_connection()
    if connection:
        try:
            print("\nWhat would you like to do?")
            print("1. View all books")
            print("2. Search books by author")
            print("3. Delete a book")
            choice = input("Enter your choice (1, 2 or 3): ").strip()

            if choice == '1':
                view_all_books(connection)
            elif choice == '2':
                author = input("Enter the author's name to search: ").strip()
                search_books_by_author(connection, author)
            elif choice == '3':
                title = input("Enter the name of the book to delete: ").strip()
                delete_book_by_title(connection, title)
            else:
                print("Invalid choice.")

        except Error as e:
            print(f"Connection error: {e}")
        finally:
            if connection:
                connection.close()
                print("Database connection closed.")


# Adding a function to allow the user to delete an entry
def delete_book_by_title(connection, title):
    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM books WHERE title = %s;"
        cursor.execute(delete_query, (title,))
        connection.commit()
        if cursor.rowcount > 0:
            print(f"Book with the title '{title}' deleted successfully!")
        else:
            print(f"No book found with the title '{title}'.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

