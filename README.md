# NanoFast Results Compiler

## What the Script is For
The NanoFast Results Compiler is a Python automation tool designed to streamline the processing and presentation of Nanofast test results. It automatically compiles individual results within a reader or saved locally into a structured, easily readable master Excel template for downstream analysis.

## How it Works
1. **Data Scraping:** The script scans data within the `Raw Data` directory or from the Reader device, for result folders. For each folder, it opens the target CSV file and its companion `result.json` file.
2. **Metadata Extraction:** It pulls specific metadata from the JSON (including Sample ID, Cassette Identifier, Lot Code, Protocol details, Date/Time, and Final Result) and stacks this on top of the CSV raw data.
3. **Template Injection:** The script creates an excel spreadsheet and pastes the compiled data into the `Raw Data` sheet, assigning one column per test result.
4. **Batching & Naming:** To prevent template overflow, the script processes results in batches of 40. It dynamically generates output files named with the current date, time, and batch number (e.g., `Compiled NanoFast Results - 07 Jul 26 - 15.43 - Part 1.xlsx`).
5. **Clean Up:** Upon successful completion, the script is ran locally then copied data is automatically purges the `Raw Data` folder to ensure it is empty and ready for the next run.

## How to Install
### Prerequisites
* Install Python *directly from the Microsoft Store*. The script has been tested with `Python 3.13`.
* Download the latest release from the GitHub repo, using the releases section of the sidebar.
* Under the assets section of the releases page, download the .zip file.
### Installation
* Extract the .zip directly into your C: Drive. Installations elsewhere are not recommended and may result in file path errors.

## How to Use
### Execution Steps
1. If processing data from a device, connect the Nanofast reader to the PC using a USB-C cable, power on the reader, and place the device into 'Mass Storage Mode' using the Menu on the reader. If using local data, copy all individual test result folders (each containing a CSV and `result.json`) into the `Raw Data` folder.
2. Run the `Solus NanoFast Compliler.bat` file by double clicking.
3. Select the appropriate location for data processing.
    * Press 1 for Automatic. This automatically sources the results from the device.
    * Press 2 for Manual. For this option manually copy the results into the folder named `Raw Data`.  
4. Select the date range for data processing, using the up and down arrows and selecting with Enter.
3. The script will display a terminal prompt warning you that the `Raw Data` folder will be deleted after processing. Type `Y` and/or press **Enter** to continue. Data stored on a Reader cannot be deleted, this only matters if you have manually transferred files.
4. The terminal will display progress as it chunks and exports the data.
5. Once complete, retrieve your newly generated `Compiled NanoFast Results` files from the main directory. The `Raw Data` folder will now be empty.

## Known Issues
1. Upon first launch, the script successfully installs pandas but fails to initialise in the same session. As a temporary workaround, restarting the script will resolve the issue. This is a known issue scheduled for resolution in an upcoming patch

---
Script created by Steve Carter in 2026. 
