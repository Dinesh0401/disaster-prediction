import os
import random
import shutil

from tqdm import tqdm

# === SETTINGS ===
SOURCE_DIR = "Dataset_Raw"
DEST_DIR = "Dataset"

TRAIN_RATIO = 0.6
VAL_RATIO = 0.2
TEST_RATIO = 0.2

assert abs((TRAIN_RATIO + VAL_RATIO + TEST_RATIO) - 1.0) < 1e-6, (
    "Ratios must sum to 1.0"
)


# === Helper: create directory if not exists ===
def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


# === Create base folders ===
for split in ["train", "validation", "test"]:
    make_dir(os.path.join(DEST_DIR, split))


# === Walk through each subfolder ===
for root, dirs, files in os.walk(SOURCE_DIR):
    # Skip base dir
    if root == SOURCE_DIR:
        continue

    # Get relative path (like "fire_disaster/urban_fire")
    rel_path = os.path.relpath(root, SOURCE_DIR)
    if not files:
        continue  # skip if empty

    # Get list of image files
    images = [f for f in files if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    if not images:
        continue

    # Shuffle
    random.shuffle(images)

    # Split indices
    total = len(images)
    train_end = int(TRAIN_RATIO * total)
    val_end = int((TRAIN_RATIO + VAL_RATIO) * total)

    train_files = images[:train_end]
    val_files = images[train_end:val_end]
    test_files = images[val_end:]

    # Define destination folders
    class_name = rel_path.replace(os.sep, "_")

    for split, split_files in [
        ("train", train_files),
        ("validation", val_files),
        ("test", test_files),
    ]:
        split_folder = os.path.join(DEST_DIR, split, class_name)
        make_dir(split_folder)

        # Copy files
        for f in tqdm(split_files, desc=f"{class_name} -> {split}", leave=False):
            src = os.path.join(root, f)
            dst = os.path.join(split_folder, f)
            shutil.copy2(src, dst)

print("\n✅ Dataset successfully split into train/validation/test sets at:", DEST_DIR)
