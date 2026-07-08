# Ronia Results Compiler

## What the Script is For
The Ronia Results Compiler is a Python automation tool designed to streamline the processing of laboratory test results. It automatically compiles individual results into a structured, easily readable master Excel template for downstream analysis.

## How it Works
1. **Data Scraping:** The script scans the `Raw Data` directory for result folders. For each folder, it opens the target CSV file and its companion `result.json` file.
2. **Metadata Extraction:** It pulls specific metadata from the JSON (including Sample ID, Cassette Identifier, Lot Code, Protocol details, Date/Time, and Final Result) and stacks this on top of the CSV raw data.
3. **Template Injection:** The script creates an excel spreadsheet and pastes the compiled data into the `Raw Data` sheet, assigning one column per test result.
4. **Batching & Naming:** To prevent template overflow, the script processes results in batches of 40. It dynamically generates output files named with the current date, time, and batch number (e.g., `Compiled Ronia Results - 07 Jul 26 - 15.43 - Part 1.xlsx`).
5. **Clean Up:** Upon successful completion, the script automatically purges the `Raw Data` folder to ensure it is empty and ready for the next run.

## How to Use It
### Prerequisites
* Ensure Python is installed on your system along with the `pandas` and `openpyxl` libraries.


### Execution Steps
1. Place all individual test result folders (each containing a CSV and `result.json`) into the `Raw Data` folder. Make sure no extra files are added as these will cause the script to fail.
2. Run the `ronia.py` script using the command prompt or powershell. If you do not know how to do this see the section below.
3. The script will display a terminal prompt warning you that the `Raw Data` folder will be deleted after processing. Type `Y` and/or press **Enter** to continue.
4. The terminal will display progress as it chunks and exports the data.
5. Once complete, retrieve your newly generated `Compiled Ronia Results` files from the main directory. The `Raw Data` folder will now be empty.

## Troubleshooting

* **Error: "Missing 'result.json' companion file"**
  * **Cause:** The script found a stray file or an incomplete folder inside the `Raw Data` directory. 
  * **Fix:** Open the `Raw Data` folder and remove any files that are not valid result folders. Ensure every folder inside contains a `result.json` file.

Script created by Steve Carter in 2026. 