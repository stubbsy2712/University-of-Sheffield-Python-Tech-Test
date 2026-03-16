## How to Run

### To instantiate and setup database (Task 1):
- `python .\CreateAndResetData.py`

### To run API (Task 2):
- To run API (Task 2): Install flask if not already installed: `pip3 install flask`
- `python .\API.py`.
- When run locally the endpoints are on port 5000 (of localhost), and consist of:
- `/customers/{customer_id}` to see customer data
- `/customers/{customer_id}/orders` to see data on the customers orders
- for the "full" endpoint with both requested in the task; `/customers/{customer_id}/full`

### To run ETL script (Task 3)
- `python .\ETLScript.py`

## Choices and Reasoning

### Tech choices:
- I Chose SQLite for the database for ease of setup. I would have normally gone for MySQL in a larger, more "serious" project as it's very standard, and these are the 2 databases I'm most familiar with.
- I chose Flask for the API very well supported and was easy to setup.
- I Chose to write raw SQLite commands in the API instead of using an ORM because an ORM would have felt overkill for the scope of the exercise.

### Programming choices:
Only one endpoint was specified in the task, however, being used to doing things the "RESTful" way, I preferred to have an endpoint for customer data, and a separate one for order data, I then created a "full" endpoint to do both. This also explains the lack of a `JOIN` in the endpoint. You may have been expecting a `JOIN`, the lack of one results not from an oversight, but takes advantage of the way the rest of the API is built.

I Decided to add `created` and `updated` columns to the tables as that's standard practice. However, it does not make sense for orders to be modified after being placed, therefore that table only has a created column.

The email addresses used in the table are invalid, this is deliberate as I don't want to accidentally type a real email address "testuser@gmail.com" could very well belong to a real person. In actual practice these addresses should be validated, but the values should point to an internal controlled email address e.g. "test@sheffield.ac.uk".

## Application Flow
- The data is defined in the sql script `SetupAndAddTestData.sql`
- Upon running the script requested in task 1, `CreateAndResetData`, the (SQLite) database is instantiated if it does not already exist, the tables are then created and populated. The `created` and `updated` columns are set to fill automatically. The SQL file makes use of `INSERT OR IGNORE` and `CREATE TABLE IF NOT EXISTS` in order to not create duplicates.
- The API runs SQLite commands to retrieve data from the database, and then transfers it via HTTP to a browser or other client
- The ETL script extracts data from the database via similar commands, transforms it into a table of orders alongside customer details and exports it to a CSV file (which results in repeated data in said file, however, the assumption is that this CSV is to be read by a human so the repeated data may be preferred, depending on use).

## Potential improvements
- If this were a more "serious" API, MySQL would have been used as opposed to SQLite, which would have necessitated a .env file which would then need to be gitignored, possibly an ORM too such as SQLAlchemy and Alembic.
- Perhaps a better URL than "/full" could have been used for the requested endpoint in Task 2.
- In a bigger project email addresses should be validated, but also accessible test email addresses should be provisioned to be used there.