# -*- coding: utf-8 -*-
""" """

import sys
import subprocess


def install_dependencies():
    packages = ["pandas", "openpyxl"]
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f"📦 {package} not found. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✅ {package} installed successfully.")


install_dependencies()

import os  # noqa: E402
import shutil  # noqa: E402
import json  # noqa: E402
import glob  # noqa: E402

# import urllib.request  # noqa: E402 Not currently used, but retained for potential future use in GitHub update feature.
import msvcrt  # noqa: E402
from datetime import datetime  # noqa: E402
import pandas as pd  # noqa: E402


# Removal of the GitHub update feature due to potential issues with script integrity. The function is retained for reference but is not called in the main execution flow.
# Users are encouraged to manually check for updates on the GitHub repository.
# def github_update():
#     """Checks GitHub for script updates."""
#     # Tell the script where to the dev.py file in the same folder.
#     script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     dev_file_path = os.path.join(script_dir, ".dev")

#     if os.path.exists(dev_file_path):
#         return

#     github_raw_url = "https://raw.githubusercontent.com/Majora2186/NanoFast-Results-Compiler/refs/heads/main/__lib__/NanoFast.py"

#     try:
#         with urllib.request.urlopen(github_raw_url) as response:
#             latest_code = response.read().decode("utf-8")

#         with open(__file__, "r", encoding="utf-8") as current_file:
#             current_code = current_file.read()

#         if latest_code != current_code:
#             with open(__file__, "w", encoding="utf-8") as current_file:
#                 current_file.write(latest_code)

#     except Exception:
#         pass


def setup_environment():
    """Sets up the necessary folders and files."""
    # 1. This is where the script itself lives (the basement)
    lib_dir = os.path.dirname(os.path.abspath(__file__))

    # 2. This is the root folder (the ground floor)
    root_dir = os.path.dirname(lib_dir)

    # 3. Path variables
    raw_data = os.path.join(root_dir, "Raw Data")
    template_path = os.path.join(lib_dir, "template.xlsx")
    compiled_dir = os.path.join(root_dir, "Compiled Results")

    for directory in [raw_data, compiled_dir]:
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

    return raw_data, template_path, compiled_dir
    # folder_x is not returned as it is only used inside this variable to define the other variables. It is not needed outside of this function.


def find_drive_by_name(target_name):
    """Searches connected drives for a specific volume name."""
    # This function uses the Windows Management Instrumentation Command-line (WMIC) to get a list of logical drives
    # and their volume names. It then checks if the target name is present in any of the volume names and returns the corresponding drive letter if found.
    print(f"\nSearching for drive named '{target_name}'...")
    try:
        # Asks Windows for a list of drive letters and their names
        output = subprocess.check_output(
            ["wmic", "logicaldisk", "get", "caption,volumename"], text=True
        )
        for line in output.splitlines():
            if target_name.lower() in line.lower():
                # Splits the line and grabs the first part (e.g., "E:")
                drive_letter = line.split()[0]
                print(f"Drive found at {drive_letter}")
                return drive_letter
    except Exception as e:
        print(f"Error searching for drives: {e}")

    print("Drive not found.")
    return None


def get_mode_selection():
    """Prompts the user for Auto/Manual mode via single keypress."""
    print("Select retrieval mode:")
    print("[1] Automatic (Retrieve from Instrument Drive)")
    print("[2] Manual (Files already loaded in Raw Data)")

    while True:
        # getch() pauses the script until a key is pressed
        key = msvcrt.getch()
        try:
            char = key.decode("utf-8")
            if char in ["1", "2"]:
                return char
        except UnicodeDecodeError:
            pass  # Ignore special keys like arrows for now


def auto_copy_data(drive_letter, raw_data):
    """Copies all contents from the target drive to Raw Data."""
    print("Copying files to Raw Data...")
    # shutil.copytree requires the destination to not exist, or dirs_exist_ok=True
    shutil.copytree(drive_letter, raw_data, dirs_exist_ok=True)
    print("Copy complete.")


def cleanup(raw_data):
    """Cleans up the Raw Data folder by removing unnecessary files."""
    # 1. Delete the LICENSES folder
    licenses_path = os.path.join(raw_data, "LICENSES")
    if os.path.isdir(licenses_path):
        shutil.rmtree(licenses_path)

    # 2. Delete the summary CSV
    summary_path = os.path.join(raw_data, "results_summary.csv")
    if os.path.isfile(summary_path):
        os.remove(summary_path)

    # 3. Delete any zip files starting with "logs-"
    zip_pattern = os.path.join(raw_data, "logs-*.zip")
    for zip_file in glob.glob(zip_pattern):
        os.remove(zip_file)


