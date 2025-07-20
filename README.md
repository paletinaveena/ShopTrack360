# 🛍️ ShopTrack360: Customer Retention and Engagement Optimization for an E-Commerce Platform

## 📌 Project Overview

**ShopTrack360** is a behavioral analytics and machine learning project that uses real-world e-commerce transaction data to simulate and optimize user retention, engagement, and product recommendation strategies — adapted from the logic of short-form content platforms like TikTok.

We applied techniques such as churn modeling, customer segmentation, time series forecasting, and simulated A/B testing to uncover revenue drivers, predict at-risk users, and surface personalized product recommendations.

**Project Summary**  
ShopTrack360 is a data-driven behavioral analytics project designed to simulate a full engagement and retention optimization pipeline for an e-commerce platform. Using real transactional data, we model customer churn, segment user personas, recommend products, forecast platform KPIs, and diagnose anomalies – all structured for real-world business impact.

---

## 🎯 Objective

To identify high-risk churn segments, optimize product engagement strategies, and forecast business health metrics using machine learning and analytics techniques.

---
## 🎯 Business Problem

E-commerce platforms often struggle with identifying which customers are at risk of churn, which products drive repeat behavior, and what strategies improve engagement. This project answers:

- Who are the loyal vs. one-time customers?
- Which behavioral features predict churn?
- How can we segment users into actionable personas?
- Can we forecast sales and identify anomalies in advance?
- What products should we recommend to which users?

---

## 📊 Key Features

- Churn prediction using Logistic Regression & Random Forest
- Customer segmentation using K-Means clustering
- Recommendation engine using Collaborative & Content-Based Filtering
- Time series forecasting with Prophet and ARIMA
- Root cause analysis for sales anomalies
- Streamlit dashboard (or Tableau) for business insights

---

## 🧱 Dataset

**Source**: [UCI Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail)

**Columns**:
- `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`

---

## 🧩 Project Modules

### 1. 🧹 Data Cleaning & Preprocessing
- Null handling
- Refund filtering
- Feature extraction (Invoice datetime, total price)

### 2. 📊 Exploratory Data Analysis
- Product trends
- Purchase patterns
- Geographic insights

### 3. 🧠 Churn Prediction
- Feature engineering (recency, frequency, monetary)
- Classification models (Logistic Regression, Random Forest)
- SHAP for interpretability

### 4. 👥 Customer Segmentation
- RFM Clustering
- K-Means with PCA
- Persona profiling

### 5. 🎁 Product Recommendation (Optional Bonus)
- Collaborative & content-based filtering
- Top-K item recommendations

### 6. 📈 Time Series Forecasting
- Daily revenue and transaction volume
- Prophet and ARIMA models

### 7. 🚨 Root Cause Analysis (RCA)
- Simulated anomalies
- Statistical testing by cohort and country
- RCA dashboard (Streamlit / Tableau)

---

## 📊 Dashboards

- Tableau: Interactive RCA and churn visualization
- Streamlit: Real-time churn prediction and forecast interface

---

## 🧪 Tools & Technologies

| Type | Tools |
|------|-------|
| Language | Python (Pandas, NumPy, Scikit-learn) |
| Modeling | Logistic Regression, Random Forest, Prophet, K-Means |
| Visualization | Seaborn, Matplotlib, Plotly |
| Dashboarding | Tableau, Streamlit |
| Explainability | SHAP |
| Deployment | GitHub, Streamlit Cloud (optional) |

---

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/your_username/ShopTrack360.git  
cd ShopTrack360

# 2. Create virtual environment (optional)
python -m venv venv  
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run notebooks in order from /notebooks/
# 5. To launch Streamlit dashboard (optional)
streamlit run dashboards/app.py

---

## 👤 Author
Naveena Paleti
MS Business Analytics & AI | Data Science Intern @ BoA
🔗 LinkedIn | 🔗 GitHub

---

## 📜 License
MIT License. See LICENSE for details.