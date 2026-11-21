import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender = os.getenv("outlook_email")
receiver = "rielbumba@gmail.com"
password = os.getenv("outlook_password")
print(sender, password)

message = MIMEMultipart() # Note to call this class you do it like it's a dictionary so message is like the variable of the dictionary. and the MIMEMultipart() has like keys and the expected values
message["From"] = sender
message["To"] = receiver
message["Subject"] = "Using Outlook To Send Email With Attachments!" # subject is always plain text that's why we used a string

body = """
<h2>Hi there!</h2>
There are only 2 cats flying today!
Let's hope for more!
"""
# Now to attach this body to the email we use th '.attach()' method. It's not for attaching files or anything Just solely for attaching the body to the email as seen below.
mimetext = MIMEText(body, "html") # if you write 'plain' in the _subtype place then python sees it as a plaintext and will print the body including the <h2>. but if it html it will understand and work as expected
message.attach(mimetext)

#To add an attachment we simply just add a set of code at here in this place between the code above and the code that establishes the server.
attachment_path = "Malayan Tiger.pdf" # Basically jus write the name of the file . make sure it's in the same directory as this script.
attachment_file = open(attachment_path, "rb")
payload = MIMEBase("application", "octet-stream") # This argument most be stated when calling the MIMEBase
payload.set_payload(attachment_file.read())
encoders.encode_base64(payload) # This is added specifically after the payload has been set cause it will then encode teh already set payload so it is converted to format that can run on the system
payload.add_header("Content-Disposition", "attachment", filename=attachment_path) # This is where u add the header and the filename is what the attachment will be named and if left empty python will fill anything
# but it's best to lead it to the actual name of the file hich is 'Malayan Tiget.pdf' and is inside the variable 'attachment_path'
message.attach(payload)



#NOTE: The lines of code below is basically what is needed to establish the server connection for the outlook email to send
server = smtplib.SMTP("smtp-mail.outlook.com", 587) # NOTE: The "smtp.offices365.com" is the host used for Those that have Microsoft365(work/School) outlook email
server.starttls()
server.login(sender, password)
message_text_string = message.as_string() # Important because the 'server.sendmail()' expects a string message but our message variable above is somewhat o a dictionary so this line is what converts it to a string.
print(message_text_string)
server.sendmail(sender, receiver, message_text_string)
server.quit()
