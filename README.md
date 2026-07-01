# 🍔 Swiggy Sales Analysis

> End-to-end food delivery analytics project using **Python, PostgreSQL, SQL, ETL, and Power BI**

![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi)
![Python](https://img.shields.io/badge/Python-Data%20Generation-blue?style=for-the-badge&logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql)
![SQL](https://img.shields.io/badge/SQL-Analytics-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 🖼 Dashboard Preview

<!-- Replace the placeholders below with actual screenshots, e.g. assets/screenshots/executive-overview.png -->

| Executive Overview | Customer Analytics |
|---|---|
| ![Executive Overview](assets/screenshots/executive-overview.png) | ![Customer Analytics](assets/screenshots/customer-analytics.png) |

| Restaurant Analytics | Order Analytics |
|---|---|
| ![Restaurant Analytics](assets/screenshots/restaurant-analytics.png) | ![Order Analytics](assets/screenshots/order-analytics.png) |

| Menu Analytics |
|---|
| ![Menu Analytics](assets/screenshots/menu-analytics.png) |

---

## 📖 Table of Contents

- [Dashboard Preview](#-dashboard-preview)
- [Project Overview](#-project-overview)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Dataset](#-dataset)
- [Database Design](#-database-design)
- [ETL Process](#-etl-process)
- [Data Model](#-data-model)
- [Feature Engineering](#-feature-engineering)
- [Dashboard Features](#-dashboard-features)
- [Business KPIs](#-business-kpis)
- [DAX Measures](#-dax-measures)
- [Business Insights](#-business-insights)
- [Getting Started](#️-getting-started)
- [Future Improvements](#-future-improvements)
- [Author](#-author)
- [License](#-license)

---

## 📌 Project Overview

This project simulates a real-world Swiggy-style food delivery platform by generating **600,000+ food delivery orders** across **10 Indian cities** and transforming them into an analytics-ready data warehouse.

The project covers the complete analytics workflow, end to end:

- ✅ Synthetic data generation using Python
- ✅ Database design in PostgreSQL
- ✅ SQL ETL & data modeling
- ✅ Star schema & aggregated tables
- ✅ Interactive Power BI dashboard
- ✅ Advanced DAX measures
- ✅ Business KPI analysis

---

## 🚀 Tech Stack

| Category | Tools |
|---|---|
| Language | Python (Pandas, NumPy) |
| Database | PostgreSQL |
| Data Layer | SQL (DDL, ETL, Aggregations) |
| Visualization | Power BI, DAX |

---

## 📂 Project Structure

```
Swiggy-Sales-Analysis
│
├── Database
│   ├── ddl.sql                # Table creation & schema definitions
│   ├── insert_data.sql        # Loads raw data into base tables
│   └── aggregated_table.sql   # Builds orders_master & order_items_master
│
├── Dataset
│   └── Data.rar                # Compressed synthetic dataset
│
├── Scripts
│   └── generate.py             # Synthetic data generation script
│
├── dashboard
│   └── DAX.md                  # DAX measure documentation
│
└── README.md
```

---

## 📊 Dataset

The synthetic dataset contains the following tables:

| Table | Description |
|---|---|
| Users | Customer information |
| Restaurants | Restaurant details |
| Menu | Food menu items |
| Orders | Order transactions |
| Order Items | Individual ordered products |

**Scale of generated data:**

| Metric | Value |
|---|---|
| Customers | 10,000 |
| Restaurants | 1,000 |
| Orders | 600,000+ |
| Date Range | 2022 – 2025 |
| Cities Covered | 10 major Indian cities |

---

## 🏗 Database Design

The project follows a relational database model consisting of:

- Users
- Restaurants
- Menu
- Orders
- Order Items

Optimized using:

- Primary keys
- Foreign keys
- Multiple SQL indexes
- Cascading relationships

---

## ⚙ ETL Process

The ETL pipeline performs:

- Data cleaning
- Feature engineering
- Customer segmentation
- Restaurant classification
- Time-based analysis
- Revenue aggregation

Master tables are built using SQL joins to improve dashboard performance:

- `orders_master`
- `order_items_master`

---

## 📐 Data Model

The project uses a star schema:

```
                        ┌─────────────┐
                        │  Date Table │
                        └──────┬──────┘
                               │
        ┌──────────────┐      │      ┌────────────────────┐
        │ Orders Master│◄─────┴─────►│ Order Items Master  │
        └──────┬───────┘             └──────────┬──────────┘
               │                                 │
        ┌──────┴───────┐                  ┌──────┴──────┐
        │    Users     │                  │     Menu     │
        └──────┬───────┘                  └─────────────┘
               │
        ┌──────┴───────┐
        │ Restaurants  │
        └──────────────┘
```

---

## 🧠 Feature Engineering

Additional analytical columns include:

- Age groups
- Rating buckets
- Restaurant type
- Repeat customer flag
- Order year / month / quarter
- Day type (weekday vs. weekend)
- Time slot
- Price category
- Veg / non-veg classification

---

## 📈 Dashboard Features

The Power BI dashboard provides interactive insights across five pages:

### Executive Overview
- Total Revenue
- Revenue Growth
- Total Orders
- Delivered Orders
- Cancelled Orders
- Customer Count
- Average Order Value

![Executive Overview Page](assets/screenshots/executive-overview.png)

### Customer Analytics
- Repeat Customers
- Customer Segmentation
- Age Group Analysis
- Occupation Insights
- Gender Distribution

![Customer Analytics Page](assets/screenshots/customer-analytics.png)

### Restaurant Analytics
- Top Restaurants
- Cuisine Performance
- Cloud Kitchen vs. Traditional
- Restaurant Ratings
- Revenue by Restaurant

![Restaurant Analytics Page](assets/screenshots/restaurant-analytics.png)

### Order Analytics
- Order Trends
- Monthly Sales
- Weekend vs. Weekday
- Time Slot Analysis
- Payment Method Distribution

![Order Analytics Page](assets/screenshots/order-analytics.png)

### Menu Analytics
- Veg vs. Non-Veg
- Category Performance
- Price Segment Analysis
- Best-Selling Items

![Menu Analytics Page](assets/screenshots/menu-analytics.png)

---

## 📊 Business KPIs

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

## 📊 DAX Measures

The dashboard includes advanced DAX calculations, including:

- Revenue Growth
- Orders Growth
- Current Year vs. Last Year
- Dynamic KPIs
- Time Intelligence
- Customer Metrics
- Average Order Value
- Revenue Display Formatting

See [`dashboard/DAX.md`](dashboard/DAX.md) for the full list of measures and formulas.

---

## 📌 Business Insights

The dashboard helps answer questions like:

- Which cities generate the highest revenue?
- Which cuisines perform best?
- What are customer ordering patterns?
- Which restaurants drive maximum sales?
- How do repeat customers contribute to revenue?
- Which payment methods are most preferred?
- What are the peak ordering hours?

---

## ▶️ Getting Started

### Prerequisites

- Python 3.9+
- PostgreSQL 13+
- Power BI Desktop

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Swiggy-Sales-Analysis.git
cd Swiggy-Sales-Analysis
```

### 2. Generate the dataset

```bash
cd Scripts
python generate.py
```

### 3. Set up the database

Run the following SQL scripts in order:

```bash
psql -U your_username -d your_database -f Database/ddl.sql
psql -U your_username -d your_database -f Database/insert_data.sql
psql -U your_username -d your_database -f Database/aggregated_table.sql
```

### 4. Connect Power BI

Open Power BI Desktop and connect to your PostgreSQL database using the `orders_master` and `order_items_master` tables as your primary data sources.

---

## 📌 Future Improvements

- [ ] Real-time dashboard
- [ ] Customer cohort analysis
- [ ] RFM segmentation
- [ ] Demand forecasting
- [ ] Machine learning recommendation system
- [ ] Delivery time prediction

---

## 👨‍💻 Author

**Karanjyoti Medhi**

- Data Analytics
- Power BI
- SQL
- Python
- PostgreSQL

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## ⭐ Support

If you found this project useful, consider giving it a star — it helps others discover it too!
