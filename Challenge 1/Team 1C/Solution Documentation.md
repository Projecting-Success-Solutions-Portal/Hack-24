# **Dukhan Housing Project - Project Documentation**

## **📂 File Directory Structure**
The project files are structured as follows:

```
├── ChatGPT Convo                # SQL Query discussions and data exploration
├── Data                          # Resource allocation and scheduling datasets
├── Photos                        # Visual documentation (if applicable)
├── Power BI Tables               # Extracted Power BI tables for data analysis
├── Presentation                  # Summary presentations and reports
├── 3 month critical.xlsx         # Critical resource allocation over 3 months
├── DHUKAL HOUSING clean.xlsx     # Finalized cleaned project dataset
├── DHUKAL HOUSING.xlsx           # Another version of the housing project data
├── DHUKAL HOUSING clean (WIP).xlsx # Work-in-progress version of the dataset
├── DHUKAL HOUSING clean Test.xlsx # Test version for validation
├── Dynamic-Resource-Scheduling-Tool.pbix  # Power BI report for scheduling
├── Dynamic-Resource-Scheduling-Tool.pdf   # PDF export of Power BI insights
```

---

## **📜 Key Project Files & Insights**

### **1️⃣ SQL Query Documentation (ChatGPT Convo Folder)**
- Contains discussions and structured SQL queries related to **resource assignments (`TASKRSRC`)**, critical path analysis, and project scheduling.
- Queries help **extract, transform, and analyze** data for SQL-based scheduling solutions.

---

### **2️⃣ Resource Allocation Data (Data Folder)**
- Various Excel files tracking **resource capacity**:
  - **Available resources by quarter (Q1-Q4)**
  - **Resource constraints due to critical vs. non-critical activities**
  - **Resource availability fluctuations over a 6-month period**
- This data is used to **populate SQLP6DB.ScenarioData** for **resource forecasting**.

---

### **3️⃣ Power BI Analysis - Schedule & Timeline Impact**
📊 **Dynamic Resource Scheduling Insights (Power BI Report)**
- The **baseline project schedule** was originally set from **January 2013 to March 2015**.
- Due to scheduling changes, the **impacted completion date** was **delayed to July 16, 2015**.
- **107-day delay** resulted in extended resource allocation periods.

#### **🕒 Timeline Comparison**
| Metric | Baseline | Impacted |
|--------|---------|----------|
| **Duration** | 881 days | 988 days |
| **Completion Date** | March 31, 2015 | July 16, 2015 |
| **Duration Movement** | — | +107 days |

#### **🔹 Resource Planning Adjustments**
- **Increased duration affects workforce allocation**.
- **Critical tasks extended**, requiring **extra resource availability**.
- SQL queries will be used to **adjust resource forecasting models**.

---

### **4️⃣ Power BI Table Extraction (Power BI Tables Folder)**
- Extracted **activity schedules, WBS structures, and resource demand** for SQL integration.
- Includes:
  - **Activity schedules** (`Activity ID`, `Start`, `Finish`, `Total Float`, `Critical Flag`)
  - **Dependency mapping** (`Predecessors`, `Successors`)
  - **WBS Hierarchy** (`WBS Name` in certain files)
  - **Impact tracking** (`Variance - BL Start/Finish Dates`)

---

## **ℹ️ Project:Hack & Documentation Process**
This documentation was created as part of **Project:Hack** – a **hackathon** run by **Projecting Success** for the **Project Data Analytics community**.

- **Step 1:** Extracted raw project data (Excel, SQL, Power BI).
- **Step 2:** Developed SQL models for **resource forecasting**.
- **Step 3:** Integrated Power BI insights to adjust schedules.
- **Step 4:** Finalized documentation for the **Dukhan Housing Project**.

