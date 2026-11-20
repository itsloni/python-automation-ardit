import os
import yagmail
import time
from datetime import datetime


my_password = os.getenv("password")
print(my_password)
sender = os.getenv("email")
receiver = "rielbumba@gmail.com"
subject = "TESTING: Sending an Email with Attachments"
content = ["""
This is a Drill. I repeat, this is a Drill. Loni automating an email 
every minute...ahhhh! yay!
""", 'text.txt'] # You add attachments by making the content a list and then after the content you want, you add a  comma ',' and then the path of the text file.
def auto_email(my_password, sender, receiver, subject, content):
    yag = yagmail.SMTP(user=sender, password=my_password)
    email = yag.send(to=receiver, subject=subject, contents=content)
    return email

while True:
    email = auto_email(my_password, sender, receiver, subject, content)
    print("Email Sent")
    time.sleep(60)

