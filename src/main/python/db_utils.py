import mysql.connector
from mysql.connector import Error
from datetime import datetime
from db_config import DB_CONFIG, STORE_TABLES

class DatabaseManager:
    def __init__(self, host=DB_CONFIG['host'], user=DB_CONFIG['user'], 
                 password=DB_CONFIG['password'], database=DB_CONFIG['database']):
        #create a new user in mysql 
        #create a new database
        #create a new table
        #insert data into the table
        #get the data from the table
        #close the connection

        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.tables = STORE_TABLES

    def connect(self):
        try:
            if self.connection and self.connection.is_connected():
                return self.connection
                
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print(f"Successfully connected to MySQL database '{self.database}'")
            return self.connection
        except Error as e:
            print(f"Error connecting to MySQL Database: {e}")
            print("\nTroubleshooting steps:")
            print("1. Make sure MySQL server is running")
            print("2. Verify the user 'pricewatch_user' exists and has proper permissions")
            print("3. Check if the password is correct")
            print("4. Ensure the database 'pricewatchdby' exists")
            return None

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            self.connection = None
            print("Database connection closed")

    def create_table_if_not_exists(self, table_name, columns):
        """
        Create a table if it doesn't exist
        columns: list of tuples (column_name, column_type)
        """
        if not self.connection:
            if not self.connect():
                print("Cannot create table: No database connection")
                return False
        
        try:
            cursor = self.connection.cursor()
            
            # Create the table definition
            columns_def = ", ".join([f"{col[0]} {col[1]}" for col in columns])
            create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id BIGINT AUTO_INCREMENT PRIMARY KEY,
                {columns_def}
            )
            """
            
            cursor.execute(create_table_query)
            self.connection.commit()
            print(f"Table {table_name} is ready")
            return True
            
        except Error as e:
            print(f"Error creating table {table_name}: {e}")
            return False
        finally:
            if 'cursor' in locals():
                cursor.close()

    def insert_products(self, table_name, products):
        """
        Insert products into the specified table
        products: list of tuples (product_name, price, date, store)
        """
        if not self.connection:
            self.connect()
        
        try:
            cursor = self.connection.cursor()
            
            # Insert products
            insert_query = f"""
            INSERT INTO {table_name} (product_name, price, date, store)
            VALUES (%s, %s, %s, %s)
            """
            
            for product in products:
                try:
                    price = float(product[1].replace(',', ''))
                    cursor.execute(insert_query, (product[0], price, product[2], product[3]))
                except ValueError as e:
                    print(f"Error converting price for {product[0]}: {e}")
                    continue
            
            self.connection.commit()
            print(f"Successfully inserted {len(products)} products into {table_name}")
            
        except Error as e:
            print(f"Error inserting data into {table_name}: {e}")
        finally:
            cursor.close()

  
# Example usage:
if __name__ == "__main__":
    # Initialize database manager
    db = DatabaseManager()
    
    # Define table columns
    columns = [
        ("product_name", "VARCHAR(255)"),
        ("price", "DECIMAL(10,2)"),
        ("date", "DATE"),
        ("store", "VARCHAR(50)")
    ]
    
    # Create tables for different stores
    for store, table in db.tables.items():
        db.create_table_if_not_exists(table, columns)
    
    # Example: Insert test data
    test_products = [
        ("Milk", "3.99", datetime.now().date(), "CVS"),
        ("Milk", "3.49", datetime.now().date(), "Walmart"),
        ("Milk", "4.29", datetime.now().date(), "RiteAid")
    ]
    
    # Insert into each store's table
    for store, table in db.tables.items():
        store_products = [(p[0], p[1], p[2], store) for p in test_products]
        db.insert_products(table, store_products)
    
    # Close the connection
    db.close() 