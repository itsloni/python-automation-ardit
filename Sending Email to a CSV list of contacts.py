import pandas
from datetime import datetime
import os
import time
import yagmail

my_password = os.getenv("password")
sender = os.getenv("email")

subject = "This is an AUTO email sent form extracted receivers in a csv file"

message = """
This email was sent as an automatic email and the sender got your email address fro a csv file. HAHAHAHA!
"""
df = pandas.read_csv("contacts.csv")
print(df)
def auto_email(my_password, sender, subject, message):
    yag = yagmail.SMTP(user=sender, password=my_password)
    email = yag.send(to=sender, subject=subject, contents=message)
    return email

while True:
    email_time = datetime.now()
    if email_time.hour == 13 and email_time.minute == 1:
        email = auto_email(my_password, sender, subject, message)
        print("Email Sent")
        time.sleep(60)


