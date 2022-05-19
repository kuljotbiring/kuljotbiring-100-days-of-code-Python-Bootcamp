import smtplib
import datetime as dt
import random

# save your own username and password into these variables
my_email = "myemail@gmail.com"
password = "abc123"

# get the datetime for right now
now = dt.datetime.now()
# get the weekday it is
weekday = now.weekday()

# check if it is Monday
if weekday == 0:
    with open("./quotes.txt") as file:
        # list to store quotes from text file
        quote_list = file.readlines()
        # select a random quote from the list
        random_quote = random.choice(quote_list)

    # create a connection using an SMTP object connecting to provider's SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        # make the connection secure - encrypting the message
        connection.starttls()
        # log into the account to use
        connection.login(user=my_email, password=password)
        # now send the mail
        connection.sendmail(
            from_addr=my_email,
            to_addrs="xyz@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{random_quote}")


