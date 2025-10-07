import os

from PIL import Image

base_dir = "Dataset"


def is_image_valid(file_path):
    try:
        with Image.open(file_path) as img:
            img.verify()
        return True
    except Exception:
        return False


removed = 0
for root, _, files in os.walk(base_dir):
    for f in files:
        if f.lower().endswith((".jpg", ".jpeg", ".png")):
            path = os.path.join(root, f)
            if not is_image_valid(path):
                print(f"❌ Corrupted: {path}")
                os.remove(path)
                removed += 1

print(f"\n✅ Removed {removed} unreadable image(s).")
