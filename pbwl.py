import csv
import sys
import os

from ffprobe import FFProbe

start_dir = ""
csv_path = ""

output_table = []

def walk_tree(path):
    for root, dirs, files in os.walk(path):
        if "PictureBook" in root:
            last_dir = os.path.split(root)[1]
            if "PictureBook" not in last_dir:
                for file in files:
                    if check_file_extension(file):
                        split_path = splitall(os.path.join(root, file))
                        pathname = os.path.join(root, file)
                        split_path = splitall(pathname)

                        metadata = FFProbe(pathname)
                        try:
                            length = metadata.streams[0].durationSeconds()
                        except (IndexError):
                            print os.path.join(root, file) + " was a problem file. skipped."
                            continue
                        path_key = os.path.join(split_path[-3], split_path[-2], split_path[-1])
                        output_table.append((path_key, length))

def output_csv():

    with open(csv_path, "wb") as file:
        writer = csv.writer(file)
        writer.writerow(["file", "seconds"])
        writer.writerows(output_table)

def check_file_extension(path):
    upper = path.upper()
    if upper.endswith(".WAV"):
        return True
    return False

def splitall(path):
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path: # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts

if __name__ == "__main__":
    start_dir = sys.argv[1]
    csv_path = sys.argv[2]

    walk_tree(start_dir)

    output_csv()
