# import mysql.connector
# from mysql.connector import Error
# import logging

# # Set up logging configuration to log errors
# logging.basicConfig(filename='app.log', level=logging.ERROR)




import logging

# Set up logging configuration to log errors
logging.basicConfig(filename='app.log', level=logging.ERROR)

# Simulated database using a dictionary
fake_db = {
    'users': {
        1: {'id': 1, 'name': 'John Doe', 'email': 'johndoe@example.com'},
        2: {'id': 2, 'name': 'Jane Smith', 'email': 'janesmith@example.com'}
    },
    'chatbot_logs': [],
    'resources': [
        {'title': 'Python Basics', 'description': 'A beginner\'s guide to Python programming.'},
        {'title': 'Machine Learning 101', 'description': 'An introduction to machine learning.'}
    ]
}

def fetch_user_data(user_id: int):
    """
    Function to fetch user data from the simulated database based on user ID.
    """
    try:
        user = fake_db['users'].get(user_id)
        if user:
            return user
        else:
            raise ValueError(f"User with ID {user_id} not found.")
    except Exception as e:
        logging.error(f"Error fetching user data: {e}")
        return None

def store_chatbot_log(user_id: int, user_query: str, chatbot_response: str):
    """
    Function to store the chatbot query and response in the simulated database.
    """
    try:
        log = {'user_id': user_id, 'user_query': user_query, 'chatbot_response': chatbot_response}
        fake_db['chatbot_logs'].append(log)
        print("Chatbot log stored successfully")
    except Exception as e:
        logging.error(f"Error storing chatbot log: {e}")

def search_database(query: str):
    """
    Function to search the simulated database for specific content related to the query.
    """
    try:
        results = []
        for resource in fake_db['resources']:
            if query.lower() in resource['title'].lower() or query.lower() in resource['description'].lower():
                results.append(resource)
        return results
    except Exception as e:
        logging.error(f"Error searching simulated database: {e}")
        return None













# def get_db_connection():
#     """
#     Function to connect to MySQL database and return the connection object.
#     """
#     try:
#         # Establishing connection to the database
#         # connection = mysql.connector.connect(
#         #     host="localhost",               # Host where MySQL server is running
#         #     user="your_db_user",            # Replace with your MySQL username
#         #     password="your_db_password",    # Replace with your MySQL password
#         #     database="ai_education_db"      # Ensure you have the correct database name
#         # )
        
#         # Check if the connection is successful
#         # if connection.is_connected():
#         #     print("Connected to the database")
#         #     return connection
#     except Error as e:
#         # Log error if the connection fails
#         logging.error(f"Error while connecting to MySQL: {e}")
#         return None

# def fetch_user_data(user_id: int):
#     """
#     Function to fetch user data from the database based on user ID.
#     """
#     # connection = get_db_connection()
#     # if connection:
#         try:
#             # cursor = connection.cursor(dictionary=True)  # Use dictionary cursor for named column access
#             # query = "SELECT * FROM users WHERE id = %s"  # SQL query to fetch user by ID
#             # cursor.execute(query, (user_id,))  # Execute the query with the provided user_id
#             # result = cursor.fetchone()  # Fetch single result
#             # cursor.close()  # Close the cursor
#             # connection.close()  # Close the database connection
#             # return result  # Return the fetched result
#         except Error as e:
#             # Log error if there's an issue fetching user data
#             logging.error(f"Error fetching user data: {e}")
#             return None
#     return None

# def store_chatbot_log(user_id: int, user_query: str, chatbot_response: str):
#     """
#     Function to store the chatbot query and response in the database.
#     """
#     # connection = get_db_connection()
#     # if connection:
#         try:
#             # cursor = connection.cursor()  # Create a cursor for execution
#             # query = "INSERT INTO chatbot_logs (user_id, user_query, chatbot_response) VALUES (%s, %s, %s)"  # SQL query to insert log
#             # cursor.execute(query, (user_id, user_query, chatbot_response))  # Execute insertion
#             # connection.commit()  # Commit the transaction
#             # cursor.close()  # Close the cursor
#             # connection.close()  # Close the connection
#             # print("Chatbot log stored successfully")  # Confirm successful insertion
#         except Error as e:
#             # Log error if there's an issue storing the log
#             logging.error(f"Error storing chatbot log: {e}")

# def search_database(query: str):
#     """
#     Function to search the database for specific content related to the query.
#     """
#     # connection = get_db_connection()
#     # if connection:
#         try:
#             # cursor = connection.cursor(dictionary=True)  # Use dictionary cursor for named column access
#             # query_str = f"SELECT * FROM resources WHERE title LIKE %s OR description LIKE %s"  # SQL query to search resources
#             # cursor.execute(query_str, ('%' + query + '%', '%' + query + '%'))  # Execute the query with the search term
#             # results = cursor.fetchall()  # Fetch all matching results
#             # cursor.close()  # Close the cursor
#             # connection.close()  # Close the connection
#             # return results  # Return the results of the search
#         except Error as e:
#             # Log error if there's an issue searching the database
#             logging.error(f"Error searching database: {e}")
#             return None
#     return None
