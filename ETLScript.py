import csv
import sqlite3
import os
connection = sqlite3.connect("db.sqlite")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute("""SELECT `orders`.`order_id`, `orders`.`customer_id`, `orders`.`quantity`, `orders`.`product_name`, `orders`.`product_name`, `orders`.`unit_price`, `orders`.`quantity`, `orders`.`created`, `customers`.`first_name`, `customers`.`surname`, `customers`.`email`
FROM `orders` INNER JOIN `customers` ON `customers`.`customer_id` = `orders`.`customer_id`
WHERE `customers`.`status` = 'active';""")

orders = cursor.fetchall()
ordersDict = [dict(row) for row in orders]
orders_formatted = []

for order in ordersDict:
	formatted_order = {}
	formatted_order['customer id'] = order['customer_id']
	formatted_order['order id'] = order['order_id']
	formatted_order['customer name'] = order['first_name'] + " " + order['surname']
	formatted_order['customer email'] = order['email']
	formatted_order['product name'] = order['product_name']
	formatted_order['order quantity'] = order['quantity']
	formatted_order['unit price'] = order['unit_price']
	formatted_order['order total price'] = order['quantity'] * order['unit_price']
	formatted_order['order time'] = order['created']
	orders_formatted.append(formatted_order)

folder_path = "orders"
file_path = os.path.join(folder_path, "orders.csv")
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

with open(os.path.join("orders", "orders.csv"), mode='w', newline='') as output_file:
	writer = csv.DictWriter(output_file, fieldnames=["order id", "customer id", "customer name", "customer email", "product name", "order quantity", "unit price",
										   "order total price", "order time"])
	writer.writeheader()
	for order in orders_formatted:
		writer.writerow(order)