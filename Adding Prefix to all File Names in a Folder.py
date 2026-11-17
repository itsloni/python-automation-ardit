from pathlib import Path

#To even manipulate like files and all you must first find their root directory like where exactly their location is

root_dir = Path("files")
file_paths = root_dir.iterdir()

for path in file_paths:
    new_filename = "new_" + path.stem + path.suffix # At this place the file name has not yet been changed from the path yet but printing new_filename
    # shows the change but its not yet effected on teh actual file yet.

