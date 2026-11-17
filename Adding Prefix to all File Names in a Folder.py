from pathlib import Path

#To even manipulate like files and all you must first find their root directory like where exactly their location is

root_dir = Path("files")
file_paths = root_dir.iterdir()

for path in file_paths:
    new_filename = "new_" + path.stem + path.suffix # At this place the file name has not yet been changed from the path yet but printing new_filename
    # shows the change but it's not yet effected on the actual file yet.
    new_filepath = path.with_name(new_filename)
    #print(path.rename(new_filepath)) # This used when new_filepath = Path(new_filename) will forgo the fact that the files are inside a folder  and create then as they were in th
    # same directory as teh folder not inside the folder. That why to correctly catch that folder we do new_filepath = path.with_name(new_filename) cause this picks up the
    # file name with eth path which is teh folder
    print(new_filepath)
    path.rename(new_filepath) # it is now you now do this to actually rename the file in the disk


