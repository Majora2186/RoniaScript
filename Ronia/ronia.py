# -*- coding: utf-8 -*-
"""
 Copy Column 3 from all spreadsheets in Folder Y → Combine them as separate 
 columns into a copy of the template spreadsheet (Compiled Ronia Results) in Folder X.
 
 Parent Folder
│
├── Folder X
│   └── run_script.py    ← Script goes here.
│   └── Compiled Ronia Results.xlsx  ← This will be created by the script.
│   └── template.xlsx  ← This is the template that the data is pasted into.
│
└── Folder Y
    ├── spreadsheet_1.xlsx
    ├── spreadsheet_2.xlsx
    └── spreadsheet_3.xlsx
"""

# Import os to manipulate files and folders and pandas for Spreadsheets
import os
import sys
import subprocess
import openpyxl
import shutil
#Brings in Python's standard tool for reading and parsing
import json
# For adding the current date and time to the Compiled Ronia results spreadsheet
from datetime import datetime

#--- Dependency check section ---
# required_packages = ["openpyxl", "os", "sys", "subprocess", "openpyxl", "shutil"]

# for package in required_packages:
#     try:
#         __import__(package)
#         print(f"✅ {package} is already installed.")
#     except ImportError:
#         print(f"📦 {package} not found. Installing...")
#         subprocess.check_call([sys.executable, "-m", "pip", "install", package])
#         print(f"✅ {package} installed successfully.")


import pandas as pd
# Not sure if I need to set pandas as pd somehow seperately as it gets installed through my loop above or whether it will just work.

# This checks if the sysem is windows or linux and clears the script.
os.system('cls' if os.name == 'nt' else 'clear')


# Define Folder X as the directory where the script is located.
folder_x = os.path.dirname(os.path.abspath(__file__))
# This is a variable to store the location of Folder Y but it hasn't yet been created.
folder_y = os.path.join(folder_x, "Folder Y")
# Define the path to the excel template file, so that it can be copied later
template_path = os.path.join(folder_x, "template.xlsx")

# This is temporarily displaying the path of both folders for debugging.
#print("Folder x ="+folder_x)
#print("Folder y ="+folder_y)
print("")

if not os.path.isdir(folder_y):
    os.makedirs(folder_y, exist_ok=True)
    
print("-" * 30)
print("Steve's Ronia Results Script")
print("-" * 30)
print("")

response = input("Are results loaded?\nWARNING: All files in Folder Y will be permanently DELETED after processing.\nContinue? [Y]/N: ").strip().lower()

if response in ["n", "no"]:
    print("")
    print("Load results and then re-run script. Stopping...")
    print("")
    print("-" * 30)
    exit(0)
else:
    print("")
    print("Processing...")
    print("")
    

# Checking if excel files are present and list them.
excel_files = []

for root, dirs, files in os.walk(folder_y):
    for file in files:
        if file.endswith('.csv'):
            excel_files.append(os.path.join(root, file))


if not excel_files:
    print("No Excel files found in Folder Y.")
    print("")
    print("Stopping Script.")
    print("-" * 30)
    input("Press Enter to exit...")
    sys.exit(0)


# My for loop for iterating through all spreadsheets.
combined_df = pd.DataFrame()

# This is the line that creates dots for each file worked on.
for file_path in excel_files:
    print('.', end='', flush=True)
    
    # I think this is where the data is extracted or at least read. This comment can be verified with an Ai.
    csv_df = pd.read_csv(file_path, usecols=[2])
    csv_df.columns = [0]
    # Find the json file in the folder
    json_path = os.path.join(os.path.dirname(file_path), 'result.json')
    # Open file and give python the ability to read it.
    with open(json_path, 'r') as json_file:
        # Reads the raw text from the file and translates it into a Python "dictionary". Save into the variable json_data.
        json_data = json.load(json_file)
        # Extract standard data points
        sample_id = json_data.get("sampleId", "")
        cassette_code = json_data.get("cassetteIdentifierCode", "")
        lot_code = json_data.get("lotCode", "")
        
        # Extract nested data points
        protocol_name = json_data.get("protocol", {}).get("name", "")
        protocol_version = json_data.get("protocol", {}).get("version", "")
        result_val = json_data.get("result", {}).get("value", "")
        
        # Extract raw endTime for future splitting
        raw_end_time = json_data.get("endTime", "")
        end_date = raw_end_time.split('T')[0] if 'T' in raw_end_time else ""
        end_time = raw_end_time.split('T')[1][:5] if 'T' in raw_end_time else ""

        # Add these scraped data points to the spreadsheet at the top
        # This is the line that decides the order the json scrape is added to the spreadsheet
        json_list = [end_time, end_date, cassette_code, sample_id, result_val, protocol_name, protocol_version, lot_code]
        # This converts my python list into a dataframe
        json_df = pd.DataFrame(json_list)
        # This adds the dataframes together
        single_result_column = pd.concat([json_df, csv_df], ignore_index=True)
        combined_df = pd.concat([combined_df, single_result_column], axis=1)



    # Use just the filename (without extension) as column name
    # Currently commented out because we no longer do this but left in JIC.
    #folder_name = os.path.basename(os.path.dirname(file_path))
    #df.columns = [folder_name]


print("")
print(f"\nTotal spreadsheets processed: {len(excel_files)}")
print("")
print("Creating Excel File...")


# Put the dataframe into an excel spreadsheet

#The below line creates the spreadsheet
#combined_df.to_excel(output_path, index=False)

# 1. Get current time and total number of results
current_time = datetime.now().strftime("%d %b %y - %H.%M")
total_results = combined_df.shape[1]

# 2. Loop through the results in chunks of 40
for i in range(0, total_results, 40):
    part_num = (i // 40) + 1
    chunk_df = combined_df.iloc[:, i:i+40]
    
    # 3. Create dynamic filename and path
    batch_filename = f"Compiled Ronia Results - {current_time} - Part {part_num}.xlsx"
    batch_output_path = os.path.join(folder_x, batch_filename)
    
    # 4. Copy template and paste the chunk
    shutil.copy(template_path, batch_output_path)
    with pd.ExcelWriter(batch_output_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        chunk_df.to_excel(writer, sheet_name='Raw Data', startcol=2, startrow=0, index=False, header=False)


print("")
print("Process complete")

# Delete and replace Compiled Ronia Results
shutil.rmtree(folder_y)
os.makedirs(folder_y, exist_ok=True)

print("-" * 30)
