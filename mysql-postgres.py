import mysql.connector
import psycopg2
from psycopg2 import sql

# MySQL configuration
mysql_config = {
    'user': 'usr',
    'password': 'pwd',
    'host': 'ls-4b69d5e205fcb767c7071495e95c05c850d2790e.cfygi06885d9.ap-southeast-1.rds.amazonaws.com',
    'database': 'dbtest'
}

# PostgreSQL configuration
postgres_config = {
    'dbname': 'dbtestpostgres',
    'user': 'usr',
    'password': 'pwd',
    'host': 'ls-e9068b28bfe4b9e28ca3df20871843b604506fde.cfygi06885d9.ap-southeast-1.rds.amazonaws.com'
}

def fetch_mysql_data():
    """Fetch data from MySQL database."""
    connection = mysql.connector.connect(**mysql_config)
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM EMPLOYEES"  # Modify this as needed
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

def insert_data_into_postgres(data):
    """Insert data into PostgreSQL database."""
    connection = psycopg2.connect(**postgres_config)
    cursor = connection.cursor()

    # Assuming your PostgreSQL table schema matches the MySQL table schema
    insert_query = sql.SQL(
        "INSERT INTO Employees (id, f_name, l_name) VALUES (%s, %s, %s)"
    )  # Modify this as needed
    
    for row in data:
        values = tuple(row.values())
        cursor.execute(insert_query, values)
    
    connection.commit()
    cursor.close()
    connection.close()

def main():
    data = fetch_mysql_data()
    insert_data_into_postgres(data)
    print("Data migration completed successfully.")

if __name__ == "__main__":
    main()