def process_files(raw_data):
    """Processes the CSV files in the Raw Data folder."""
    # Checking if excel files are present and list them.
    excel_files = []

    for root, dirs, files in os.walk(raw_data):
        for file in files:
            if file.endswith(".csv"):
                excel_files.append(os.path.join(root, file))

    if not excel_files:
        print("No Excel files found in Raw Data.")
        print("")
        print("Stopping Script.")
        print("-" * 30)
        sys.exit(0)

    # My for loop for iterating through all spreadsheets.
    combined_df = pd.DataFrame()
    # This is the line that creates dots for each file worked on.
    for file_path in excel_files:
        print("*", end="", flush=True)

        # This is where the data is extracted.
        csv_df = pd.read_csv(file_path, usecols=[2])
        csv_df.columns = [0]
        # Find the json file in the folder
        json_path = os.path.join(os.path.dirname(file_path), "result.json")
        # Error if extra files found
        if not os.path.exists(json_path):
            print("")
            print("")
            print(f"Stray file found in: {os.path.dirname(file_path)}")
            print("")
            print("Please clear 'Raw Data' of invalid files and try again.")
            print("Safely exiting script.")
            print("-" * 30)
            sys.exit(1)
        # Open file and give python the ability to read it.
        with open(json_path, "r") as json_file:
            # Reads the raw text from the file and translates it into a Python "dictionary". Save into the variable json_data.
            json_data = json.load(json_file)
            # Extract standard data points
            sample_id = json_data.get("sampleId", "")
            cassette_code = json_data.get("cassetteIdentifierCode", "")
            lot_code = json_data.get("lotCode", "")

            # Extract nested data points safely (handles null values)
            protocol_name = (json_data.get("protocol") or {}).get("name", "")
            protocol_version = (json_data.get("protocol") or {}).get("version", "")
            result_val = (json_data.get("result") or {}).get("value", "")

            # Extract raw endTime for future splitting
            raw_end_time = json_data.get("endTime", "")
            end_date = raw_end_time.split("T")[0] if "T" in raw_end_time else ""
            end_time = raw_end_time.split("T")[1][:5] if "T" in raw_end_time else ""

            enhanced_json_path = os.path.join(
                os.path.dirname(file_path), "enhanced-result.json"
            )
            if os.path.exists(enhanced_json_path):
                with open(enhanced_json_path, "r") as enhanced_file:
                    enhanced_data = json.load(enhanced_file)
                    instrument_info = enhanced_data.get("InstrumentInformation", [{}])
                    factory_data = instrument_info[0].get("factoryDataName", "")
            else:
                factory_data = ""

            # Add these scraped data points to the spreadsheet at the top
            # This is the line that decides the order the json scrape is added to the spreadsheet
            json_list = [
                end_time,
                end_date,
                cassette_code,
                sample_id,
                result_val,
                protocol_name,
                protocol_version,
                lot_code,
            ]
            # This adds on the NanoFast Instrument number from the second json file.
            json_list.append(factory_data)
            # This converts my python list into a dataframe
            json_df = pd.DataFrame(json_list)
            # This adds the dataframes together
            single_result_column = pd.concat([json_df, csv_df], ignore_index=True)
            combined_df = pd.concat([combined_df, single_result_column], axis=1)

    return combined_df, len(excel_files)


