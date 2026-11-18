from pathlib import Path

root_folder = Path("file-ext")
full_path = root_folder.glob("*.txt") # You cn use rglob("*.txt") but is used when there is a lot f sub folders..basically means recursive and it's the equivalent of glob("**/*.txt")
for path in full_path:
    if path.is_file():
        new_extension = path.stem + ".csv"
        full_new_extension = path.with_name(new_extension)
        # The  lines above can be written in a single line like: 'full_new_extension = path.with.suffix(".txt")' # Easier so long the path.stem name does not need to be changed.
        renamed_full_new_extension = path.rename(full_new_extension)
        print(renamed_full_new_extension)


