import datetime as dt
import smtplib

import pandas
import random

# save your own username and password into these variables
my_email = "myemail@gmail.com"
password = "abc123"

# Update the birthdays.csv with friends details.
# name,email,year,month,day
# YourName,your_own@email.com,today_year,today_month,today_day

# Check if today matches a birthday in the birthdays.csv
# Create a tuple from today's month and day using datetime. e.g.
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# Use pandas to read the birthdays.csv
data = pandas.read_csv("./birthdays.csv")

# Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
# Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
# e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
# Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Compare and see if today's month/day tuple matches one of the keys in birthday_dict :
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    # If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates
    # Use the random module to get a number between 1-3 to pick a randome letter.
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    # replace the [NAME] with the person's actual name from birthdays.csv
    with open(file_path) as letter_file:
        contents = letter_file.read()
        # Use the replace() method to replace [NAME] with the actual name.
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", ) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        # now send the mail
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}")




