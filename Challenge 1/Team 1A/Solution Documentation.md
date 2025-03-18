# Solution Documentation

## **Python Modelling**

### `Modelling.ipynb`
- Jupyter notebook used for model development and training.
- Implements data preprocessing, feature engineering, and machine learning models for predicting resource requirements.
- Uses **scikit-learn** for training regression models.
- Outputs processed datasets and trained models for later use.

### `MinMaxtransformer.pkl`
- Pickle file containing a **MinMaxScaler** transformer used for feature scaling.
- Normalizes numerical data between a fixed range to improve model performance.
- Used in both training and deployment phases.

### `OHE_census.pkl`
- Pickle file containing a **One-Hot Encoder** (OHE) model for encoding categorical data.
- Converts categorical features into numerical format for machine learning models.

### `rfr_remain_work_qty.p`
- Pickle file containing a trained **Random Forest Regressor** model.
- Used for predicting remaining work quantity based on input task and resource data.

---

## **Python Deployment**

### `Deployed_model.py`
- Python script for deploying the trained model.
- Loads the pre-trained models (`MinMaxtransformer.pkl`, `OHE_census.pkl`, `rfr_remain_work_qty.p`).
- Preprocesses input data and generates predictions.
- Saves results to `results.csv`.

### `deployment.ipynb`
- Jupyter notebook demonstrating the deployment process.
- Shows data preprocessing, model loading, and prediction generation.

### `results.csv`
- Stores the model's prediction output for further analysis.

---

## **Resource Capacity File Conversion**

### `1 - Finding Month Intervals between exp start exp end.xlsx`
- Processes month intervals between expected start and end dates.
- Used for analyzing resource capacity timelines.

### `2 - melted resource capacity to pivoted form.xlsx`
- Converts raw resource capacity data into a pivot table format.
- Enhances data structure for Power BI and visualization tools.

---

## **XER Extract**

### `XER Extraction_toJoinedData.py`
- Extracts **Primavera P6 XER** data and converts it into **CSV format**.
- Splits XER sections into separate tables such as `TASK.csv`, `RSRC.csv`, and `PROJWBS.csv`.
- Uses **pandas** for processing and merging extracted data.

### Key Extracted Files:
- `TASK.csv` – Contains task-level project data.
- `TASKRSRC.csv` – Links tasks to their assigned resources.
- `PROJWBS.csv` – Work Breakdown Structure (WBS) hierarchy.
- `RSRC.csv` – Resource data including roles and availability.
- `SCHEDOPTIONS.csv` – Scheduling options extracted from Primavera P6.

---

## **Team 1A Solution**

### `JoinedTable_melted Wgraph Wdifference.xlsx`
- Processed dataset used for visualization and analysis.

---

## **Integration & Usage**
1. **Preprocess Data** – Use `XER Extraction_toJoinedData.py` to convert XER files to CSV.
2. **Train Models** – Run `Modelling.ipynb` to generate trained models.
3. **Deploy Models** – Use `Deployed_model.py` or `deployment.ipynb` to generate predictions.
4. **Analyze Results** – Use Power BI dashboards and `results.csv` for insights.

For further details, refer to `README.md` for a high-level overview.

