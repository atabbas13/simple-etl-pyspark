# 🚀 ETL Pipeline with PySpark, PostgreSQL & Docker

This project is a simple ETL pipeline using **PySpark**, **PostgreSQL**, and **Docker Compose**. It follows a basic structure that outlines the purpose of an ETL pipeline at its core.

---

## 🧱 Tech Stack

- **PySpark** for data processing
- **PostgreSQL** as the data warehouse
- **Docker Compose** for container orchestration
- **DBeaver** (optional) for visual querying OR you can directly query using the docker CLI.

---

## 📊 ETL Process Overview

1. **Extract**: Read sales data from a CSV file
2. **Transform**: Compute revenue, cost, profit, and profit margin.
3. **Load**: Write the final dataset in a PostgreSQL table (`sales`)

---

## 📁 Project Structure
```
etl-pipeline-pyspark/
├── data/
│ └── sales_data.csv # Raw input CSV
├── jars/
│ └── postgresql-42.6.0.jar # PostgreSQL JDBC driver
├── sql/
│ └── init.sql # Initializes the PostgreSQL table
├── main.py # PySpark ETL script
├── docker-compose.yml # Services: Spark + Postgres
└── README.md
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Docker & Docker Compose
- (Optional) DBeaver for querying PostgreSQL

### 📦 Setup Steps

1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-username>/etl-pipeline-pyspark.git
   cd etl-pipeline-pyspark
   ```

2. **Download the PostgreSQL JDBC driver**
- Download postgresql-42.6.0.jar
- Place it in the jars/ folder

3. **Start the pipeline**
    ```bash
    docker-compose up --build
    ```

4. **Verify output**
- Connect to PostgreSQL using DBeaver or CLI:
    ```bash
    docker exec -it postgres psql -U sparkuser -d sparkdb
    ```
- Run a sample query:
    ```sql
    SELECT * FROM sales LIMIT 10;
    --Don't forget the semicolon ;
    ```
---

### 🧼 To Clean Up
```bash
docker-compose down -v
```

---

### ✅ Next Steps
- Add reporting layer (e.g., export CSV summary)
- Connect Apache Airflow to schedule ETL jobs
- Add logging and unit tests

## Author
### Abbas Mirza
