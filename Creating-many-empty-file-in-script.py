from pathlib import Path
#To create empty file
root_dir = Path("file2")

for i in range(10, 21):
    filename = str(i) + ".txt"
    filepath = root_dir / Path(filename)
    filepath.touch()

# TO PUT FILES IN AN ARCHIVE/ZIP FILE: BELOW SHOWS THAT USING THE EMPTY FILE CREATED BY THE CODE ABOVE.
import zipfile
# We create the Path object for the folder containing the  files we want to zip which is already done in line 3
#Then we create another Path object that is used to for the ath to where the zipfile will be. Which i just did below
archive_path = root_dir / Path("archive.zip")

with zipfile.ZipFile(archive_path, "w") as zip_ref:
    for path in root_dir.glob("*.txt"):
        zip_ref.write(path)
        path.unlink() # This is used to delete files as they are being archived

