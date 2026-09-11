CREATE DATABASE IF NOT EXISTS shopscale;

USE shopscale;

-- Products table
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    price DECIMAL(10,2) NOT NULL
);

-- Cart table
CREATE TABLE IF NOT EXISTS carts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Seed products
INSERT INTO products (name, category, price) VALUES
('Wireless Keyboard', 'Electronics', 1299.00),
('Wireless Mouse', 'Electronics', 799.00),
('USB-C Charger', 'Electronics', 999.00),
('Bluetooth Speaker', 'Electronics', 1499.00),
('Noise Cancelling Headphones', 'Electronics', 2999.00),
('Smart Watch', 'Electronics', 3999.00),

('Coffee Maker', 'Home', 2499.00),
('Electric Kettle', 'Home', 1299.00),
('LED Desk Lamp', 'Home', 899.00),
('Water Bottle', 'Home', 499.00),
('Air Fryer', 'Home', 5499.00),
('Vacuum Cleaner', 'Home', 6999.00),

('Running Shoes', 'Fitness', 2499.00),
('Yoga Mat', 'Fitness', 799.00),
('Dumbbell Set', 'Fitness', 1999.00),
('Resistance Bands', 'Fitness', 699.00),
('Gym Gloves', 'Fitness', 499.00),
('Fitness Tracker', 'Fitness', 1999.00),

('Cotton T-Shirt', 'Clothing', 599.00),
('Hoodie', 'Clothing', 1499.00),
('Denim Jeans', 'Clothing', 1999.00),
('Sports Jacket', 'Clothing', 2499.00),
('Casual Shirt', 'Clothing', 999.00),
('Track Pants', 'Clothing', 899.00);

-- Verify number of products
SELECT COUNT(*) AS total_products FROM products;
