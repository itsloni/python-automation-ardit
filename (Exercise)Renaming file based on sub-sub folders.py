# I Created a file named 'filez' and it has 2 folders named '2021' and '2022' and each of them have 2 folder named 'November' and 'December'
# Where each of those now have 2 files each. It's those files I'll rename.
from pathlib import Path

filepath = Path("filez")
print(filepath)

full_filepath = filepath.glob("**/*")

for path in full_filepath:
    if path.is_file():
        grandparent_folder_name = path.parts[-3]
        parent_folder_name = path.parts[-2]
        #print(grandparent_folder_name, parent_folder_name)
        new_filename = grandparent_folder_name + "-" + parent_folder_name + "-" + path.stem + path.suffix
        updated_new_filepath = path.rename(new_filename)
        print(updated_new_filepath)
