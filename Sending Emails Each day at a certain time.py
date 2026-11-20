import os
import yagmail
import time # this has time in seconds only
from datetime import datetime # here you can write "from datetime import datetime as dt" the as dt means the
# datetime imported will be represented as 'dt' instead of typing datetime when calling it.


my_password = os.getenv("password")
print(my_password)
sender = os.getenv("email")
receiver = "rielbumba@gmail.com"
subject = "Daily Automated Exercise"
content = """
This is a Drill. I repeat, this is a Drill. Loni automating an email 
every day at 1:37 pm ...ahhhh! yay!
"""
def auto_email(my_password, sender, receiver, subject, content):
    yag = yagmail.SMTP(user=sender, password=my_password)
    email = yag.send(to=receiver, subject=subject, contents=content)
    return email

while True:
    email_time = datetime.now()
    if email_time.hour == 14 and email_time.minute == 1:
        email = auto_email(my_password, sender, receiver, subject, content)
        print("Email Sent")
        time.sleep(60) # note that the 60 is in seconds which is 1 minute, but if you want to sleep for 1 hour then its 3600 seconds

