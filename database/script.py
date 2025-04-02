import mysql.connector
from mysql.connector import Error
from dotenv import dotenv_values


class DatabaseLibrary:
    def __init__(self):
        """
        Initializes a connection to the MySQL database.
        :param host: The host of the MySQL database (e.g. 'localhost').
        :param user: The username to connect to the database.
        :param password: The password for the username.
        :param database: The name of the database to connect to.
        """
        secrets= dotenv_values (".env")
        self.host = secrets["DB_HOST"]
        self.user = secrets["DB_USER"]
        self.password = secrets["DB_PASSWORD"]
        self.database = secrets["DB_NAME"]
        self.conn = None
        self.cursor = None
    
    def connect(self):
        """
        Connects to the MySQL database.
        """
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
                return f"Connected to MySQL database: {self.database}"
        except Error as e:
            self.connection= None
            return f"Error while connecting to MySQL: {e}"

    def close(self):
        """
        Closes the database connection.
        """
        if self.conn and self.conn.is_connected():
            self.conn.close()
            return "Database connection closed."
        
    def execute_query_create_update_delete(self, query):
        try:
            self.cursor.execute(query)
            self.conn.commit()
            return True, "Success"
        except Error as e:
            return False, e
    
    def execute_query_insert(self, query, values):
        try:
            self.cursor.execute(query, values)
            self.conn.commit()
            return True, "Success"
        except Error as e:
            return False, e
        
    def execute_query_select(self, query, params):
        try:
            self.cursor.execute(query, params)            
            return True, "Success"
        except Error as e:
            return False, e
    

    def create_table(self, table_name, columns):
        """
        Creates a table in the database.
        :param table_name: The name of the table to create.
        :param columns: A string representing the column definitions (e.g. 'id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100)').
        """
        
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});"
        res, message= self.execute_query_create_update_delete(query)
        if res:
            return f"Table {table_name} created successfully."
        else: 
            return f"Error creating table: {message}"

    def insert(self, table_name, columns, values):
        """
        Inserts data into a table.
        :param table_name: The name of the table.
        :param columns: A comma-separated string of column names (e.g. 'name, age').
        :param values: A tuple containing the values to insert (should match the number of columns).
        """
        placeholders = ", ".join(["%s"] * len(values))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        res, message= self.execute_query_insert( query, values)
        if res:
            message= "Data inserted successfully."
            status= True            
            return message,status
        else:       
            message= f"Error inserting data: {message}"
            status= False
            return message, status
        
    def query(self, query, params=()):
        """
        Executes a SELECT query and returns the results.
        :param query: The SELECT query string. SELECT all the rows from the table
        :param params: A tuple of parameters to substitute in the query.
        :return: A list of rows (tuples) from the query result.
        """
        res, message= self.execute_query_select( query, params )
        if res:
            return self.cursor.fetchall()
        else:
            return f"Error executing query: {message}"
        
    def query_specific_row(self, table_name, columns, where_conditions, params=()):
        """
        Executes a SELECT query and returns the results.
        :param query: The SELECT query string. SELECT specific columns for a specific where clause
        :param params: A tuple of parameters to substitute in the query.
        :return: A list of rows (tuples) from the query result.
        """
        query = f"SELECT {columns} FROM {table_name} WHERE {where_conditions};"
        res, message= self.execute_query_select(query, params)
        if res:
            return self.cursor.fetchall()
        else:
            return f"Error executing query: {message}"
            

    def update(self, table_name, set_columns, where_conditions):
        """
        Updates data in a table.
        :param table_name: The name of the table to update.
        :param set_columns: A string of the columns to update (e.g. "name = 'John'").
        :param where_conditions: A string for the WHERE clause (e.g. "id = 1").
        """
        query = f"UPDATE {table_name} SET {set_columns} WHERE {where_conditions};"
        res, message= self.execute_query_create_update_delete( query)
        if res:
            return "Data updated successfully."
        else:
            return f"Error updating data: {message}"

    def delete(self, table_name, where_conditions):
        """
        Deletes data from a table.
        :param table_name: The name of the table.
        :param where_conditions: The conditions to identify the rows to delete (e.g. "id = 1").
        """
        
        query = f"DELETE FROM {table_name} WHERE {where_conditions};"
        res, message= self.execute_query_create_update_delete( query)
        if res:    
            return "Data deleted successfully."
        else:
            return f"Error deleting data: {message}"
        



