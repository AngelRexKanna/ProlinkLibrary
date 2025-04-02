from script import DatabaseLibrary
#from dotenv import dotenv_values

#secrets= dotenv_values (".env")
# Create an instance of the library
db = DatabaseLibrary()

# Connect to the database
db.connect()

# Create a table
db.create_table("users", "id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), age INT")

# Insert some data
message, status = db.insert("users", "name, age", ("John Doe", 30))
if status:
    print (message)
else:
    print (message)

db.insert("users", "name, age", ("Jane Smith", 25))
if status:
    print (message)
else:
    print (message)
# Query the data
results = db.query_specific_row("users", "name,age", "id = 2")
print("All users:", results)

# Update data
db.update("users", "age = 31", "id = 1")
if status:
    print (message)
else:
    print (message)

# Query the data again
updated_results = db.query("SELECT * FROM users")
print("Updated users:", updated_results)

# Delete data
db.delete("users", "id = 2")
if status:
    print (message)
else:
    print (message)

# Query again after deletion
final_results = db.query("SELECT * FROM users")
print("Final users:", final_results)

# Close the connection
db.close()
