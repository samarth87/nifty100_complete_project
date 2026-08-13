# 📊 Mutual Fund Analytics

### 🚀 End-to-End Mutual Fund Data Analytics & Performance Analysis Platform

<p align="center">

**A data-driven analytics platform for exploring, cleaning, analyzing and evaluating mutual fund performance using Python, SQL, statistical analysis and data visualization.**

<br>

<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>

</p>

<p align="center">

📈 **Data Engineering**   •  
🔍 **Exploratory Data Analysis**   •  
📊 **Performance Analytics**   •  
💡 **Financial Insights**

</p>

---

# 🧭 Overview

**Mutual Fund Analytics** is an end-to-end data analytics project focused on transforming raw mutual fund data into meaningful and actionable financial insights.

The project follows a complete analytics pipeline:

```text
📁 Raw Data
     │
     ▼
🧹 Data Cleaning
     │
     ▼
🧪 Data Validation
     │
     ▼
🗄️ Database
     │
     ▼
🔍 Exploratory Data Analysis
     │
     ▼
📈 Performance Analysis
     │
     ▼
📊 Visualizations
     │
     ▼
💡 Financial Insights
```

The objective is to make mutual fund data easier to understand by examining important factors such as:

* 📈 Fund performance
* 💰 Returns
* 📊 NAV trends
* 📉 Risk-related indicators
* 🏦 Fund characteristics
* 🔎 Historical patterns
* 📊 Fund-level comparisons

This project was developed as part of the **Bluestock Mutual Fund Analytics Capstone**.

---

# 🎯 Project Objectives

The main objectives of this project are:

|     | Objective                                      |
| --- | ---------------------------------------------- |
| 📥  | Collect and organize mutual fund datasets      |
| 🧹  | Clean and standardize raw financial data       |
| 🔍  | Perform exploratory data analysis              |
| 📊  | Analyze mutual fund performance                |
| 📈  | Study NAV and historical trends                |
| 🗄️ | Store structured data in a relational database |
| 🧪  | Validate data quality and consistency          |
| 📉  | Generate analytical charts and reports         |
| 💡  | Extract meaningful financial insights          |
| 📝  | Document the complete analytics workflow       |

---

# 🔎 What Does This Project Analyze?

## 📌 01 — Fund Master Data

Analysis of fundamental information related to mutual fund schemes.

### Includes

* 🏦 Fund and scheme information
* 🗂️ Categories and classifications
* 📋 Fund characteristics
* 📊 Scheme-level attributes

---

## 📌 02 — NAV Analysis

Historical NAV data is processed and analyzed to understand:

* 📈 NAV movement
* 📊 Historical trends
* 🧪 Data consistency
* 🔎 Fund-level performance patterns

---

## 📌 03 — Performance Analytics

The project examines mutual fund performance using historical data and analytical calculations.

### Questions explored

> 📈 Which funds have performed strongly?

> 📊 How does performance vary across funds?

> 💰 What are the historical return patterns?

> 🔎 Which funds show consistent performance?

---

## 📌 04 — Exploratory Data Analysis

EDA is used to identify:

* 📊 Distribution patterns
* ❌ Missing values
* 📈 Outliers
* ⚠️ Data inconsistencies
* 🔎 Fund-level trends
* 🔗 Relationships between important variables

---

# 🏗️ Project Architecture

```text
                         ┌─────────────────────┐
                         │     📁 RAW DATA     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  📥 DATA INGESTION  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                    ┌─────────────────────────────┐
                    │   🧹 DATA CLEANING &        │
                    │      STANDARDIZATION        │
                    └──────────────┬──────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────────┐
                    │   🧪 DATA VALIDATION &      │
                    │      QUALITY CHECKS         │
                    └──────────────┬──────────────┘
                                   │
                                   ▼
                         ┌─────────────────────┐
                         │   🗄️ SQLite DB     │
                         └──────────┬──────────┘
                                    │
                         ┌──────────┴──────────┐
                         ▼                     ▼
                ┌─────────────────┐   ┌─────────────────┐
                │ 🔍 EDA           │   │ 📈 Performance  │
                │                  │   │    Analytics    │
                └────────┬─────────┘   └────────┬────────┘
                         │                      │
                         └──────────┬───────────┘
                                    ▼
                         ┌─────────────────────┐
                         │ 📊 Charts & Reports │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ 💡 Financial       │
                         │    Insights        │
                         └─────────────────────┘
```

---

# 🛠️ Technology Stack

<div align="center">

|         Technology        | Purpose                                 |
| :-----------------------: | --------------------------------------- |
|       🐍 **Python**       | Data processing and analytics           |
|       🐼 **Pandas**       | Data cleaning and manipulation          |
|  📓 **Jupyter Notebook**  | Exploratory and analytical work         |
|    🗄️ **SQL / SQLite**   | Structured data storage and querying    |
| 📊 **Data Visualization** | Charts and analytical insights          |
|  📁 **CSV / Data Files**  | Source and processed datasets           |
|   🔧 **Python Scripts**   | Data pipeline automation                |
|      📝 **Markdown**      | Project documentation                   |
|      ⚡ **Streamlit**      | Interactive analytics dashboard         |
|      📊 **Power BI**      | Business intelligence and visualization |

</div>

---

# 🔄 Data Pipeline

