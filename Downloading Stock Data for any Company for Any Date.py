# here your typically learning how to download historical stock data via python
# So going to 'finance.yaho.com' cause it has access to historical stock data of companies that are public. basically their shares values and all daily.
# So to find a company you should know that each company has a name-code for them in the stock market like 'AAPL' for 'apple' etc
import yfinance as yf
import requests

data = yf.download("TSLA", start="2010-06-29", end="2026-11-20")
data.to_csv("TSLA-Historical-Data.csv")

# Aside from the 'yfinace' we can use requests. but we need to have the url link and an example is the download url.
#Now because the 'yahoo finace' no longer allows free download, I am using a different link to download a file so i practice with requests
#NOTE: There will be some sites that don't let scripts download things from their website so we use something called headers.
#headers trick the site inti thinking it's a webbroswer.

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
} #This header basically works with almost any site and it will allow your script work in sites that block oython scripts from scraping or downloading.

contents = requests.get("https://idh-be.iowa.gov/api/v1/datasets/675/rows.csv", headers=headers).content
print(contents)

with open("iowa_immigration.csv", "wb") as file:
    file.write(contents)


# NOTE: BELOW IS HOW TO CONVERT A STRING TIME BACK TO A DATETIME OBJECT
from datetime import datetime
old_time_as_string = "2027/01/13"
str_to_datetime_converter = datetime.strptime(old_time_as_string, "%Y/%m/%d" )
print(str_to_datetime_converter) # THIS HAS OFFICIALLY CONVERTED THE DATETIME STRING BACK TO THE DATETIME OBJECT

#Now if you plan to then Convert the datetime object to an EPOCH time. you will do the below: # But you have to import time first
import time
from_epoch = time.mktime(str_to_datetime_converter.timetuple())
print(from_epoch) #Exactly now it has been converted to time in epoch version which is time in seconds.


