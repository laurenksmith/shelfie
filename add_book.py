import mysql.connector
from mysql.connector import Error


# create a function in order for the user to be able to add a book to the database
def add_book(connection, title, author, genre, year_read, rating):
    try:
        cursor = connection.cursor()  # this allows me to execute SQL commands in Python
        insert_query = (
            "INSERT INTO books (title, author, genre, year_read, rating) "
            "VALUES (%s, %s, %s, %s, %s);"
        )
        data = (title, author, genre, year_read, rating)
        cursor.execute(insert_query, data)
        connection.commit()  # this ensures that the changes are saved to the database
        print(f"Success! Your book, {title} has been added. What book will capture your imagination next...?")
    except Error as e:  # error handling
        print(f"Whoops! Something went wrong trying to add {title} to Shelfie. Please try again.")
    finally:
        cursor.close()  # to close the connection to the database


# add a prompt for the user to add their book details
if __name__ == "__main__":
    try:
        connection = mysql.connector.connect(
            host="host",
            user="user",  # to use, I shall replace with my actual credentials
            password="password",
            database="book_tracker"
        )
        if connection.is_connected():  # I want it to return a message to let me know if it has been successful
            print("Successfully connected to the database.")

        title = input("Enter the title of your book: ").strip()
        author = input("Enter the author of your book: ").strip()
        genre = input("Enter the genre of your book: ").strip()
        try:
            year_read = int(input("Enter the year you read it: "))
            rating = float(input("Enter your rating (out of 10): "))
        except ValueError:
            print("Invalid input for year or rating. Please enter numbers only.")
            exit()

    except Error as e:
        print(f"Connection error: {e}")

    finally:
        if connection:
            connection.close()
            print("Database connection closed.")
