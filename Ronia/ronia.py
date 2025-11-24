# -*- coding: utf-8 -*-
"""
 Copy Column 3 from all spreadsheets in Folder Y → Combine them as separate 
 columns into a new spreadsheet (Spreadsheet Y) in Folder X.
 
 Parent Folder
│
├── Folder X
│   └── run_script.py    ← Script goes here
│   └── Spreadsheet Y.xlsx  ← This will be created by the script
│
└── Folder Y
    ├── spreadsheet_1.xlsx
    ├── spreadsheet_2.xlsx
    └── spreadsheet_3.xlsx
"""
import os
import sys
import subprocess
import openpyxl

#--- Dependency check section ---
# required_packages = ["openpyxl", "os", "sys", "subprocess"]

# for package in required_packages:
#     try:
#         __import__(package)
#         print(f"✅ {package} is already installed.")
#     except ImportError:
#         print(f"📦 {package} not found. Installing...")
#         subprocess.check_call([sys.executable, "-m", "pip", "install", package])
#         print(f"✅ {package} installed successfully.")



# Import os to manipulate files and folders and pandas for Spreadsheets

import pandas as pd
# Not sure if I need to set pandas as pd somehow seperately as it gets installed through my loop above or whether it will just work.

# This checks if the sysem is windows or linux and clears the script.
os.system('cls' if os.name == 'nt' else 'clear')


# Define Folder X as the directory where the script is located.
folder_x = os.path.dirname(os.path.abspath(__file__))
# This is a variable to store the location of Folder Y but it hasn't yet been created.
folder_y = os.path.join(folder_x, "Folder Y")
# Define the path for the final excel spreadsheet created at the end.
output_path = os.path.join(folder_x, "Spreadsheet Y.xlsx")

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

response = input("Have results been loaded into Folder Y? [Y]/N: ").strip().lower()

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
    exit(0)

# My for loop for iterating through all spreadsheets.
combined_df = pd.DataFrame()

for file_path in excel_files:
    print('.', end='', flush=True)
    
    df = pd.read_csv(file_path, usecols=[2])

    # Use just the filename (without extension) as column name
    folder_name = os.path.basename(os.path.dirname(file_path))
    df.columns = [folder_name]

    combined_df = pd.concat([combined_df, df], axis=1)

print("")
print(f"\nTotal spreadsheets processed: {len(excel_files)}")
print("")
print("Creating Excel File...")


# Put the dataframe into an excel spreadsheet
combined_df.to_excel(output_path, index=False)
print("")
print("Process complete")
print("-" * 30)
