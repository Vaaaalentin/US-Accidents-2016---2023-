import os
import shutil
import kagglehub

cache_path = kagglehub.dataset_download("sobhanmoosavi/us-accidents")

os.makedirs("data", exist_ok=True)

source_file = os.path.join(cache_path, "US_Accidents_March23.csv")
dest_file = os.path.join("data", "US_Accidents_2016_2023.csv")

shutil.copy2(source_file, dest_file)