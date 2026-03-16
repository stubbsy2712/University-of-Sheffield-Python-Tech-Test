CREATE TABLE IF NOT EXISTS "customers" (
	"customer_id"	INTEGER NOT NULL,
	"first_name"	TEXT NOT NULL,
	"surname"	TEXT NOT NULL,
	"email"	TEXT NOT NULL UNIQUE,
	"status"	TEXT NOT NULL CHECK(status IN ('active','archived','suspended')),
    "created" DATETIME DEFAULT CURRENT_TIMESTAMP,
    "updated" DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("customer_id" AUTOINCREMENT)
);

INSERT OR IGNORE INTO "customers"
("customer_id", "first_name", "surname", "email", "status")
VALUES (1, 'Test', 'Customer', 'testemail1', 'active'),
(2, 'Second', 'Test', 'testemail2', 'archived'),
(3, 'Third', 'Person', 'testemail3', 'suspended');

CREATE TABLE IF NOT EXISTS "orders" (
	"order_id"	INTEGER NOT NULL,
	"customer_id"	INTEGER NOT NULL,
	"quantity"	INTEGER NOT NULL,
	"product_name"	TEXT NOT NULL,
	"unit_price"	INTEGER NOT NULL,
    "created" DATETIME DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY("customer_id") REFERENCES "customers"("customer_id"),
	PRIMARY KEY("order_id" AUTOINCREMENT)
);

INSERT OR IGNORE INTO "orders"
("order_id", "customer_id", "quantity", "product_name", "unit_price")
VALUES (1, 1, 1, 'product 1', 10),
(2, 1, 4, 'screws', 25),
(3, 1, 5, 'misc', 5),
(4, 2, 2, 'screws', 25);

DROP TRIGGER IF EXISTS update_customers_updated;
CREATE TRIGGER update_customers_updated
AFTER UPDATE ON customers
FOR EACH ROW
BEGIN
    UPDATE customers
    SET updated = CURRENT_TIMESTAMP
    WHERE id = OLD.id;
END;