def export_results(combined_df, template_path, compiled_dir, raw_data):
    """Exports the compiled dataframe into chunked Excel templates and resets Raw Data."""
    # 1. Get current time and total number of results
    current_time = datetime.now().strftime("%d %b %y - %H.%M")
    total_results = combined_df.shape[1]
    total_parts = len(range(0, total_results, 40))

    # 2. Loop through the results in chunks of 40
    for i in range(0, total_results, 40):
        part_num = (i // 40) + 1
        print(f"Exporting to Excel {part_num}/{total_parts}.")
        chunk_df = combined_df.iloc[:, i : i + 40]

        # 3. Create dynamic filename and path
        batch_filename = (
            f"Compiled NanoFast Results - {current_time} - Part {part_num}.xlsx"
        )
        batch_output_path = os.path.join(compiled_dir, batch_filename)

        # 4. Copy template and paste the chunk
        shutil.copy(template_path, batch_output_path)
        with pd.ExcelWriter(
            batch_output_path, engine="openpyxl", mode="a", if_sheet_exists="overlay"
        ) as writer:
            chunk_df.to_excel(
                writer,
                sheet_name="Raw Data",
                startcol=2,
                startrow=0,
                index=False,
                header=False,
            )
    print("")
    print("Process complete.")
    print("Script closing.")
    print("")
    # print("Created by Steve Carter.")
    print("-" * 30)
    print("")

    # Delete and replace Compiled NanoFast Results
    shutil.rmtree(raw_data)
    os.makedirs(raw_data, exist_ok=True)


def get_available_months(raw_data):
    """Scans JSON files in Raw Data and groups directories by month."""
    print("")
    print("Scanning copied files for dates...")
    month_data = {}

    for root, dirs, files in os.walk(raw_data):
        if "result.json" in files:
            json_path = os.path.join(root, "result.json")
            try:
                with open(json_path, "r") as f:
                    data = json.load(f)
                    raw_time = data.get("endTime", "")
                    if raw_time:
                        # Parse "YYYY-MM-DD" into a date object, format as "Month YYYY"
                        date_obj = datetime.strptime(raw_time.split("T")[0], "%Y-%m-%d")
                        month_key = date_obj.strftime("%B %Y")

                        if month_key not in month_data:
                            month_data[month_key] = []
                        # Store the directory path to easily delete it later
                        month_data[month_key].append(root)
            except Exception:
                pass

    return month_data


def select_month_interactive(month_data):
    """Displays an interactive menu to select a month using arrow keys."""
    if not month_data:
        return None

    months = list(month_data.keys())
    total_files = sum(len(folders) for folders in month_data.values())
    options = months + ["All"]
    if len(months) == 1:
        print(f"Only found data for {months[0]}. Auto-selecting.")
        return months[0]

    current_index = 0

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("")
        print("-" * 30)
        print("Solus NanoFast Compiler")
        print("-" * 30)
        print("")
        # Optional: keeps the header visible
        print("Select a month to process (Use UP/DOWN arrows, then ENTER):")
        print("-" * 30)

        for i, option in enumerate(options):
            if option == "All":
                print("")  # Adds the requested space
                count = total_files
            else:
                count = len(month_data[option])

            if i == current_index:
                print(f" > {option}: {count} result(s)")
            else:
                print(f"   {option}: {count} result(s)")

        key = msvcrt.getch()

        # Arrow keys send a double byte: \x00 or \xe0, followed by the key code
        if key in (b"\x00", b"\xe0"):
            special_key = msvcrt.getch()
            if special_key == b"H":  # Up arrow
                current_index = (current_index - 1) % len(options)
            elif special_key == b"P":  # Down arrow
                current_index = (current_index + 1) % len(options)
        elif key == b"\r":  # Enter key
            return options[current_index]


def purge_unselected_months(month_data, selected_month):
    """Deletes all folders in Raw Data that do not belong to the selected month."""
    print(f"Purging files outside of {selected_month}...")
    print("")
    for month, folders in month_data.items():
        if month != selected_month:
            for folder in folders:
                if os.path.exists(folder):
                    shutil.rmtree(folder)


####################################################################################################################################################################
####################################################################################################################################################################
####################################################################################################################################################################


def main():

    # This checks if the sysem is windows or linux and clears the script.
    os.system("cls" if os.name == "nt" else "clear")

    # Updates the script from GitHub if ENABLE_UPDATES is set to True.
    # github_update()

    # This sets up the environment and creates necessary folders if they don't exist.
    raw_data, template_path, compiled_dir = setup_environment()
    # Start user interaction and processing
    print("")
    print("-" * 30)
    print("Solus NanoFast Compiler")
    print("-" * 30)
    print("")

    mode = get_mode_selection()

    if mode == "1":
        target_drive_name = "RESULTS"
        drive_letter = find_drive_by_name(target_drive_name)

        if drive_letter:
            auto_copy_data(drive_letter + "\\", raw_data)

        else:
            print("Cannot proceed automatically. Please load files manually.")
            mode = "2"  # Switch to manual mode if drive not found.
    else:
        print("\nManual mode selected. Ensure files are in Raw Data.")

    if mode == "2":
        print(
            "\nWARNING: All files in Raw Data will be permanently DELETED after processing."
        )
        # We can keep a simple standard input here just to confirm they are ready to nuke the folder
        ready = input("Continue? [Y]/N: ").strip().lower()
        if ready in ["n", "no"]:
            sys.exit(0)

    month_data = get_available_months(raw_data)
    if month_data:
        selected_month = select_month_interactive(month_data)
        if selected_month and selected_month != "All":
            purge_unselected_months(month_data, selected_month)
    else:
        print("Could not find any valid dates in the copied files.")

    print("")
    print("Processing...")
    print("")

    cleanup(raw_data)
    combined_df, total_files = process_files(raw_data)
    print("")
    print(f"\nTotal spreadsheets processed: {total_files}")
    print("")
    print("-" * 30)
    export_results(combined_df, template_path, compiled_dir, raw_data)


if __name__ == "__main__":
    main()