```text
┌─────────────┐
│  📁 Source  │
│    Data     │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ 📥 Ingestion │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ 🧹 Cleaning │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ 🧪 Validate │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ 🗄️ SQLite   │
└──────┬──────┘
       │
       ├───────────────┐
       ▼               ▼
┌─────────────┐  ┌──────────────┐
│ 🔍 EDA      │  │ 📈 Analytics  │
└──────┬──────┘  └──────┬───────┘
       │                │
       └───────┬────────┘
               ▼
       ┌──────────────┐
       │ 📊 Reports   │
       │ & Charts     │
       └──────┬───────┘
              ▼
       ┌──────────────┐
       │ 💡 Insights  │
       └──────────────┘
```

---

# 📂 Repository Structure

```text
Mutual-fund-Analytics/
│
├── 📁 charts/
│   └── 📊 Generated visualizations
│
├── 📁 data/
│   └── 📁 Raw and processed datasets
│
├── 📁 notebooks/
│   ├── 📓 EDA_Analysis.ipynb
│   ├── 📓 Performance_Analytics.ipynb
│   └── 📓 fund_master_analysis.ipynb
│
├── 📁 outputs/
│   └── 📊 Analytical outputs
│
├── 📁 reports/
│   ├── 📄 data_quality_notes.txt
│   └── 📄 data_quality_summary.txt
│
├── 📁 sql/
│   └── 🗄️ SQL scripts and database queries
│
├── 🐍 clean_nav.py
├── 🐍 clean_performance.py
├── 🐍 clean_transactions.py
├── 🐍 create_database.py
├── 📖 data_dictionary.md
├── 🐍 data_ingestion.py
├── 🐍 live_nav_fetch.py
├── 🐍 load_data.py
├── 🐍 run_pipeline.py
├── 🐍 verify_data.py
├── 🐍 check_tables.py
│
├── 🗄️ bluestock_mf.db
├── 📋 requirements.txt
├── 📊 Mutual Funds Analytics.pptx
├── 📄 Bluestock Mutual Fund Analytics Platform.docx
│
└── 📖 README.md
```

---

# 📊 Analytics Capabilities

### 📈 Performance Analysis

Analyze historical performance across different mutual fund schemes.

### 💰 Return Analysis

Evaluate return patterns using historical financial data.

### 📊 NAV Trends

Study how NAV values change over time.

### 🔎 Fund Comparison

Compare funds based on important analytical metrics.

### 🧪 Data Quality

Identify missing values, inconsistencies and potential data issues.

### 📉 Visualization

Generate charts and reports to communicate financial insights clearly.

---

# 📋 Data Quality & Validation

The project includes data validation steps to improve the reliability of the analytical results.

### Validation areas include:

* ✅ Missing value checks
* ✅ Duplicate detection
* ✅ Data type validation
* ✅ Date validation
* ✅ Numerical consistency
* ✅ Database integrity
* ✅ Record-level checks

---

# 📈 Project Workflow

```text
        📁 Collect Data
              │
              ▼
        🧹 Clean Data
              │
              ▼
       🧪 Validate Data
              │
              ▼
       🗄️ Build Database
              │
              ▼
          🔍 Perform EDA
              │
              ▼
       📈 Analyze Performance
              │
              ▼
        📊 Create Charts
              │
              ▼
        💡 Generate Insights
              │
              ▼
       📝 Document Results
```

---

# 🚀 Key Highlights

<div align="center">

### 📥 Data Engineering

Structured ingestion, cleaning and transformation of financial datasets.

### 🔍 Exploratory Analysis

Identification of patterns, distributions, missing values and inconsistencies.

### 📈 Performance Analytics

Analysis of fund performance, NAV movement and historical trends.

### 🗄️ Database Integration

Structured storage and querying using SQLite.

### 📊 Visualization

Charts and analytical reports for communicating financial insights.

### 💡 Financial Insights

Transforming raw financial data into meaningful analytical conclusions.

</div>

---

# 🎓 Project Context

This project was developed as part of the:

## **Bluestock Mutual Fund Analytics Capstone**

The project demonstrates an end-to-end approach to financial data analytics, covering the complete journey from **raw datasets to structured insights and visualizations**.

---

# 🔮 Future Improvements

Potential future enhancements include:

* 📈 Additional financial performance metrics
* 📊 More interactive dashboards
* 🔎 Advanced fund screening
* 🤝 Peer-group comparison
* 📉 Advanced risk analysis
* 🤖 Predictive analytics
* ⚡ Automated data updates
* 🌐 Live financial data integration
* 📊 Enhanced Power BI reporting

---

# 👨‍💻 Author

### **Samarth Sehdev**

🎓 Computer Science Engineering Graduate

💻 Software & Full-Stack Developer
🤖 AI / ML Enthusiast
📊 Data & Analytics
🚀 Building practical technology projects

<br>

<a href="https://github.com/samarth87">
<img src="https://img.shields.io/badge/GitHub-samarth87-181717?style=for-the-badge&logo=github&logoColor=white"/>
</a>

<a href="https://www.linkedin.com/in/samarth-sehdev-36039726a/">
<img src="https://img.shields.io/badge/LinkedIn-Samarth_Sehdev-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>

<a href="mailto:samarthsehdev502@gmail.com">
<img src="https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
</a>

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

**Built with 🐍 Python • 🐼 Pandas • 🗄️ SQLite • 📊 Data Analytics**

</div>
