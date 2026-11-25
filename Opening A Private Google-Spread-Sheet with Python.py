# So here we have to configure the API cause we have to tell google that we are the owner of the
# private google spread sheet. Hence the url for the spreadsheet is not enough
#So essentially google will have to give you an api key which you will then use to access the sheet to change,
# delete data, update, edit etc.

# To do this we need the 'gspread' library and then you get an api key from google.
#To get google api what you do is search for google api console, set up your google drive API(already did that you only set it up once) AND THEN YOU ENABLE GOOGLE SPREADSHEET API.
import gspread


