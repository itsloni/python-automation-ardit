from pathlib import Path

root_folder = Path("file-ext")
full_path = root_folder.glob("*.txt")
for path in full_path:
    new_extension = path.stem + ".csv"
    full_new_extension = path.with_name(new_extension)
    renamed_full_new_extension = path.rename(full_new_extension)
    print(renamed_full_new_extension)


