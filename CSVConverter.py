import os
import subprocess
import shutil

# Paths
activities_unzipped_path = "output\\activitiesUnzipped\\"
activities_csv_path = "output\\activitiesCSV\\"
fit_tool_path = "FitSDKRelease_21.158.00\\java\\FitCSVTool.jar"

# Creating output directory's
if not os.path.exists(activities_csv_path):
    os.makedirs(activities_csv_path)

# Converting files to CSV
for file in os.listdir(activities_unzipped_path):
    if file.endswith(".fit"):

        print(f"Converting {file} to CSV")
        subprocess.call(['java', '-jar', fit_tool_path, activities_unzipped_path + file])

        csv_file = file.replace(".fit", ".csv")
        if os.path.exists(activities_unzipped_path + csv_file):
            shutil.move(activities_unzipped_path + csv_file, activities_csv_path + csv_file)
            print(f"{file} converted to {csv_file}")
        else:
            print("Error")

print("Conversion Completed")