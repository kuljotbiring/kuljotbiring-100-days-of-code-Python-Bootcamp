import requests


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_url = "https://api.sheety.co/e16bd98df5e37971e300376e218ae6fe/flightDeals/prices"

    def get_google_sheet(self):
        sheet_response = requests.get(url=self.sheety_url)
        return sheet_response.json()

