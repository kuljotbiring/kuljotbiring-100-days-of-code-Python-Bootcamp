import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 38.637241
MY_LONG = -121.512604

# save your own username and password into these variables
MY_EMAIL = "myemail@gmail.com"
PASSWORD = "abc123"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def is_close(MY_LAT, MY_LONG, iss_lat, iss_long):
    if (MY_LAT - 5) <= iss_lat <= (MY_LAT + 5) <= 5 and (MY_LONG - 5) <= iss_long <= (MY_LONG + 5):
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False


while True:
    # BONUS: run the code every 60 seconds.
    time.sleep(60)
    # If the ISS is close to my current position
    if is_close(MY_LAT, MY_LONG, iss_latitude, iss_longitude):
        # and it is currently dark
        if is_night():

            # Then send myself an email to tell me to look up.
            # create a connection using an SMTP object connecting to provider's SMTP server
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                # make the connection secure - encrypting the message
                connection.starttls()
                # log into the account to use
                connection.login(user=MY_EMAIL, password=PASSWORD)
                # now send the mail
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:ISS is located overhead"
                                    "\n\nLook outside! The ISS is flying overhead")




