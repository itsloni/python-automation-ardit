# Here we're going tp load a PDF file and extract its text as a python string.
import pymupdf

with pymupdf.open("students.pdf") as pdf:
    for page in pdf:
        print(20*'-') # This is to show the number of pages in the pdf by using the '-' as an identifier/marker
        # because you're print ing the '-' for each page.
        print(page.get_text())