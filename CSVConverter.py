import os
import subprocess
import shutil

# Paths
activities_unzipped_path = "output\\activitiesUnzipped\\"
fit_tool_path = "FitSDKRelease_21.158.00\\java\\FitToCSV-record.bat"

# Converting files to CSV
for file in os.listdir(activities_unzipped_path):
    if file.endswith(".fit"):

        print(f"Converting {file} to CSV")

        process = subprocess.Popen(
            [fit_tool_path, os.path.join(activities_unzipped_path, file)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        process.stdin.write('\n')
        process.stdin.flush()
        process.wait()


print("Conversion Completed")
