## Project Overview
This project is a solution developed by **Team 1A** for the Rolls Royce Resource Adjustment Challenge. The challenge aims to create a tool that dynamically adjusts project activity durations based on resource data, recalculates critical paths, and highlights schedule impacts. This ensures efficient resource utilization and enhances decision-making.

## Folder Structure Summary
The project is organized into several key folders, each containing relevant scripts, data, and models used in the solution:

- **Python Modelling** – Contains Python scripts and notebooks for model training and predictive analysis.
- **Python Deployment** – Includes deployment scripts for executing the trained models.
- **Resource Capacity File Conversion** – Houses Excel files used for converting and processing resource capacity data.
- **XER Extract** – Includes extracted data from Primavera P6 XER files in CSV format.
- **Team 1A Solution** – Contains final reports, presentations, and summary files related to the project.

## Folder Descriptions

### **Python Modelling**
This folder contains scripts and models used to process and analyze project data.
- `Modelling.ipynb` – Jupyter notebook used for model development.
- `MinMaxtransformer.pkl` – Pickle file for scaling numerical data.
- `OHE_census.pkl` – Pickle file containing one-hot encoded categorical data.
- `rfr_remain_work_qty.p` – Pickle file storing a trained regression model.

### **Python Deployment**
Scripts and files needed for running the predictive models in deployment mode.
- `Deployed_model.py` – Python script that loads models, preprocesses data, and makes predictions.
- `deployment.ipynb` – Jupyter notebook demonstrating the deployment process.
- `results.csv` – Stores model prediction results.

### **Resource Capacity File Conversion**
Contains files used to process and convert resource capacity data.
- `1 - Finding Month Intervals between exp start exp end.xlsx` – Processes month intervals from start and end dates.
- `2 - melted resource capacity to pivoted form.xlsx` – Converts resource capacity data into a pivot table format.

### **XER Extract**
A collection of CSV files extracted from a Primavera P6 XER file for analysis and integration.
- Includes **TASK.csv, TASKRSRC.csv, PROJWBS.csv, RSRC.csv, SCHEDOPTIONS.csv, etc.**
- `XER Extraction_toJoinedData.py` – Python script that extracts data from an XER file and converts it into CSV format.

### **Team 1A Solution**
Final deliverables, presentations, and summary files.
- `Hitch Hackers.pptx` – Presentation summarizing the solution approach, challenges, and results.
- `Hitch Hacker.mp4` – Video explaining the solution.
- `JoinedTable_melted Wgraph Wdifference.xlsx` – Processed dataset for visualization.

## Info Section
This documentation was created as part of **Project:Hack** – a hackathon run by Projecting Success for the Project Data Analytics community. The solution integrates **Python, Power BI, and Primavera P6 data** to create a robust resource adjustment tool.

For a more detailed breakdown of each file, refer to `Detailed_Documentation.md`.
