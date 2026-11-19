from pathlib import Path
import zipfile

root_dir = Path(".") # This is created to get the path to the main file which is 'Extracting Files from a Zipfile.py' so
# that the extracted files from the zipfiles will land in this path.
destination_dir = Path("files") #This is the path to the directory housing the zipfiles we want to extract.
