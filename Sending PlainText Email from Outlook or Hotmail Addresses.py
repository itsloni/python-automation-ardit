import smtplib
import os

sender = os.getenv("outlook_email")
receiver = "rielbumba@gmail.com"
password = os.getenv("outlook_password")
print(sender, password)

message = """\
Subject: Message Sent From Outlook(Python)

This is Loni!
Just wanted to say hi!
"""

server = smtplib.SMTP("smtp-mail.outlook.com", 587) # NOTE: The "smtp.offices365.com" is the host used for Those that have Microsoft365(work/School) outlook email
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()
