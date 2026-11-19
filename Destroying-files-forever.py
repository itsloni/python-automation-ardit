# Suppose you want to delete a file cause your selling your laptop and all in this method we start be replacing the content
# of the file and then deleting it as shown below.
from pathlib import Path

location_dir_to_delete = Path("deletion-folder") # THe path to the dir containing the files to delete

for path in location_dir_to_delete.glob("*.txt"):
    with open(path, "wb") as file: # the 'wb' mean write in binary so like u change the content to a binary
        file.write(b"")
    path.unlink() # This is to delete the file after it's been changed


