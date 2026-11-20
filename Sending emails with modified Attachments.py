import yagmail
import pandas
import os

my_password = os.getenv("password")
sender = os.getenv("email")
yag = yagmail.SMTP(user=sender, password=my_password)
df = pandas.read_csv("contacts.csv")

def generate_file(filename, content):
    with open(filename, "w") as file:
        file.write(str(content))
    return filename


def auto_email(df):
    for index, row in df.iterrows():
        name = row["name"]
        amount = row["amount"]
        receivers_email = row["email"]
        filename_ext = name + ".txt"
        filename = generate_file(filename_ext, amount)
        subject = f"Final: Here's Your Bill For This Month {name}"
        content = [f"""
        Hey, {name} you have to pay {amount}
        Bill is attached!
        """, filename]
        email = yag.send(to=receivers_email, subject=subject, contents=content)
    return email

email = auto_email(df)
print("Email Sent!")