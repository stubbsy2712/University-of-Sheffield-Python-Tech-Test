from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def db_connection():
	connection = sqlite3.connect("db.sqlite")
	connection.row_factory = sqlite3.Row
	return connection.cursor()

def get_customer(customer_id, cursor):
	cursor.execute("SELECT * FROM `customers` WHERE `customer_id` = ?", (customer_id,))
	customer_data = cursor.fetchone()
	return customer_data

def get_orders_for_customer(customer_id, cursor):
	cursor.execute("SELECT * FROM `orders` WHERE `customer_id` = ?", (customer_id,))
	orders = cursor.fetchall()
	return orders

def get_customer_and_order_data(customer_id, cursor):
	customer_data = get_customer(customer_id, cursor)
	all_customer_orders = get_orders_for_customer(customer_id, cursor)
	customer_and_orders_object = {
		"customer" : dict(customer_data) if customer_data else None,
		"orders" : [dict(row) for row in all_customer_orders] if all_customer_orders else None
	}
	return customer_and_orders_object

@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer_endpoint(customer_id):
	customer_data = get_customer(customer_id, db_connection())
	return jsonify(dict(customer_data)) if customer_data else jsonify(None)

@app.route('/customers/<int:customer_id>/orders', methods=['GET'])
def get_orders_for_customer_endpoint(customer_id):
	order_data = get_orders_for_customer(customer_id, db_connection())
	return jsonify([dict(row) for row in order_data]) if order_data else jsonify(None)

@app.route('/customers/<int:customer_id>/full', methods=['GET'])
def get_customer_with_orders_endpoint(customer_id):
	return jsonify(get_customer_and_order_data(customer_id, db_connection()))

if __name__ == "__main__":
	app.run(debug=True)