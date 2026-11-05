# Here we're going tp load a PDF file and extract its text as a python string.
import pymupdf

with pymupdf.open("students.pdf") as pdf:
    for page in pdf:
        print(20*'-') 
        print(page.get_text())