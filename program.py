

PRACTICAL 1- Simulating Digital Evidence Collection  
Write a Python script to simulate collecting basic digital evidence from system logs and files (e.g., fetching system log files). 




import os
import shutil
import hashlib
import csv
from datetime import datetime

source_folder = "Evidence_Source"
destination_folder = "Collected_Evidence"

os.makedirs(destination_folder, exist_ok=True)

report_file = "evidence_report.csv"


def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)
-
    return sha256.hexdigest()


with open(report_file, "w", newline="") as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow([
        "File Name",
        "File Size",
        "Modified Time",
        "SHA-256 Hash"
    ])

    for file_name in os.listdir(source_folder):

        source_path = os.path.join(source_folder, file_name)

        if os.path.isfile(source_path):

            destination_path = os.path.join(
                destination_folder,
                file_name
            )

            shutil.copy2(source_path, destination_path)

            file_size = os.path.getsize(source_path)

            modified_time = datetime.fromtimestamp(
                os.path.getmtime(source_path)
            )

            file_hash = calculate_hash(source_path)

            writer.writerow([
                file_name,
                file_size,
                modified_time,
                file_hash
            ])

            print("Collected:", file_name)


print("\nDigital evidence collection completed.")
print("Evidence saved in:", destination_folder)
print("Report saved as:", report_file)

TEXT DOCUMENT  
system_log.txt  
2026-08-21 09:00:01 - User login successful  
2026-08-21 09:15:22 - File accessed  
2026-08-21 09:30:45 - USB device connected  
2026-08-21 10:05:12 - User logout  
  
Suspicious_file.txt  
This is a sample file for digital forensic investigation.  

DF_Program_1
│
├── program1.py          
│
├── Evidence_Source
│   ├── system_log.txt
│   └── Suspicious_file.txt
│
└── Collected_Evidence
                
