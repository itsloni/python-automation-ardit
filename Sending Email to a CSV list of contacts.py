import pandas
from datetime import datetime
import os
import time
import yagmail

my_password = os.getenv("password")
sender = os.getenv("email")

subject = "This is an AUTO email sent form extracted receivers in a csv file"

message = """
This email was sent as an automatic email and the sender got your email address 
from a csv file. HAHAHAHA!!
"""
df = pandas.read_csv("contacts.csv")

for index, row in df.iterrows():
    print(row["email"])
    #print(row)

def auto_email(df, my_password, sender, subject, message):
    for index, row in df.iterrows():
        yag = yagmail.SMTP(user=sender, password=my_password)
        email = yag.send(to=row["email"], subject=subject, contents=message)
    return email

while True:
    email_time = datetime.now()
    if email_time.hour == 15 and email_time.minute == 51:
        email = auto_email(df, my_password, sender, subject, message)
        print("Email Sent")
        time.sleep(60)


