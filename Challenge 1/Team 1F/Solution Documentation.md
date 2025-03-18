# Solution Documentation

## File Directory
This project consists of the following key files:
- **24HackChallenge_TokenRedacted.pbix** – Power BI report for activity tracking.
- **Dynamic_Scheduling.ipynb** – Jupyter Notebook for scheduling updates using an EA Simple algorithm.
- **Hack Trial.ipynb** – Jupyter Notebook for calculating percentage completion of tasks.

## Specific Files
### **24HackChallenge_TokenRedacted.pbix**
**Purpose:**  
This Power BI report is designed to **display a table of activities** along with their associated data, including variances. It also includes a structured table that serves as an input for **Power Automate** to facilitate **automated schedule updates**.

**Key Features:**
- **Activity Table**: Displays a structured list of activities and their metadata.
- **Variance Analysis**: Highlights deviations in schedule durations.
- **Power Automate Integration**: Outputs a structured table used for automated schedule updates.

**Data Sources:**
- **P6 Cloud Service** (Primavera P6)

**Dependencies:**
- **Power Automate**: Used to process and update schedules based on Power BI outputs.
- **Power Query Scripts** (if applicable)
- **External Data Connections** (Primavera P6 Cloud Service)

---

### **Dynamic_Scheduling.ipynb**
**Purpose:**  
This Jupyter Notebook performs **scheduling updates** using an **EA Simple (Evolutionary Algorithm - Simple) approach** to optimize scheduling dynamically.

**Key Features:**
- **Data Loading**: Reads and processes scheduling data from **CSV files**.
- **EA Simple Algorithm**: Applies an **Evolutionary Algorithm (EA Simple)** to optimize and adjust scheduling dynamically.
- **Data Processing**: Uses **pandas** to structure and manipulate data.
- **Visualization**: Generates insights, potentially through **matplotlib** plots.

**Data Inputs:**
- **CSV files** containing scheduling data.

**Outputs:**
- A **pandas DataFrame** representing the optimized schedule.
- Potential visualizations of scheduling outcomes.

**Dependencies:**
- **deap** (for EA Simple algorithm and optimization)
- **networkx** (for graph-based scheduling structures)
- **numpy** (for numerical operations)
- **pandas** (for data handling)
- **random, datetime** (for randomization and time-based scheduling)
- **matplotlib** (for visualizing scheduling results)

---

### **Hack Trial.ipynb**
**Purpose:**  
This Jupyter Notebook calculates the **percentage completion** of tasks in a project based on extracted scheduling data.

**Key Features:**
- **Data Loading**: Reads task completion data from **CSV files** (extracted from an **XER file**).
- **Completion Calculation**: Implements the function **`calculate_percentage_completion`** to determine project progress.
- **Data Processing**: Uses **pandas** to structure and manipulate data.

**Data Inputs:**
- **CSV files** extracted from an **XER file**.

**Outputs:**
- A **string output** representing the **percentage of project completion**.

**Dependencies:**
- **deap** (for evolutionary computation, if needed)
- **networkx** (for handling task dependencies)
- **numpy** (for numerical calculations)
- **pandas** (for data handling and manipulation)
- **random, datetime** (for handling task durations and randomness)
- **matplotlib** (for visualization, if applicable)

---

## Info Section
This documentation was created as part of **Project:Hack** – a hackathon run by **Projecting Success** for the **Project Data Analytics** community.

