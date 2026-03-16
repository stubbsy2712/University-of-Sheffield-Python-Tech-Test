TO RUN
- To instantiate and setup database (Task 1) `python .\CreateAndResetData.py`
- To run API (Task 2): Install flask if not already installed: `pip3 install flask`, then run with `python .\CreateAndResetData.py`. When run locally the endpoints are on port 5000 (of localhost), and consist of `/customers/{customer_id}` to see customer data, `/customers/{customer_id}/orders` to see data on the customers orders, and for the "full" endpoint with both requested in the task; `/customers/{customer_id}/full`
- To run ETL script (Task 3) `python .\ETLScript.py`

Chose SQLite for time and ease of setup, would have normally gone for MySQL in a larger, more "serious" project as it's very standard.
Flask is very well supported and was easy to setup.
Chose to write raw commands in the API instead of using an ORM because an ORM would have felt overkill for the scope of the exercise.

If this were a more "serious" API, MySQL would have been used, which would have necessitated a .env file which would then need to be gitignored, possibly an ORM too such as SQLAlchemy and Alembic.

Only one endpoint was specified in the task, however, being used to doing things the "RESTful" way, I preferred to have an endpoint for customer data, and a separate one for order data, I then created a "full" endpoint to do both. Perhaps a better URL than "full" could have been in order. This also explains the lack of a `JOIN` in the endpoint which might have been expected. It results not from an oversight, but takes advantage of the way the API is built.

Decided to add created and updated columns as its standard practice. However, it does not make sense for orders to be modified after being placed, therefore that table only has a created column.

The email addresses are invalid, this is deliberate as I don't want to accidentally type a real email address "testman@gmail.com" could very well belong to a real person. In actual practice these addresses should be validated, but the values should point to an internal controlled email address e.g. "test@sheffield.ac.uk".