from pathlib import Path
path = Path("file2/archive/10.txt")
print(path.absolute())

root_dir_path = Path(".")

full_root_dir_path = root_dir_path.rglob("*.txt")

for path in full_root_dir_path:
    if path.stem == "14":
        print(path.absolute())
