import csv

def extract_xer_sections(xer_file):
    """
    Reads a Primavera P6 .XER file and extracts readable sections into CSV files.
    """
    sections = {}
    current_section = None
    
    with open(xer_file, "r", encoding="latin-1") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            # Identify new section headers (e.g., %T, %F, %R denote different tables)
            if line.startswith("%T"):
                current_section = line.replace("%T", "").strip()
                sections[current_section] = []
            elif current_section:
                sections[current_section].append(line.split("\t"))  # Split by tab delimiter

    # Save each section as a CSV file
    for section, rows in sections.items():
        filename = f"{section}.csv"
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)
        print(f"Extracted: {filename}")

# Usage example
extract_xer_sections("DUKHAN HOUSING PROJECT PHASE IX Original.xer")


RSRC =    pd.read_csv(r'RSRC.csv')
TASK =    pd.read_csv(r'TASK.csv')
PRJWBS =  pd.read_csv(r'PROJWBS.csv')
CAL =     pd.read_csv(r'CALENDAR.csv')

TASK_RSRC = TASK.merge(RSRC, on="rsrc_id", how="left")

# Rename _x columns and drop _y columns
TASK_RSRC.columns = [col[:-2] if col.endswith('_x') else col for col in TASK_RSRC.columns]
TASK_RSRC = TASK_RSRC.loc[:, ~TASK_RSRC.columns.str.endswith('_y')]

# Now merge TASK_RSRC with WBS instead of RSRC (assuming wbs_id belongs to WBS)
TASK_RSRC_WBS = TASK_RSRC.merge(PRJWBS, on="wbs_id", how="left")

# Rename _x columns and drop _y columns after second merge
TASK_RSRC_WBS.columns = [col[:-2] if col.endswith('_x') else col for col in TASK_RSRC_WBS.columns]
TASK_RSRC_WBS = TASK_RSRC_WBS.loc[:, ~TASK_RSRC_WBS.columns.str.endswith('_y')]


TASK_RSRC_WBS.to_csv('joined_TASK_RSRC_WBS_with pivot table on total time difference.csv', index = False)
