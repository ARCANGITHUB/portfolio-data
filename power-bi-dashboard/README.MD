# 📊 Sales Analytics Dashboard — Power BI

 
The dashboard provides insights into revenue, profitability, product performance, geographic markets, and long-term sales trends.

---

## 📁 Repository Structure

```
project-3-powerbi-dashboard/
│
├── data/
│   ├── raw/
│   │   └── Superstore_Sales.csv
│   └── processed/
│       └── superstore_cleaned.csv
│
├── docs/
│   └── screenshots/
│       ├── Page 1 - Sales Performance Dashboard.png
│       ├── Page 2 - Product and Data Analysis.png
│       └── Page 3 - Sales by Region and Category.png
│
├── powerbi/
│   └── sales_dashboard.pbix
│
└── README.md
```

---

## 📌 Project Overview

This Power BI report was created to analyze sales across:

- Countries  
- Product categories
- Products by region
- Yearly trends  
- Profitability metrics  


---

## 🧱 Data Model

### **Tables**
- `sales` — main fact table with all transactions  
- `date` — calendar table created in Power BI  

### **Relationship**
```
calendar[date] 1 ───── * fact_sales[order_date]
```

This relationship enables time-intelligence calculations (YoY, MoM, etc.).

---

## 📐 DAX Measures Used

```
Total Sales =
SUM(sales[total_sales])

Total Profit =
SUM(sales[profit])

Profit Margin =
DIVIDE([Total Profit], [Total Sales])

Total Quantity =
SUM(sales[quantity])

Sales YoY % =
VAR PrevYear =
    CALCULATE([Total Sales], SAMEPERIODLASTYEAR(date[date]))
RETURN
DIVIDE([Total Sales] - PrevYear, PrevYear)
```

---

# 📊 Dashboard Pages

## 🟦 Page 1 — Executive Summary

Includes:
- KPI Cards  
  - Total Sales  
  - Total Profit  
  - Profit Margin  
  - Total Quantity Sold  
  - Sales YoY %  
- Monthly Sales Line Chart  
- Filters for:
  - Country  
  - Category  
  - Product  

**Purpose:** Provide a global performance overview for decision-makers.

---

## 🟩 Page 2 — Product & Category Analysis

Includes:
- Top 10 Products by Sales (bar chart)  
- Category vs. Country Matrix  
- Sales by Country Map (shape map or filled map)  
- Filters for product and category  

**Purpose:** Identify top sellers, weak categories, and strong regional markets.

---

## 🟧 Page 3 — Trend & Time Analysis

Includes:
- Sales by Category Over Time  
- YoY Trend Comparison  
- Seasonal or monthly patterns  

**Purpose:** Understand long-term behavior, trends, and category growth.

---

## 📸 Report Screenshots

Screenshots are stored in:

```
docs/screenshots/
```


## 🚀 How to Open the Dashboard

1. Download the `.pbix` file from `/pbix/sales_dashboard.pbix`  
2. Open it using **Power BI Desktop**  
3. Use the slicers and visuals to explore the data interactively  

---

## 🧩 Tools Used

- Power BI Desktop  
- Power Query  
- DAX  
- CSV structured dataset  

---

## 📜 License

This project is available for learning, portfolio, and demonstration purposes.

