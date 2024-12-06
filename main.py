# pip install mysql-connector-python        Install library in your terminal

import mysql.connector
from mysql.connector import Error


"""
Create Database in your mysql workbench with following query.

CREATE DATABASE SalesDB;
USE SalesDB;
CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(100),
    Quantity INT,
    Price DECIMAL(10, 2),
    SaleDate DATE
);

"""
# Create functions connect with database

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='SalesDB'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

# This function create records
def create_record(connection, product_name, quantity, price, sale_date):
    cursor = connection.cursor()
    query = """
        INSERT INTO Sales (ProductName, Quantity, Price, SaleDate)
        VALUES (%s, %s, %s, %s);
    """
    data = (product_name, quantity, price, sale_date)
    cursor.execute(query, data)
    connection.commit()
    print(f"Record inserted: {cursor.rowcount} row(s) affected.")

# This function READ operation
def read_records(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM Sales;"
    cursor.execute(query)
    records = cursor.fetchall()
    print("Records in Sales table:")
    for record in records:
        print(record)

# This function UPDATE operation
def update_record(connection, sale_id, new_quantity):
    cursor = connection.cursor()
    query = """
        UPDATE Sales
        SET Quantity = %s
        WHERE SaleID = %s;
    """
    data = (new_quantity, sale_id)
    cursor.execute(query, data)
    connection.commit()
    print(f"Record updated: {cursor.rowcount} row(s) affected.")

# This function DELETE operation
def delete_record(connection, sale_id):
    cursor = connection.cursor()
    query = "DELETE FROM Sales WHERE SaleID = %s;"
    data = (sale_id,)
    cursor.execute(query, data)
    connection.commit()
    print(f"Record deleted: {cursor.rowcount} row(s) affected.")

# This is main function to create CRUD operations
def main():
    connection = connect_to_db()
    if connection:
        # Create operation
        create_record(connection, 'Laptop', 10, 750.00, '2024-11-01')
        create_record(connection, 'Mobile', 20, 250.00, '2024-11-02')

        # Read operation
        read_records(connection)

        # Update operation
        update_record(connection, 1, 15)  # Update Quantity for SaleID = 1

        # Read again to verify update
        read_records(connection)

        # Delete operation
        delete_record(connection, 2)  # Delete record with SaleID = 2

        # Read again to verify deletion
        read_records(connection)

        connection.close()
        print("MySQL connection closed.")

# If you want any changes and Uodate,delete then you can do that with below main1 function
def main1():
  connection = connect_to_db()
  if connection:
    read_records(connection)
    connection.close()
    print("MySQL connection closed.")

if __name__ == "__main__":
    main1()
