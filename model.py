import tensorflow as tf
import mysql.connector

# Initialize the LLM model (assuming you have pretrained it)
llm_model = tf.saved_model.load(r'C:\Users\Smile\web-crawler\env')

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="2345",
    database="DA"
)
db_cursor = db_connection.cursor()

# Receive user input (assuming it's stored in the variable user_input)
user_input = input("Enter your search query: ")

# Use LLM to convert user input into a refined search query
refined_query = llm_model(user_input)

# Construct SQL query based on the refined query
sql_query = f"SELECT * FROM businesses WHERE description LIKE '%{refined_query}%'"

# Execute SQL query
db_cursor.execute(sql_query)

# Fetch results
results = db_cursor.fetchall()

# Display results
for row in results:
    print(row)
