# 🧮 Sales Data — SQL + ETL Project

This project demonstrates a complete **ETL (Extract, Transform, Load)** workflow using Python and SQLite, followed by **SQL analysis** for business insights.

---

## 🚀 Project Overview

**Goal:** Load and analyze sales data from a CSV file into a SQLite database using an automated ETL pipeline.

**Key Tasks:**
1. Extract raw data (`superstore_cleaned.csv`).
2. Transform and clean using pandas.
3. Load data into SQLite (`data/sales.db`).
4. Execute SQL queries for analysis.
5. Export results as CSV for reporting.

---

## 🧰 Tech Stack

- **Python** (pandas, sqlite3, argparse)
- **SQLAlchemy / SQLite**
- **Jupyter Notebook**
- **SQL**

---

## 🗂️ Repository Structure
```
sales-data-etl-and-sql-analysis/
│
├── data/
│ ├── raw/sales.csv
│ └── sales.db
│
├── src/
│ └── etl.py
│
├── sql/
│ └── queries.sql
│
├── notebooks/
│ └── 02_sql_analysis.ipynb
│
├── exports/
│ ├── query_1.csv
│ ├── query_2.csv
│ ├── query_3.csv
│ ├── query_4.csv
│ └── query_5.csv
│
└── README.md
```
---

## ⚙️ How to Run

1. **Run the ETL pipeline:**
   ```bash
   python src/etl.py --input data/raw/sales.csv --db data/sales.db
   
2. **Execute the analysis notebook:**
Open notebooks/02_sql_analysis.ipynb and run all cells.

3. **Explore exported results:**
CSV files will be generated in /exports/.

🧑‍💻 Author

Daniel Rojas Rodríguez
Industrial Engineer | Data Analyst

https://github.com/ARCANGITHUB/portfolio-data.git