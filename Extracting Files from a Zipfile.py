from pathlib import Path
import zipfile

root_dir = Path(".") # This is created to get the path to the main file which is 'Extracting Files from a Zipfile.py'
# because the zip files are in this path.
destination_dir = Path("file2") #This is the path to the directory where the extracted zipfile will enter.

for path in root_dir.glob("*.zip"):
    with zipfile.ZipFile(path, "r") as zip_ref:
        final_path = destination_dir / Path(path.stem)
        zip_ref.extractall(path=final_path)
