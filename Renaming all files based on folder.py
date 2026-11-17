from pathlib import Path
# print(Path.cwd()) Just to check my cwd
root_dir = Path("New-megafiles")
file_paths = root_dir.glob("**/*")
print(file_paths)
for path in file_paths:
    print(path)
    if path.is_file():
        parent_folder = path.parts[-2]
        new_filename = parent_folder + "_" + path.name
        # print(new_filename)
        # result = path.with_name(new_filename)
        # path.rename(result)

