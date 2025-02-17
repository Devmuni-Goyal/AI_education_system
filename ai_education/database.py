import mysql.connector
from mysql.connector import Error
import logging

# Set up logging configuration
logging.basicConfig(filename='app.log', level=logging.ERROR)

def get_db_connection():
    """
    Function to connect to MySQL database and return the connection object.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="your_db_user",        # Update with your MySQL user
            password="your_db_password", # Update with your MySQL password
            database="ai_education_db"   # Ensure this is the correct database name
        )
        if connection.is_connected():
            print("Connected to the database")
            return connection
    except Error as e:
        logging.error(f"Error while connecting to MySQL: {e}")
        return None

def fetch_user_data(user_id: int):
    """
    Function to fetch user data from the database based on user ID.
    """
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            cursor.close()
            connection.close()
            return result
        except Error as e:
            logging.error(f"Error fetching user data: {e}")
            return None
    return None

def store_chatbot_log(user_id: int, user_query: str, chatbot_response: str):
    """
    Function to store the chatbot query and response in the database.
    """
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO chatbot_logs (user_id, user_query, chatbot_response) VALUES (%s, %s, %s)"
            cursor.execute(query, (user_id, user_query, chatbot_response))
            connection.commit()
            cursor.close()
            connection.close()
            print("Chatbot log stored successfully")
        except Error as e:
            logging.error(f"Error storing chatbot log: {e}")

def search_database(query: str):
    """
    Function to search the database for specific content related to the query.
    """
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query_str = f"SELECT * FROM resources WHERE title LIKE %s OR description LIKE %s"
            cursor.execute(query_str, ('%' + query + '%', '%' + query + '%'))
            results = cursor.fetchall()
            cursor.close()
            connection.close()
            return results
        except Error as e:
            logging.error(f"Error searching database: {e}")
            return None
    return None
