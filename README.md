Data-Driven Stock Analysis: Nifty 50 Market Trends
Project Overview

This project focuses on analyzing the performance of Nifty 50 stocks over a one-year period using data-driven techniques.
The data is originally provided in YAML format, organized month-wise, and is processed using Python to generate meaningful insights and visualizations.

The project demonstrates data extraction, cleaning, transformation, analysis, and visualization, enabling investors and analysts to better understand market trends.

Problem Statement

To build a stock performance analysis system that:

Processes daily stock data (Open, High, Low, Close, Volume)

Identifies top-performing and worst-performing stocks

Provides clear insights through visualizations

Supports decision-making for investors and analysts

Business Use Cases

Identify top gainers and losers

Understand overall market performance

Analyze stock-wise yearly returns

Enable data-driven investment insights

Tech Stack Used
Languages & Libraries

Python

Pandas – Data processing & analysis

Matplotlib – Visualizations

PyYAML – YAML parsing

Visualization Tools

Streamlit – Interactive dashboard

Power BI – Business Intelligence visualization (conceptual integration)

📁 Project Structure
data_driven_stock_analysis/
│
├── data/
│   └── raw_yaml/              # Original YAML files (month-wise folders)
│
├── src/
│   ├── yaml_to_csv.py         # Converts YAML files to CSV
│   ├── yearly_return.py       # Calculates yearly stock returns
│   └── top_gainers_losers.py  # Identifies top gainers & losers
│
├── output/
│   ├── nifty50_all_data.csv
│   ├── yearly_returns.csv
│   ├── top_5_gainers.csv
│   └── top_5_losers.csv
│
├── streamlit_app.py           # Streamlit dashboard
├── README.md
└── requirements.txt

Project Workflow

Data Ingestion

Stock data provided in YAML format across multiple folders

Data Transformation

YAML files parsed and merged into a single CSV using Python

Data Analysis

Yearly return calculated using opening and closing prices

Top 5 gainers and top 5 losers identified

Visualization

Streamlit dashboard for interactive exploration

Charts created using Matplotlib

Power BI integration designed using processed CSV files

Streamlit Dashboard

The Streamlit application provides:

Raw stock data view

Yearly return table and bar chart

Top gainers

Top losers

How to Run Streamlit App
streamlit run streamlit_app.py

Power BI Integration (Design Level)

The cleaned CSV output can be directly imported into Power BI Desktop to create:

Stock-wise average price dashboards

Yearly trend analysis

Volume-based insights

Note: Due to environment constraints, Power BI dashboards are described as part of the project design and can be easily implemented using the provided CSV files.

Key Outcomes

Successfully converted raw YAML data into structured CSV

Generated meaningful stock performance insights

Built an interactive visualization dashboard

Delivered a complete end-to-end data analytics solution

Future Enhancements

Integrate MySQL/PostgreSQL for persistent storage

Add volatility and correlation analysis

Deploy Streamlit app on cloud

Implement real-time data ingestion

Create advanced Power BI dashboards

Coding Standards & Practices

Followed PEP 8 Python coding standards

Modular and maintainable code

Clear folder structure

Well-documented scripts

Author

[Gomathi Boopathy]
Domain: Finance / Data Analytics

📎 Submission Notes

GitHub repository is public

Project is fully reproducible

