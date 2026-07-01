# 🍔 Swiggy Sales Analysis

> End-to-End Food Delivery Analytics Project using **Python, PostgreSQL, SQL, ETL, and Power BI**

![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi)
![Python](https://img.shields.io/badge/Python-Data%20Generation-blue?style=for-the-badge&logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql)
![SQL](https://img.shields.io/badge/SQL-Analytics-orange?style=for-the-badge)

---

## 📌 Project Overview

This project simulates a real-world Swiggy food delivery platform by generating **600,000+ food delivery orders** across **10 Indian cities** and transforming them into an analytics-ready data warehouse.

The project covers the complete analytics workflow:

- Synthetic Data Generation using Python
- Database Design in PostgreSQL
- SQL ETL & Data Modeling
- Star Schema & Aggregated Tables
- Interactive Power BI Dashboard
- Advanced DAX Measures
- Business KPI Analysis

---

## 🚀 Tech Stack

- **Python**
- **PostgreSQL**
- **SQL**
- **Power BI**
- **DAX**
- **Pandas**
- **NumPy**

---

# 📂 Project Structure

```
Swiggy-Sales-Analysis
│
├── Database
│   ├── ddl.sql
│   ├── aggregated_table.sql
│   └── inset_data.sql
│
├── Dataset
│   └── Data.rar
│
├── Scripts
│   └── generate.py
│
├── dashboard
│   └── DAX.md
│
└── README.md
```

---

# 📊 Dataset

The synthetic dataset contains:

| Table | Description |
|---------|-------------|
| Users | Customer information |
| Restaurants | Restaurant details |
| Menu | Food menu items |
| Orders | Order transactions |
| Order Items | Individual ordered products |

Generated using Python:

- **10,000 Customers**
- **1,000 Restaurants**
- **600,000 Orders**
- **2022 – 2025**
- **10 Major Indian Cities**

---

# 🏗 Database Design

The project follows a relational database model consisting of:

- Users
- Restaurants
- Menu
- Orders
- Order Items

Optimized using:

- Primary Keys
- Foreign Keys
- Multiple SQL Indexes
- Cascading Relationships

---

# ⚙ ETL Process

The ETL pipeline performs:

- Data Cleaning
- Feature Engineering
- Customer Segmentation
- Restaurant Classification
- Time-based Analysis
- Revenue Aggregation

Master tables are created using SQL joins to improve dashboard performance.

Generated Tables:

- `orders_master`
- `order_items_master`

---

# 📈 Dashboard Features

The Power BI dashboard provides interactive insights into:

### Executive Overview

- Total Revenue
- Revenue Growth
- Total Orders
- Delivered Orders
- Cancelled Orders
- Customer Count
- Average Order Value

### Customer Analytics

- Repeat Customers
- Customer Segmentation
- Age Group Analysis
- Occupation Insights
- Gender Distribution

### Restaurant Analytics

- Top Restaurants
- Cuisine Performance
- Cloud Kitchen vs Traditional
- Restaurant Ratings
- Revenue by Restaurant

### Order Analytics

- Order Trends
- Monthly Sales
- Weekend vs Weekday
- Time Slot Analysis
- Payment Method Distribution

### Menu Analytics

- Veg vs Non-Veg
- Category Performance
- Price Segment Analysis
- Best Selling Items

---

# 📊 Business KPIs

The project tracks:

- Total Revenue
- Revenue Growth %
- Total Orders
- Order Growth %
- Delivered Orders
- Cancelled Orders
- Repeat Customer Rate
- Customer Lifetime Insights
- Restaurant Performance
- Average Order Value

---

# 📐 Data Model

The project uses a Star Schema consisting of:

```
            Date Table
                 |
                 |
Orders Master -------- Order Items Master
      |                     |
      |                     |
 Users                Menu
      |
 Restaurants
```

---

# 🧠 Feature Engineering

Additional analytical columns include:

- Age Groups
- Rating Buckets
- Restaurant Type
- Repeat Customer Flag
- Order Year
- Order Month
- Quarter
- Day Type
- Time Slot
- Price Category
- Veg / Non-Veg Classification

---

# 📊 DAX Measures

The dashboard contains advanced DAX calculations including:

- Revenue Growth
- Orders Growth
- Current Year vs Last Year
- Dynamic KPIs
- Time Intelligence
- Customer Metrics
- Average Order Value
- Revenue Display Formatting

---

# 📌 Business Insights

The dashboard helps answer questions like:

- Which cities generate the highest revenue?
- Which cuisines perform best?
- What are customer ordering patterns?
- Which restaurants drive maximum sales?
- How do repeat customers contribute to revenue?
- Which payment methods are most preferred?
- What are peak ordering hours?

---

# ▶️ Getting Started

### Clone Repository

```bash
git clone https://github.com/yourusername/Swiggy-Sales-Analysis.git
```

### Generate Dataset

```bash
cd Scripts

python generate.py
```

### Create Database

Run:

```
Database/ddl.sql
```

Then

```
Database/inset_data.sql
```

Then

```
Database/aggregated_table.sql
```

Finally connect Power BI to PostgreSQL.

---

# 📌 Future Improvements

- Real-time Dashboard
- Customer Cohort Analysis
- RFM Segmentation
- Demand Forecasting
- Machine Learning Recommendation System
- Delivery Time Prediction

---

# 👨‍💻 Author

**Karanjyoti Medhi**

- Data Analytics
- Power BI
- SQL
- Python
- PostgreSQL

---

## ⭐ If you found this project useful, consider giving it a Star!
