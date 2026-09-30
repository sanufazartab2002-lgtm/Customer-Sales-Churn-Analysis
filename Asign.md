<div align="center">

# 📊 Customer Sales & Churn Analysis

**Understanding customer behavior and spotting churn patterns with Python**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Charts-11557C)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4C72B0)
![VS Code](https://img.shields.io/badge/VS%20Code-Editor-007ACC?logo=visualstudiocode&logoColor=white)

</div>

---

## 📑 Table of Contents

- [🧭 Project Overview](#-project-overview)
- [🎯 Objective](#-objective)
- [🛠️ Tools & Technologies](#️-tools--technologies)
- [🗂️ Data Source](#️-data-source)
- [📋 Dataset Columns](#-dataset-columns)
- [🧹 Data Preparation & Quality Checks](#-data-preparation--quality-checks)
- [🔍 Analysis Performed](#-analysis-performed)
- [📈 Visualizations](#-visualizations)
- [🏆 Key Results](#-key-results)
- [💡 Business Insights](#-business-insights)
- [📁 Project Structure](#-project-structure)
- [▶️ How to Run](#️-how-to-run)
- [✅ Conclusion](#-conclusion)

---

## 🧭 Project Overview

This project analyzes **customer sales and churn data** using Python. The analysis focuses on:

- 💰 Customer spending
- 🎟️ Subscription type
- ⏳ Tenure
- 📞 Support calls
- 🚪 Churn behavior

> 🎯 **Main goal:** identify customer patterns and generate useful business insights from structured customer data.

---

## 🎯 Objective

The objective is to **understand customer behavior** and **identify patterns related to customer churn**. The project:

1. 🧮 Calculates customer and churn metrics
2. ⚖️ Compares customer groups
3. 📊 Uses charts to make the results easier to understand

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| 🐍 **Python** | Core programming language |
| 🐼 **Pandas** | Data handling and analysis |
| 📉 **Matplotlib** | Base charts and plots |
| 🎨 **Seaborn** | Statistical visualization |
| 💻 **VS Code** | Development environment |

---

## 🗂️ Data Source

The project uses a **small structured customer dataset** created directly in Python and converted into a **Pandas DataFrame**.

> ℹ️ **Database:** No SQL database was used in this project.

---

## 📋 Dataset Columns

| # | Column | Description |
|---|--------|-------------|
| 1 | 🆔 `Customer_ID` | Unique customer identifier |
| 2 | 🎂 `Age` | Customer age |
| 3 | 🚻 `Gender` | Customer gender |
| 4 | 🏙️ `City` | Customer city |
| 5 | 🎟️ `Subscription_Type` | Basic, Standard, or Premium subscription |
| 6 | 💵 `Monthly_spend` | Monthly customer spending |
| 7 | ⏳ `Tenure_Months` | Length of customer relationship in months |
| 8 | 🛒 `Total_Purchases` | Total purchases made by the customer |
| 9 | 📞 `Support_Calls` | Number of support calls |
| 10 | 🚪 `Churn` | Customer churn status: **Yes / No** |

---

## 🧹 Data Preparation & Quality Checks

- [x] 👀 Display customer data
- [x] 🔢 Check total number of customers
- [x] ❓ Check missing values
- [x] 🔁 Check duplicate records
- [x] 🚪 Check churn counts
- [x] 🧱 Review the structure of the data

---

## 🔍 Analysis Performed

### 📌 Overall Metrics
- 👥 Total customer count
- 🚪 Churned customer count
- 📉 Overall churn rate
- 💵 Average monthly spending

### 🏙️ Customer Distribution
- 📍 Customers by city
- 🎟️ Customers by subscription type

### 💰 Spending Analysis
- 🎟️ Average spending by subscription type
- 🏙️ Average spending by city

### 🔄 Churn Comparison
- ⏳ Average tenure by churn status
- 📞 Average support calls by churn status
- 💵 Average monthly spending by churn status
- 🎟️ Churn by subscription type

---

## 📈 Visualizations

The project creates the following charts:

| Chart | What it shows |
|-------|---------------|
| 📊 **Churn by Subscription Type** | Which plans see more churn |
| 💵 **Average Monthly Spend by Churn** | Spending gap between churned and retained customers |
| 📞 **Average Support Calls by Churn** | Link between support contact and churn |
| ⏳ **Average Tenure by Churn** | How long churned vs. retained customers stay |

---

## 🏆 Key Results

> Based on the current project dataset:

| 👥 Total Customers | 🚪 Churned Customers | 📉 Churn Rate | 💵 Avg Monthly Spend |
|:---:|:---:|:---:|:---:|
| **5** | **3** | **60%** | **1240** |

---

## 💡 Business Insights

The analysis helps understand:

- 📉 **Customer churn percentage**
- 🏙️ **Customer distribution across cities**
- 🎟️ **Customer distribution across subscription plans**
- 💵 **Spending differences by churn status**
- ⏳ **Tenure differences by churn status**
- 📞 **Support-call differences by churn status**
- 🔍 **Churn patterns across subscription types**

---

## 📁 Project Structure

```text
CUSTOMER_SALES_CHURN_ANALYSIS
│
├── 🐍 customer_churn.py
└── 📄 README.md
```

---

## ▶️ How to Run

**1️⃣ Install Python**

**2️⃣ Open the project folder in VS Code**

**3️⃣ Install the required libraries**

```bash
pip install pandas matplotlib seaborn
```

**4️⃣ Run the script**

```bash
python customer_churn.py
```

**5️⃣ View the results** in the terminal and the charts generated by the program. 🎉

---

## ✅ Conclusion

This project demonstrates how **Python** can be used to analyze customer data and identify churn-related patterns. **Pandas** is used for data handling and analysis, while **Matplotlib** and **Seaborn** are used for visualization.

The project provides practical experience in:

- 🧹 Data cleaning
- 🔬 Data analysis
- 🗃️ Grouping and calculations
- 📊 Business-focused data visualization

---

<div align="center">

⭐ **Thanks for checking out this project!** ⭐

</div>