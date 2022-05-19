# import smtplib
#
# # save your own username and password into these variables
# my_email = "myemail@gmail.com"
# password = "abc123"
#
# # create a connection using an SMTP object connecting to provider's SMTP server
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     # make the connection secure - encrypting the message
#     connection.starttls()
#     # log into the account to use
#     connection.login(user=my_email, password=password)
#     # now send the mail
#     connection.sendmail(from_addr=my_email, to_addrs="xyz@yahoo.com", msg="Subject:Hello"
#                                                                           "\n\nPython Email Automation Test")


