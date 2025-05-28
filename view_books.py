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


# Adding a function to allow the user to delete an entry
def delete_book_by_title(connection, title):
    try:
        cursor = connection.cursor()

        # Step 1: Find the book
        search_query = "SELECT id, title, author FROM books WHERE title = %s;"
        cursor.execute(search_query, (title,))
        book = cursor.fetchone()

        if not book:
            print(f"No book found with the title '{title}'.")
            return

        # Step 2: Ask for confirmation
        book_id, found_title, author = book
        confirm = input(f"Are you sure you want to delete '{found_title}' by {author}? (Y/N): ").strip().lower()

        if confirm == 'y':
            delete_query = "DELETE FROM books WHERE id = %s;"
            cursor.execute(delete_query, (book_id,))
            connection.commit()
            print(f"'{found_title}' by {author} has been deleted.")
        else:
            print("Deletion cancelled.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


# Prompts the user to view all their saved books or books by a specific author or delete a book.
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





