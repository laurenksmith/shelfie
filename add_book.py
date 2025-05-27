import mysql.connector
from mysql.connector import Error


# create a function in order for the user to be able to add a book to the database
def add_book(connection, title, author, genre, year_read, rating):
    print(f"Starting to add your book...")
    try:
        cursor = connection.cursor()
        insert_query = (
            "INSERT INTO books (title, author, genre, year_read, rating) "
            "VALUES (%s, %s, %s, %s, %s);"
        )
        data = (title, author, genre, year_read, rating)
        cursor.execute(insert_query, data)
        connection.commit()
        print(f"Success! Your book, '{title}', has been added. What book will capture your imagination next...?")
    except Error as e:
        print(f"Whoops! Something went wrong trying to add '{title}' to Shelfie. Please try again.\nError: {e}")
    finally:
        cursor.close()


# prompt for the user to add their book details
if __name__ == "__main__":
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Apple+91",
            database="book_tracker"
        )
        if connection.is_connected():
            print("Successfully connected to the database.")

            title = input("Enter the title of your book: ").strip()
            author = input("Enter the author of your book: ").strip()
            genre = input("Enter the genre of your book: ").strip()

            try:
                year_read = int(input("Enter the year you read it: "))
                rating = float(input("Enter your rating (out of 10): "))
            except ValueError:
                print("Invalid input for year or rating. Please enter numbers only.")
                connection.close()
                exit()

            # ✅ Now calling the function!
            add_book(connection, title, author, genre, year_read, rating)

    except Error as e:
        print(f"Connection error: {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print("Database connection closed.")