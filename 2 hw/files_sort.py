import os
import sys

def files_sort(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    files.sort()
    for file in files:
        print(file)

if __name__ == "__main__":
    directory = sys.argv[1]
    files_sort(directory)