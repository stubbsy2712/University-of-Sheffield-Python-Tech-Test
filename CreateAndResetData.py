import sqlite3
connection = sqlite3.connect("db.sqlite")
cursor = connection.cursor()

def create_data():
	# Code to create data goes here
	print("Data created successfully.")

def cleanup_data():
	cursor.execute("`id`, `first_name`, `surname`, `email`, `status` ENUM('archived','active','suspended')")
	cursor.execute("""
    INSERT INTO `customer` VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)""")
	print("Data cleaned up successfully.")

if __name__ == "__main__":
	cleanup_data()
	create_data()