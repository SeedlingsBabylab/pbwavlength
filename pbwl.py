import csv
import sys
import os

start_dir = ""

file_info = []

def walk_tree(path):
    for root, dirs, files in os.walk(path):
        if "PictureBook" in root:
            last_dir = os.path.split(root)[1]
            if "PictureBook" not in last_dir:
                for file in files:


if __name__ == "__main__":
    start_dir = sys.argv[1]


    walk_tree(start_dir)
