from zipfile import ZipFile
import os
import gzip
import shutil

# Paths
activities_path = "output\\activities\\"
activities_unzipped_path = "output\\activitiesUnzipped\\"

# Creating output directory's
if not os.path.exists("output\\"):
    os.makedirs("output\\")

if not os.path.exists(activities_unzipped_path):
    os.makedirs(activities_unzipped_path)

# Unzipping activities.zip
with ZipFile("activities.zip", 'r') as zObject:
    zObject.extractall(
    path="output\\")

# Unzipping .gz files into activitiesUnzipped directory
for file in os.listdir(activities_path):
    with gzip.open(activities_path + file, 'rb') as f_in:
        with open(activities_unzipped_path + file.replace(".gz", ""), 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

print("Unzip Completed")