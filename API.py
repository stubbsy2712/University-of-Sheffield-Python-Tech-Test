from flask import Flask, request, jsonify

app = Flask(__name__)

def get_customer(customer_id):
	# Code to retrieve customer data goes here
	return {"customer_id": customer_id, "name": "John Doe", "email": "john.doe@example.com"}

@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer_endpoint(customer_id):
	return jsonify(get_customer(customer_id))

if __name__ == "__main__":
	app.run(debug=True)