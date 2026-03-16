import sqlite3
import os

def execute_sql():
	db_path = "./db.sqlite"
	sql_file = "./SetupAndAddTestData.sql"
	conn = sqlite3.connect(db_path)
	cursor = conn.cursor()
	if os.path.exists(sql_file):
		with open(sql_file, 'r') as f:
			sql_script = f.read()
			cursor.executescript(sql_script)
			conn.commit()

if __name__ == "__main__":
    execute_sql()