from pathlib import Path
from datetime import datetime

file_path = Path("practice file")
full_filepath = file_path.glob("**/*")

for path in full_filepath:
    if path.is_file():
        stats = path.stat()
        seconds_created = stats.st_ctime
        date_created = datetime.fromtimestamp(seconds_created) # The '.fromtimestamp()' is a methode from datetime to get the time stamp in a human-readable format
        date_created_str = date_created.strftime("%Y-%m-%d %H:%M:%S")# The '.strfrime()' is a method to converts the time to a string to be usable in the script
        new_filepath = date_created_str + "-" + path.name
        full_new_filepath = path.with_name(new_filepath)
        # print(full_new_filepath)
        renamed_full_new_filepath = path.rename(full_new_filepath)
        print(renamed_full_new_filepath)


# print(stats)
# print(second_created)
# print(date_created_str) # Note: that this output is not a string and inorder to use it in your script, you have to make it a string first.
