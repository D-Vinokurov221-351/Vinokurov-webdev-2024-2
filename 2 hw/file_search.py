import os
import sys

def file_search(file_name):
    for root, _, files in os.walk("."):
        if file_name in files:
            with open(os.path.join(root, file_name)) as file:
                for _ in range(5):
                    print(file.readline(),end='')
            return
    print(f"Файл {file_name} не найден")

if __name__ == "__main__":
    file_name = sys.argv[1]
    file_search(file_name)