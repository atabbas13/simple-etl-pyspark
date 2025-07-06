CREATE TABLE IF NOT EXISTS sales (
  order_id INT,
  customer_id TEXT,
  order_date DATE,
  product TEXT,
  quantity INT,
  unit_price NUMERIC,
  cost_price NUMERIC,
  revenue NUMERIC,
  cost NUMERIC,
  profit NUMERIC,
  profit_margin NUMERIC
);