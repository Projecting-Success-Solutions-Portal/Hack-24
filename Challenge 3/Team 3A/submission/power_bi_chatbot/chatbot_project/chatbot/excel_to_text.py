import pandas as pd
import os
import re
from datetime import datetime
from tqdm import tqdm

def process_excel_to_text(excel_file, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    try:
        # Read the Excel workbook
        print(f"Opening Excel file: {excel_file}")
        xl = pd.ExcelFile(excel_file)
    except Exception as e:
        print(f"Error opening Excel file: {e}")
        return
    
    # Process each sheet
    sheet_names = [s for s in ['Risks', 'Mitigations'] if s in xl.sheet_names]
    for sheet_name in tqdm(sheet_names, desc="Processing sheets"):
        try:
            print(f"\nReading {sheet_name} sheet...")
            df = pd.read_excel(xl, sheet_name=sheet_name)

            if 'Report Date' not in df.columns:
                print(f"Warning: 'Report Date' column not found in {sheet_name} sheet. Skipping.")
                continue
            
            print(f"Converting dates in {sheet_name} sheet...")

            df['Valid_Date'] = True
            date_series = pd.to_datetime(df['Report Date'], errors='coerce')

            df.loc[date_series.isna(), 'Valid_Date'] = False

            invalid_count = df[~df['Valid_Date']].shape[0]
            if invalid_count > 0:
                print(f"Warning: {invalid_count} rows in {sheet_name} sheet have invalid date formats and will be skipped.")

            df = df[df['Valid_Date']].copy()
            df['Report Date'] = pd.to_datetime(df['Report Date'])

            if df.empty:
                print(f"No valid data found in {sheet_name} sheet after filtering invalid dates. Skipping.")
                continue
            
            df['Month'] = df['Report Date'].dt.strftime('%B').str.lower()
            df['Year'] = df['Report Date'].dt.year
            
            grouped = df.groupby(['Month', 'Year'])

            group_items = list(grouped)
            for (month, year), group_df in tqdm(group_items, desc=f"Exporting {sheet_name} text files"):
                try:
                    output_df = group_df.drop(['Month', 'Year', 'Valid_Date'], axis=1)
                    
                    def clean_text(text):
                        if isinstance(text, str):
                            text = re.sub(r'[^\w\s]', ' ', text)
                            text = re.sub(r'\s+', ' ', text)

                            text = text.strip()
                        return text

                    output_df = output_df.applymap(clean_text)
                    

                    num_parts = 5
                    rows_per_part = len(output_df) // num_parts
                    remainder = len(output_df) % num_parts
                    start_row = 0

                    for part in range(1, num_parts + 1):
                        end_row = start_row + rows_per_part + (1 if part <= remainder else 0)
                        part_df = output_df.iloc[start_row:end_row]
                        
                        # Create file name
                        file_prefix = 'risks' if sheet_name == 'Risks' else 'mitigation'
                        file_name = f"{file_prefix}_{month}_{year}_{part}.txt"
                        file_path = os.path.join(output_folder, file_name)
                        
                        # Convert the DataFrame to plain text
                        text_content = part_df.to_string(index=False, header=False, na_rep="NA")
                        
                        # Write text content to text file
                        with open(file_path, 'w') as f:
                            f.write(text_content)
                        
                        start_row = end_row
                    
                except Exception as e:
                    print(f"Error exporting {sheet_name} data for {month} {year}: {e}")
        
        except Exception as e:
            print(f"Error processing {sheet_name} sheet: {e}")
    
    print(f"\nProcessing complete. Text files exported to: {output_folder}")

if __name__ == "__main__":
    excel_file_path = "chatbot/data/250304 PDAC Hack Risk data v5.0.xlsx"
    output_folder_path = "chatbot/exported_txt"
    
    process_excel_to_text(excel_file_path, output_folder_path)
