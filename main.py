import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="secret",
    database="mydatabase"
)

customers_table = """
CREATE TABLE customers(
    name VARCHAR(100),
    address VARCHAR(255)
)
"""
movie_table = """
CREATE TABLE movies(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    release_year YEAR(4),
    genre VARCHAR(100),
    collection_in_mil DECIMAL(4,1)
)
"""

mycursor = mydb.cursor()

mycursor.execute("SELECT id, name FROM customers")
myresult = mycursor.fetchone()
print(myresult)

# for result in myresult:
#     print(result)
