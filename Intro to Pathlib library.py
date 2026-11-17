from pathlib import Path
# so pathlib typically uses a path object type to represent the file path.
# For example normally if we'd used import os then if we wanted to import filein file abc.txt it'll be:
p1 = "files/abc.txt"
with open (p1, "r") as file:
    print(file.read()) # and this prints the content/text inside the abc.txt file which is content 1

# But with file path you simply use the Path class and then instantiate it as below:
p2 = Path("files/abc.txt")
print(p2) # This print the literal path which is 'files/abc.txt'. and NOTE: it is not a string but the actual PATH.
#  so the usefulness is now like imagine we want to say if path exist we can just say:
if p2.exists():
    with open(p2, "r") as file:
        print(file.read())

# We can also use the path when teh path doesn't exist yet. for example:
p3 = Path("files/num.txt") # at this moment there is no file named 'num.txt'

if not p3.exists():
    with open (p3, "w") as file:
        file.write("Content 3")
        # So it check ooh! 'num.txt' does not exist then lemme create teh file and then
        #write 'Content 3'


