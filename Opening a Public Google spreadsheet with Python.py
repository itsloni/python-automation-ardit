
#We're going to get the data and print them out using pandas
import pandas

url_sheet1 = "https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/gviz/tq?tqx=out:csv&sheet=2013"
# So normally if you copy the link of a public google sheet it has an ending after a / that starts with 'edit?usp=sharing' but to
# make it work in python you must remove that and replace it with to 'gviz/tq?tqx=out:csv&sheet={input the name of the
# sheet file (usually located at the bottom of the google-sheet)and remove the curly bracket}'.
url_sheet2 = "https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/gviz/tq?tqx=out:csv&sheet=2014"
data = pandas.read_csv(url_sheet2) # the csv() normally expects a file that's locally here, but you can also give it a link
print(data)

#NOTE : USING just pandas alone you CANNOT write, change or EDIT a spreadsheet in python, you will have to use the google sheet API'