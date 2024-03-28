-- use utibu database
USE utibu_db;


-- customers table
CREATE TABLE customers
(
    customer_id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone_number VARCHAR(20),
    address VARCHAR(255)
);

-- medications table
CREATE TABLE medications
(
    medication_id INT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    stock_level INT,
    price DECIMAL(10, 2)
);

-- orders table
CREATE TABLE orders
(
    order_id INT PRIMARY KEY,
    customer_id INT,
    medication_id INT,
    quantity INT,
    order_date DATE,
    status VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (medication_id) REFERENCES medications(medication_id)
);

-- sales table
CREATE TABLE sales
(
    sale_id INT PRIMARY KEY,
    order_id INT,
    total_amount DECIMAL(10, 2),
    payment_status VARCHAR(50),
    sale_date DATE,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- invoices table
CREATE TABLE invoices
(
    invoice_id INT PRIMARY KEY,
    sale_id INT,
    invoice_number VARCHAR(50),
    invoice_date DATE,
    FOREIGN KEY (sale_id) REFERENCES sales(sale_id)
);

-- payments table
CREATE TABLE payments
(
    payment_id INT PRIMARY KEY,
    sale_id INT,
    amount DECIMAL(10, 2),
    payment_date DATE,
    FOREIGN KEY (sale_id) REFERENCES sales(sale_id)
);

-- statements table
CREATE TABLE statements
(
    statement_id INT PRIMARY KEY,
    customer_id INT,
    statement_date DATE,
    balance DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- inventory table
CREATE TABLE inventory
(
    inventory_id INT PRIMARY KEY,
    medication_id INT,
    stock_level INT,
    last_updated DATE,
    FOREIGN KEY (medication_id) REFERENCES medications(medication_id)
);