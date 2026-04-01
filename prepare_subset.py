import os
import shutil
import pandas as pd

# paths
CSV_PATH = "data/UrbanSound8K/metadata/UrbanSound8K.csv"
AUDIO_PATH = "data/UrbanSound8K/audio"
OUTPUT_PATH = "data/UrbanSoundSubset"

# classes to keep
TARGET_CLASSES = ["dog_bark", "drilling", "siren", "street_music"]

# max files per class
MAX_FILES = 100

# load metadata
df = pd.read_csv(CSV_PATH)

# filter only needed classes
df = df[df["class"].isin(TARGET_CLASSES)]

# create output folders
for cls in TARGET_CLASSES:
    os.makedirs(os.path.join(OUTPUT_PATH, cls), exist_ok=True)

# counter per class
class_counts = {cls: 0 for cls in TARGET_CLASSES}

# copy files
for _, row in df.iterrows():
    label = row["class"]

    if class_counts[label] >= MAX_FILES:
        continue

    file_name = row["slice_file_name"]
    fold = f"fold{row['fold']}"

    src = os.path.join(AUDIO_PATH, fold, file_name)
    dst = os.path.join(OUTPUT_PATH, label, file_name)

    shutil.copy(src, dst)
    class_counts[label] += 1

print("Done!")
print(class_counts)