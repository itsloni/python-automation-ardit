import yagmail
import pandas
import os

my_password = os.getenv("password")
sender = os.getenv("email")
yag = yagmail.SMTP(user=sender, password=my_password)
df = pandas.read_csv("contacts.csv")


def auto_email(df):
    for index, row in df.iterrows():
        subject = f"Here's Your Bill For This Month {row["name"]}"
        content = [f"""
        Hey, {row["name"]} you have to pay {row["amount"]}
        Bill is attached!
        """, row["filepath"]]
        email = yag.send(to=row["email"], subject=subject, contents=content)
    return email

email = auto_email(df)
print("Email Sent!")