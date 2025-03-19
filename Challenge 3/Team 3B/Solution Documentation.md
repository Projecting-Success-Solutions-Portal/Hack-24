# Solution Documentation

## 📂 File Directory
```
Hack 24 Challenge 3/
│
├── Data 3/
│   ├── 250304 PDAC Hack Risk data v5.0.xlsx
│   ├── Configure Source Datasets for Risk Ease (H24).txt
│   ├── Risk Ease (H24).pbix
│
├── hidden_ipynb_checkpoints/
│   ├── Hack24_Challenge_3_Solution-checkpoint.ipynb
│   ├── Hack24_chatbot-checkpoint.ipynb
│
├── 250304 PDAC Hack Risk data v5.0 clean.xlsx
├── 250304 PDAC Hack Risk data v5.0 clean_edited.xlsx
├── Hack24_Challenge_3_Solution.ipynb
├── risk_mitigations.db
├── risk_mitigations_export.xlsx
├── Risks_and_Costs_for_All_Projects.png
```

---

## 📌 Specific Files & Documentation

### **1️⃣ Hack24_Challenge_3_Solution.ipynb**
- **Purpose**: Performs data cleaning and risk processing using SQLite.
- **Key Functions**:
  - Cleans raw risk data.
  - Creates an SQLite database and tables.
  - Inserts processed data into the database.
  - Implements a chatbot query system for data interaction.
  - Generates bar charts for "Risks and Costs for ALL_PROJECTS" and specific projects.
  - Provides data visualization as an alternative to Power BI.

### **2️⃣ Hack24_chatbot-checkpoint.ipynb**
- **Purpose**: Stores metadata and checkpoint information for the chatbot.

### **3️⃣ Risk Ease (H24).pbix**
- **Purpose**: Power BI report providing risk analysis and mitigation insights.
- **Key Insights**:
  - **Risk Mitigation Dashboard** – Tracks risk trends and evaluates mitigation effectiveness.
  - **Risk Summary** – Provides an overview of risk exposure.
  - **Risk Trend Analysis** – Displays changes in risk levels over time.
  - **Risk Scoring** – Assigns scores based on cost, probability, and resolution time.
  - **Data Confidence** – Identifies inconsistencies and missing risk data.
- **Setup Instructions**:
  - The report relies on **250120 PDAC Hack Risk data v4.1.xlsx**.
  - Follow steps in `Configure Source Datasets for Risk Ease (H24).txt` to update the data connection.

### **4️⃣ 250304 PDAC Hack Risk data v5.0.xlsx**
- **Purpose**: Contains structured risk data used for analysis in Power BI and SQLite.
- **Key Data**:
  - **Risk Details** – Descriptions, categories, and ownership.
  - **Mitigation Plans** – Tracks risk reduction efforts.
  - **Financial Impact** – Pre- and post-mitigation cost estimates.
  - **Data for Power BI** – Used as an input for `Risk Ease (H24).pbix`.
- **Usage**:
  - Ensure proper file path configuration when connecting to Power BI.
  - Used in `Hack24_Challenge_3_Solution.ipynb` for risk analysis.

### **5️⃣ risk_mitigations.db**
- **Purpose**: SQLite database storing structured risk mitigation data.
- **Tables**:
  - `D_Risks` – Risk details.
  - `D_Mitigations` – Captures mitigation actions.
  - `F_RiskHierarchy`, `F_DateCreated`, `F_Version` – Additional metadata.
- **Usage**:
  - Access via SQLite commands for data queries.
  - Used in **`Hack24_Challenge_3_Solution.ipynb`** for risk processing.

### **6️⃣ risk_mitigations_export.xlsx**
- **Purpose**: Exported dataset from `risk_mitigations.db`.
- **Key Data**:
  - **Risk ID & Description** – Individual risk details.
  - **Mitigation Actions** – Steps taken to reduce risks.
  - **Pre & Post-Mitigation Costs** – Financial impact comparison.
  - **Status & Owner** – Progress tracking.
- **Usage**:
  - Can be re-imported into SQLite for further processing.
  - Useful for Excel-based risk analysis.

### **7️⃣ Risks_and_Costs_for_All_Projects.png**
- **Purpose**: A visualization showing risk costs across projects.
- **Key Insights**:
  - **Pre vs. Post-Mitigation Costs** – Highlights financial risk reduction.
  - **High-Risk Projects** – Identifies significant risk exposure.
  - **Trend Insights** – Shows improvement or problem areas in risk mitigation.
- **Usage**:
  - Used in `Hack24_Challenge_3_Solution.ipynb` for risk visualization.
  - Can be included in presentations or reports.

---

## ℹ️ Project Information
**This documentation was created as part of Project:Hack – a hackathon run by Projecting Success for the Project Data Analytics community.**

