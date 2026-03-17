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

CREATE TABLE IF NOT EXISTS app_components (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS agg_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS kpis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS ppgs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(100) NOT NULL UNIQUE,
    description VARCHAR(200) NOT NULL
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

CREATE TABLE IF NOT EXISTS business_top_scorecard (
    id INT AUTO_INCREMENT PRIMARY KEY,
    brand_id INT NOT NULL,
    subcategory_id INT NOT NULL,
    year INT NOT NULL,
    month INT NOT NULL,
    app_component_id INT NOT NULL,
    agg_type_id INT NOT NULL,
    kpi_id INT NOT NULL,
    month_value DECIMAL(14,2) NOT NULL,
    month_growth DECIMAL(14,2) NOT NULL,
    quarterly_value DECIMAL(14,2) NOT NULL,
    quarterly_growth DECIMAL(14,2) NOT NULL,
    ytd_value DECIMAL(14,2) NOT NULL,
    ytd_growth DECIMAL(14,2) NOT NULL,
    category_change_monthly DECIMAL(14,2) NOT NULL,
    category_change_quarterly DECIMAL(14,2) NOT NULL,
    category_change_ytd DECIMAL(14,2) NOT NULL,
    INDEX idx_bts_brand (brand_id),
    INDEX idx_bts_subcategory (subcategory_id),
    INDEX idx_bts_year (year),
    INDEX idx_bts_month (month),
    INDEX idx_bts_app_component (app_component_id),
    INDEX idx_bts_agg_type (agg_type_id),
    INDEX idx_bts_kpi (kpi_id),
    CONSTRAINT fk_bts_brand FOREIGN KEY (brand_id) REFERENCES brands(id),
    CONSTRAINT fk_bts_subcategory FOREIGN KEY (subcategory_id) REFERENCES subcategories(id),
    CONSTRAINT fk_bts_app_component FOREIGN KEY (app_component_id) REFERENCES app_components(id),
    CONSTRAINT fk_bts_agg_type FOREIGN KEY (agg_type_id) REFERENCES agg_types(id),
    CONSTRAINT fk_bts_kpi FOREIGN KEY (kpi_id) REFERENCES kpis(id)
);

CREATE TABLE IF NOT EXISTS business_consumption_over_time (
    id INT AUTO_INCREMENT PRIMARY KEY,
    brand_id INT NOT NULL,
    subcategory_id INT NOT NULL,
    year INT NOT NULL,
    month INT NOT NULL,
    agg_type_id INT NOT NULL,
    value DECIMAL(14,2) NOT NULL,
    INDEX idx_bcot_brand (brand_id),
    INDEX idx_bcot_subcategory (subcategory_id),
    INDEX idx_bcot_year (year),
    INDEX idx_bcot_month (month),
    INDEX idx_bcot_agg_type (agg_type_id),
    CONSTRAINT fk_bcot_brand FOREIGN KEY (brand_id) REFERENCES brands(id),
    CONSTRAINT fk_bcot_subcategory FOREIGN KEY (subcategory_id) REFERENCES subcategories(id),
    CONSTRAINT fk_bcot_agg_type FOREIGN KEY (agg_type_id) REFERENCES agg_types(id)
);

CREATE TABLE IF NOT EXISTS business_sku_level (
    id INT AUTO_INCREMENT PRIMARY KEY,
    brand_id INT NOT NULL,
    subcategory_id INT NOT NULL,
    year INT NOT NULL,
    month INT NOT NULL,
    ppg_id INT NOT NULL,
    sku_id INT NOT NULL,
    autoship_contribution DECIMAL(14,2) NOT NULL,
    non_autoship_contribution DECIMAL(14,2) NOT NULL,
    INDEX idx_bsl_brand (brand_id),
    INDEX idx_bsl_subcategory (subcategory_id),
    INDEX idx_bsl_year (year),
    INDEX idx_bsl_month (month),
    INDEX idx_bsl_ppg (ppg_id),
    INDEX idx_bsl_sku (sku_id),
    CONSTRAINT fk_bsl_brand FOREIGN KEY (brand_id) REFERENCES brands(id),
    CONSTRAINT fk_bsl_subcategory FOREIGN KEY (subcategory_id) REFERENCES subcategories(id),
    CONSTRAINT fk_bsl_ppg FOREIGN KEY (ppg_id) REFERENCES ppgs(id),
    CONSTRAINT fk_bsl_sku FOREIGN KEY (sku_id) REFERENCES skus(id)
);

CREATE TABLE IF NOT EXISTS business_health_scorecard (
    id INT AUTO_INCREMENT PRIMARY KEY,
    brand_id INT NOT NULL,
    subcategory_id INT NOT NULL,
    year INT NOT NULL,
    month INT NOT NULL,
    agg_type_id INT NOT NULL,
    kpi_id INT NOT NULL,
    ytd_value DECIMAL(14,2) NOT NULL,
    py_growth DECIMAL(14,2) NOT NULL,
    category_avg_ytd DECIMAL(14,2) NOT NULL,
    INDEX idx_bhs_brand (brand_id),
    INDEX idx_bhs_subcategory (subcategory_id),
    INDEX idx_bhs_year (year),
    INDEX idx_bhs_month (month),
    INDEX idx_bhs_agg_type (agg_type_id),
    INDEX idx_bhs_kpi (kpi_id),
    CONSTRAINT fk_bhs_brand FOREIGN KEY (brand_id) REFERENCES brands(id),
    CONSTRAINT fk_bhs_subcategory FOREIGN KEY (subcategory_id) REFERENCES subcategories(id),
    CONSTRAINT fk_bhs_agg_type FOREIGN KEY (agg_type_id) REFERENCES agg_types(id),
    CONSTRAINT fk_bhs_kpi FOREIGN KEY (kpi_id) REFERENCES kpis(id)
);
