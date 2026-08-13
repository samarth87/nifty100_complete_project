📊 Mutual Fund Analytics
End-to-End Mutual Fund Data Analytics & Performance Analysis Platform

A data-driven analytics project for exploring, cleaning, analyzing and evaluating mutual fund performance using Python, SQL, statistical analysis and visualization.

📈 Data Engineering • Exploratory Data Analysis • Performance Analytics • Financial Insights

🧭 Overview

Mutual Fund Analytics is an end-to-end data analytics project focused on transforming mutual fund data into meaningful financial insights.

The project covers the complete analytics workflow:

Raw Data → Data Cleaning → Data Validation → Database → EDA → Performance Analysis → Visualizations → Insights

The objective is to make mutual fund data easier to understand and analyze by examining important factors such as fund performance, NAV trends, returns, risk-related indicators and fund characteristics.

This project was developed as part of the Bluestock Mutual Fund Analytics Capstone.

🎯 Project Objectives

The main objectives of this project are to:

📥 Collect and organize mutual fund datasets
🧹 Clean and standardize raw financial data
🔍 Perform exploratory data analysis
📊 Analyze mutual fund performance
📈 Study NAV and historical trends
🗄️ Store structured data in a relational database
🧪 Validate data quality and consistency
📉 Generate analytical charts and reports
💡 Extract meaningful insights from financial data
📝 Document the complete analytics workflow
🔎 What Does This Project Analyze?

The project focuses on several important dimensions of mutual fund analytics.

📌 Fund Master Data

Analysis of fundamental information related to mutual fund schemes, including:

Fund / scheme information
Categories and classifications
Fund characteristics
Scheme-level attributes
📌 NAV Analysis

Historical NAV data is processed and analyzed to understand:

NAV movement
Historical trends
Data consistency
Fund-level performance patterns
📌 Performance Analytics

The project examines mutual fund performance using historical data and analytical calculations.

This helps answer questions such as:

Which funds have performed strongly?
How does performance vary across funds?
What are the historical return patterns?
Which funds show consistent performance?
📌 Exploratory Data Analysis

EDA is used to identify:

Distribution patterns
Missing values
Outliers
Data inconsistencies
Fund-level trends
Relationships between important variables
🏗️ Project Architecture
                    ┌─────────────────────┐
                    │     Raw Data        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Data Ingestion    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Data Cleaning &     │
                    │ Standardization     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Data Validation &   │
                    │ Quality Checks      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   SQLite Database   │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
          ┌─────────────────┐   ┌──────────────────┐
          │ Exploratory     │   │ Performance      │
          │ Data Analysis   │   │ Analytics        │
          └────────┬────────┘   └────────┬─────────┘
                   │                     │
                   └──────────┬──────────┘
                              ▼
                    ┌─────────────────────┐
                    │ Charts & Reports    │
                    └─────────────────────┘


🛠️ Technology Stack
TechnologyPurpose	
🐍 Python	Data processing and analytics
🐼 Pandas	Data cleaning and manipulation
📓 Jupyter Notebook	Exploratory and analytical work
🗄️ SQL / SQLite	Structured data storage and querying
📊 Data Visualization	Charts and analytical insights
📁 CSV / Data Files	Source and processed datasets
🔧 Python Scripts	Automation of data pipeline
📝 Markdown	Documentation
📂 Repository Structure
Mutual-fund-Analytics/
│
├── 📁 charts/
│   └── Generated visualizations
│
├── 📁 data/
│   └── Raw and processed datasets
│
├── 📁 notebooks/
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── fund_master_analysis.ipynb
│
├── 📁 outputs/
│   └── Analytical outputs
│
├── 📁 reports/
│   ├── data_quality_notes.txt
│   └── data_quality_summary.txt
│
├── 📁 sql/
│   └── SQL scripts and database queries
│
├── 📄 clean_nav.py
├── 📄 clean_performance.py
├── 📄 clean_transactions.py
├── 📄 create_database.py
├── 📄 data_dictionary.md
├── 📄 data_ingestion.py
├── 📄 live_nav_fetch.py
├── 📄 load_data.py
├── 📄 run_pipeline.py
├── 📄 verify_data.py
├── 📄 check_tables.py
│
├── 🗄️ bluestock_mf.db
├── 📋 requirements.txt
├── 📊 Mutual Funds Analytics.pptx
├── 📄 Bluestock Mutual Fund Analytics Platform.docx
└── 📖 README.md
