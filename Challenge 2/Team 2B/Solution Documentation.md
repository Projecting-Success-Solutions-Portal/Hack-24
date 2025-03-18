# Solution Documentation

## File Directory Overview
This project contains the following key files:

- **Power BI Dashboard User Guide (DOCX)** – A guide for navigating and using Power BI dashboards.
- **Pre Post Mitigation Differences (PBIX)** – A Power BI report analyzing cost differences before and after mitigation.
- **Python Linear Regression Script (TXT)** – A script that models post-mitigation costs based on pre-mitigation values.
- **Risks - Hackathon (XLSX)** – An Excel-based heat map of resourcing risks.
- **Data Cleanse (DOCX)** – Instructions for cleaning and standardizing Risk IDs.
- **Hackerthon - Trending Graph (PBIX)** – A Power BI dashboard showing trends in risk data over time.

---

## Specific File Details

### **Power BI Dashboard User Guide (DOCX)**
This document explains how to navigate and interact with Power BI dashboards, covering:
- Filters & Slicers
- Visual interactions
- Exporting data
- Troubleshooting tips

### **Pre Post Mitigation Differences (PBIX)**
This Power BI dashboard analyzes cost variations before and after mitigation efforts.

#### **Data Transformations in Power Query**
- Loads data from an Excel file (**250304 PDAC Hack Risk data v5.0.xlsx**)
- Retrieves and processes sheets: `Lists`, `Fields`, `Mitigations`, `Risks`
- Promotes headers for better readability
- Cleans column types (text, number, date) to ensure accurate calculations
- Generates a **unique identifier (UniRis)** using `Report Date`, `Project ID`, and `Risk ID`
- Removes errors and blank rows for cleaner analysis
- **Scales cost values** (`Pre Cost`, `Post Cost`) by multiplying them by **1000**

### **Python Linear Regression Script (TXT)**
This script predicts **post-mitigation costs** using **linear regression** based on pre-mitigation data.

**Key Features:**
- Reads risk data from an Excel file
- Uses `scipy.stats` for linear regression modeling
- Generates a trend line to estimate **post-mitigation cost** for given `Pre Cost` values
- Plots the relationship between **Pre vs. Post Cost**

### **Risks - Hackathon (XLSX)**
An **Excel-based heat map** analyzing **resourcing risks** within projects. Includes:
- Risk classifications
- Cost impact analysis
- Mitigation actions tracking

### **Data Cleanse (DOCX)**
This document provides **Risk ID standardization techniques** using **Excel formulas and Python scripts**.

#### **Excel-based Cleaning Process:**
- Standardizes **Risk ID** format (e.g., adds missing zeros, removes extra spaces)
- Ensures all IDs start with the prefix `RISK`

#### **Python-based Cleaning Process:**
- Uses `pandas` and `re` (regex) for automated data cleansing
- Removes invalid characters, corrects spelling errors, and formats text fields

### **Hackerthon - Trending Graph (PBIX)**
A Power BI dashboard analyzing **trends in risk-related costs**.

#### **Data Transformations in Power Query**
- Loads and cleans data from **Excel**
- Applies structured transformations:
  - Promotes headers
  - Cleans column types
  - Creates **unique risk identifiers**
- **Analyzes cost trends over time** using DAX calculations

---

## Project Info Section
This documentation was created as part of **Project:Hack** – a hackathon organized by **Projecting Success** for the **Project Data Analytics** community.

