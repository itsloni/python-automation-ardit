import os
import yagmail
from time import time
from datetime import datetime


my_password = os.getenv("password")
print(my_password)
sender = os.getenv("email")
receiver = "rielbumba@gmail.com"
subject = "Automated Exercise"
content = """
This is a Drill. I repeat, this is a Drill. Loni automating an email 
every minute...ahhhh! yay!
"""
def auto_email(my_password, sender, receiver, subject, content):
    yag = yagmail.SMTP(user=sender, password=my_password)
    email = yag.send(to=receiver, subject=subject, contents=content)
    email_time = datetime.now()
    return email_time,email

email_time, email = auto_email(my_password, sender, receiver, subject, content)
while True:
    current_time = time()
    if current_time > 60:
        print(email)
