# SalesDB CRUD Operations with Python and MySQL

This project provides a practical example of performing CRUD (Create, Read, Update, Delete) operations on a MySQL database table using Python. The `mysql-connector-python` library is used to connect and interact with the database. This repository demonstrates how to handle database connections, execute queries, and manage data efficiently.

---

## Overview

This project is centered around a hypothetical `SalesDB` database containing a `Sales` table. The script allows you to manage sales records, including products, their quantities, prices, and sale dates. By running the provided Python script, you can:
- Insert new records into the `Sales` table.
- Retrieve and display all records.
- Update existing records by their unique `SaleID`.
- Delete records from the table.

---

## Features

- **Database Connectivity:** Easy and secure connection to a MySQL database.
- **CRUD Operations:** Comprehensive functions to manage table records.
- **Dynamic Interaction:** SQL queries use placeholders to avoid SQL injection.
- **Ease of Use:** Simple and clean Python functions for each operation.

---

## Database Setup

Run these SQL commands to set up the database and table:

```sql
CREATE DATABASE SalesDB;
USE SalesDB;
CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(100),
    Quantity INT,
    Price DECIMAL(10, 2),
    SaleDate DATE
);

## How to Run

1. Make sure your MySQL server is running, and the `SalesDB` database is created.
2. Run the Python script:
   ```bash
   python script_name.py

