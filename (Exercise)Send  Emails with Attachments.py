import yagmail
import pandas
import os

my_password = os.getenv("password")
sender = os.getenv("email")
yag = yagmail.SMTP(user=sender, password=my_password)
df = pandas.read_csv("contacts.csv")

# NOTE: After I learnt this the file paths were removed from content.cvs by me to work on another task/project.
#So this script may not work or break. That's the reason.
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