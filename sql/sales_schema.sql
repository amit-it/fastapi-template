CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS subcategories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS regions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS segments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS brands (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS skus (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS sales_fact (
    id INT AUTO_INCREMENT PRIMARY KEY,
    week_start DATE NOT NULL,
    category_id INT NOT NULL,
    subcategory_id INT NOT NULL,
    region_id INT NOT NULL,
    segment_id INT NOT NULL,
    brand_id INT NOT NULL,
    sku_id INT NOT NULL,
    units_sold INT NOT NULL,
    price DECIMAL(12,2) NOT NULL,
    discount DECIMAL(5,2) NOT NULL,
    revenue DECIMAL(14,2) NOT NULL,
    cost DECIMAL(14,2) NOT NULL,
    profit DECIMAL(14,2) NOT NULL,
    INDEX idx_sales_week (week_start),
    INDEX idx_sales_category (category_id),
    INDEX idx_sales_subcategory (subcategory_id),
    INDEX idx_sales_region (region_id),
    INDEX idx_sales_segment (segment_id),
    INDEX idx_sales_brand (brand_id),
    INDEX idx_sales_sku (sku_id),
    CONSTRAINT fk_sales_category FOREIGN KEY (category_id) REFERENCES categories(id),
    CONSTRAINT fk_sales_subcategory FOREIGN KEY (subcategory_id) REFERENCES subcategories(id),
    CONSTRAINT fk_sales_region FOREIGN KEY (region_id) REFERENCES regions(id),
    CONSTRAINT fk_sales_segment FOREIGN KEY (segment_id) REFERENCES segments(id),
    CONSTRAINT fk_sales_brand FOREIGN KEY (brand_id) REFERENCES brands(id),
    CONSTRAINT fk_sales_sku FOREIGN KEY (sku_id) REFERENCES skus(id)
);
