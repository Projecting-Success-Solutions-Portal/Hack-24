### Project Documentation

## File Directory
- **Resource Analysis Dashboard.pbix**: Power BI dashboard file containing resource allocation and activity tracking insights.
- **ACTVCODE.csv** (Source data): CSV file imported into the Power BI dashboard containing activity code data.

## Specific Files
### **Resource Analysis Dashboard.pbix**
This Power BI dashboard provides insights into resource allocation and activity tracking for project management.

#### **Data Sources**
The dataset used in this dashboard includes:
- **ACTVCODE.csv**: A CSV file containing activity code data, imported from:
  ```
  C:\[redacted]\ACTVCODE.csv
  ```
- The CSV file contains the following fields after transformation:
  - `actv_code_id` (Integer)
  - `actv_code_type_id` (Integer)
  - `actv_code_name` (Text)
  
  **Removed Fields**: `color`, `parent_actv_code_id`, `seq_num`, `short_name`

#### **Dashboard Overview**
The report visualizes task completion, project timelines, and approvals, including:
- **Task Names** such as:
  - Anti Termite Treatment
  - Ceiling Works
  - Block Work
  - Column Drawings
  - Carpentry & Joinery Works
  - Approval of Cost Proposal
- **Timeframe Covered**: November 2012 – March 2015
- **Project Milestones**: Approval of site design, cost proposals, and various construction-related tasks.

## Info Section
This documentation was created as part of Project:Hack – a hackathon run by Projecting Success for the Project Data Analytics community.

