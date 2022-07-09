#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint

from data_manager import DataManager

google_sheet = DataManager()

pprint(google_sheet.get_google_sheet())
