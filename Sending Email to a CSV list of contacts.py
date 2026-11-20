import pandas
from datetime import datetime
import os
import time
import yagmail

my_password = os.getenv("password")
sender = os.getenv("email")

subject = "UPDATE: This is an AUTO email sent form extracted receivers in a csv file"

# message = f"""
# This email was sent as an automatic email and the sender got your email address
# from a csv file. HAHAHAHA!!
# """
df = pandas.read_csv("contacts.csv")

for index, row in df.iterrows():
    print(row["email"])
    #print(row)
yag = yagmail.SMTP(user=sender, password=my_password)
def auto_email(df, subject):
    for index, row in df.iterrows():

        message = f"""
Hi {row["name"]}, This email was sent as an automatic email and the sender got your email address ({row["email"]})
from a csv file. HAHAHAHA!! This is the final check.
"""
        email = yag.send(to=row["email"], subject=subject, contents=message)
    return email

while True:
    email_time = datetime.now()
    if email_time.hour == 16 and email_time.minute == 53:
        email = auto_email(df, subject)
        print("Email Sent")
        time.sleep(60)


