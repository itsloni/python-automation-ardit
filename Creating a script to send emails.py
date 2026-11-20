import yagmail
import os

my_gmail_password = os.getenv("password") # This has to be a gmail App password not the normal password to gmail account !

print(my_gmail_password)

sender = "ayoolaoluwalonimi15@gmail.com"

receiver = "rielbumba@gmail.com"

subject = "This is the Subject"

contents = """
Here is the content of the email Hi!!
"""

yag = yagmail.SMTP(user=sender, password=my_gmail_password)
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent")