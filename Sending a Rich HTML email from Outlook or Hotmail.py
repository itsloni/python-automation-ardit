import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = os.getenv("outlook_email")
receiver = "rielbumba@gmail.com"
password = os.getenv("outlook_password")
print(sender, password)

message = MIMEMultipart() # Note to call this class you do it like it's a dictionary so message is like the variable of the dictionary. and the MIMEMultipart() has like keys and the expected values
message["From"] = sender
message["To"] = receiver
message["Subject"] = "Hello Again!" # subject is always plain text that's why we used a string

body = """
<h2>Hi there!</h2>
There are only 2 cats flying today!
Let's hope for more!
"""
# Now to attach this body to the email we use th '.attach()' method. It's not for attaching files or anything Just solely for attaching the body to the email as seen below.
mimetext = MIMEText(body, "html") # if you write 'plain' in the _subtype place then python sees it as a plaintext and will print the body including the <h2>. but if it html it will understand and work as espected
message.attach(mimetext)


server = smtplib.SMTP("smtp-mail.outlook.com", 587) # NOTE: The "smtp.offices365.com" is the host used for Those that have Microsoft365(work/School) outlook email
server.starttls()
server.login(sender, password)
message_text_string = message.as_string() # Important because the 'server.sendmail()' expects a string message but our message variable above is somewhat o a dictionary so this line is what converts it to a string.
print(message_text_string)
server.sendmail(sender, receiver, message_text_string)
server.quit()
