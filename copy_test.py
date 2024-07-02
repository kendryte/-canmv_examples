import glob
import os
import sys
import shutil


copy_map = {
    "ai_cube_examples": "16-AI-Cube",
    "ai_demo": "04-AI-Demo",
    "April-tags": "07-April-Tags",
    "cipher": "03-Cipher",
    "Codes": "08-Codes",
    "Color-Tracking": "09-Color-Tracking",
    "demo": "04-AI-Demo",
    "Drawing": "10-Drawing",
    "Feature-Detection": "11-Feature-Detection",
    "Image-Filters": "12-Image-Filters",
    "lvgl": "15-LVGL",
    "machine": "02-Machine",
    "media": "01-Media",
    "Micropython-Basics": "00-Micropython-Basics",
    "nncase_runtime": "05-nncase-Runtime",
    "Snapshot": "13-Snapshot",
    "socket": "14-Socket",
}

if __name__ == '__main__':
    for key in copy_map:
        scripts = glob.glob(f"{sys.argv[1]}/{key}/*.py", recursive=True)
        target = f"examples/{copy_map[key]}/"
        if os.path.exists(target):
            shutil.rmtree(target)
        os.mkdir(target)
        for script in scripts:
            shutil.copy2(script, target)
