A script for Rob to automate the task he had to perform that was extremely labourous.  

<ins>Tasks Performed by Script</ins>  
Copy Column 3 from all spreadsheets in Folder Y → Combine them as separate columns into a new spreadsheet (Spreadsheet Y) and place in Folder X.  

 <ins> Structure</ins>  
 Parent Folder  
│  
├── Folder X  
│   └── run_script.py    ← Script goes here  
│   └── Spreadsheet Y.xlsx  ← This will be created by the script  
    └── Folder Y  
      ├── spreadsheet_1.xlsx  
      ├── spreadsheet_2.xlsx  
      └── spreadsheet_3.xlsx  
