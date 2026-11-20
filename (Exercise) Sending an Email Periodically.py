import os
import yagmail
from datetime import datetime

my_password = os.getenv("password")
print(my_password)
sender = os.getenv("sender")
receiver = "rielbumba@gmail.com"
subject = "Automated Exercise"
content = """
This is a Drill. I repeat, this is a Drill. Loni automating an email 
every minute...ahhhh! yay!
"""

yag = yagmail.SMTP(user= sender, password= my_password)
email = yag.send(to= receiver, subject= subject, contents=content)
for email:
    if
