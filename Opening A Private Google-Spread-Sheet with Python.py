# So here we have to configure the API cause we have to tell google that we are the owner of the
# private google spread sheet. Hence the url for the spreadsheet is not enough
#So essentially google will have to give you an api key which you will then use to access the sheet to change,
# delete data, update, edit etc.

# To do this we need the 'gspread' library and then you get an api key from google.
#To get google api what you do is search for google api console, set up your google-drive API(already did that you only set it up once) AND THEN YOU ENABLE GOOGLE SPREADSHEET API.
import gspread

gc = gspread.service_account("secrets.json") # This line establishes a connection to that google sheet, and that '.service_account()' method accepts the "secrets.json" path so it sees ths info

spreadsheet = gc.open("Automating google-sheet with python") # This is to open the actual google spreadsheet that can have multiple worksheet Tabs

#So now you know that there can be multiple worksheets in a spreadsheet like the '2013' and the '2014' worksheet created at the bottom of the page. remember they are tabs those worksheets and you can create many tabs/worksheet in a single google spreadsheet.
# So one way to call the worksheet you want from that "Automating google-sheet with python" spreadsheet  is by INDEX as shown below
worksheet1 = spreadsheet.get_worksheet(0)


