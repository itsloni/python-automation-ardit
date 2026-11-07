# Here we're going tp load a PDF file and extract its text as a python string.
import pymupdf

with pymupdf.open("students.pdf") as pdf:
    for page in pdf:
        print(20*'-') # This is to show the number of pages in the pdf by using the '-' as an identifier/marker
        # because you're print ing the '-' for each page.
        print(page.get_text()) # The .get_text() is a pymupdf method that is used to extract the text from that specified pdf

    page1 = pdf[0].get_text() # If you decide to print just the first page of the pdf. or one particular page
    print(20 * "&")
    print(page1)

    txt = "________"
    for page in pdf:
        txt = txt + page.get_text() # If you want to make each page print after each  other
    print(txt)
