from pathlib import Path
#NOTE: THE file names and locations that are use here might change and have a prefix like 'New_' there about but everything here worked and is correct


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
        result = file.write("Content 3")
        print(result)
        # So it check ooh! 'num.txt' does not exist then lemme create teh file and then
        #write 'Content 3'

#ALSO you realize that the Path pobject has a lot of attributes that it can be used with for exampl if yiu want to get just the name of the file you just do:
print(p3.name) # here you will get the result 'num.txt' and with this it'll be helpful in manipulation or changing file names.
print(p3.stem) # This prints the file name WITHOUT the extension so like e.g 'num' without the txt.
print(p3.suffix) # This just prints the extension eng. '.txt' from the file name num.txt
# YOU can also use path with folders/directories
p4 = Path("files")
# We can even iterate through it to get the list of iles inside the folder by using a for loop and .iterdir() example below:
for item in p4.iterdir():
    print(item)# We get the list of all the files inside the folder, and they are still not string but Path that can
    # still be used which shows the consistency of pathlib
print(list(p4.iterdir())) # you could even do these so this list the full path of all the items inside the folder/directory

# AND THIS ALL WORKS CAUSE TEH PATH NAME STORED IN P2 OR P3 IS NOT A STRING LIKE THE ONE IN P1 EXAMPLE CAUSE PATH DOESN'T STORE IT AS STRING BUT AS OBJECT PATH.
# ALSO, YOU REALISE OS DOES SIMILAR BUT OS TREAT THE FILE PATH AS A STRING AND HENCE CAN'T BE AS EASY AS PATH tho it POSSIBLE WITH OS JUST HARDER.

