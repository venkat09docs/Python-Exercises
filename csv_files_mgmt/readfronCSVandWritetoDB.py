import csv

import mysql
from mysql.connector import Error

# Replace these with your MySQL credentials and database name
hostname = 'employee.c2vwtuzq6y0y.ap-southeast-1.rds.amazonaws.com'
username = 'admin'
password = 'Welcome123'
database = 'employeedb'

try:
    with open('employee_dict.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        rows = []
        for row in reader:
            print(f"{row['EmpName']} is located in {row['EmpAddress']}")
            rows.append(row.values())

    connection = mysql.connector.connect(
        host=hostname,
        user=username,
        password=password,
        database=database
    )

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)

        cursor = connection.cursor()

        insert_query = "INSERT INTO employee (empid, empname, empage, empaddress) VALUES (%s, %s, %s, %s)"
        print(rows)
        # Execute the insert query
        cursor.executemany(insert_query, rows)

        # Commit the transaction
        connection.commit()
        print("Records inserted successfully into employee")

        # Example query to fetch data
        cursor.execute("SELECT * FROM employee")
        records = cursor.fetchall()

        print("\nTotal rows in table:", cursor.rowcount)

        # Print each row
        for row in records:
            print(row)


except mysql.connector.Error as e:
    print("Error while connecting to MySQL", e)

finally:
    # Close database connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
