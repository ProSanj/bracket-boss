import subprocess
import os
import time

print("=" * 50)
print("UPDATING FIFA PREDICTOR")
print("=" * 50)
print()

start = time.time()

# -------------------------
# DOWNLOAD DATASET
# -------------------------

print("Downloading latest dataset...")

subprocess.run(
    [
        "python",
        "-m",
        "kaggle",
        "datasets",
        "download",
        "-d",
        "aissaouihamda/international-football-matches-1872-present",
        "-p",
        "data",
        "--force"
    ],
    check=True
)

# -------------------------
# UNZIP DATASET
# -------------------------

print("Extracting dataset...")

subprocess.run(
    [
        "python",
        "-m",
        "kaggle",
        "datasets",
        "download",
        "-d",
        "aissaouihamda/international-football-matches-1872-present",
        "-p",
        "data",
        "--unzip",
        "--force"
    ],
    check=True
)

# -------------------------
# REBUILD DATASET
# -------------------------

print("Building ML dataset...")

subprocess.run(
    ["python", "src/build_dataset.py"],
    check=True
)

# -------------------------
# RETRAIN MODEL
# -------------------------

print("Training model...")

subprocess.run(
    ["python", "src/save_model.py"],
    check=True
)

end = time.time()

print()
print("=" * 50)
print("UPDATE COMPLETE")
print("=" * 50)

print(
    "Runtime:",
    round(end - start, 2),
    "seconds"
)