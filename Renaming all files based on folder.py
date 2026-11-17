from pathlib import Path
# print(Path.cwd()) Just to check my cwd
root_dir = Path("New-megafiles")
file_paths = root_dir.glob("**/*")

for path in file_paths:
    # print(path)
    if path.is_file():
        parent_folder = path.parts[-2]
        new_filename = parent_folder + "_" + path.name # This is a string object
        # print(new_filename)
        new_filepath = path.with_name(new_filename) # This is a path object the '.with_name()' ensures it's still within the subfolders
        path.rename(new_filepath)


