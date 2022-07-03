import requests
import os
from datetime import date, timedelta

STOCK_NAME = "AAPL"
COMPANY_NAME = "Apple Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything?"

stock_api = os.environ.get("STOCK_API")
stock_url = f'{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={stock_api}'
stock_response = requests.get(stock_url)
stock_response.raise_for_status()
stock_data = stock_response.json()


# print(data["Time Series (Daily)"]["2022-07-01"]["4. close"])

# get today's date
today = date.today()

# # STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g.
#  [new_value for (key, value) in dictionary.items()]
# save yesterday's date in a variable
yesterday = today - timedelta(days=1)
yesterday_price = float(stock_data["Time Series (Daily)"][str(yesterday)]["4. close"])

# TODO 2. - Get the day before yesterday's closing stock price
# save yesterday's date in a variable
day_before_yesterday = today - timedelta(days=2)
day_before_yesterday_price = float(stock_data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"])

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp
price_difference = abs(yesterday_price - day_before_yesterday_price)

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday.
is_less = False
change = day_before_yesterday_price - yesterday_price
percent_change = change / day_before_yesterday_price * 100

if percent_change < 0:
    is_less = True
    percent_change *= -1

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
significant_change = False

if percent_change < 5:
    print("Getting News...")
    significant_change = True

# # STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if significant_change:
    news_api = os.environ.get("NEWS_API")
    news_url = f'{NEWS_ENDPOINT}q={COMPANY_NAME}&apiKey=0bd159ebe9c040f3b3100fe8b6813ca8'
    news_response = requests.get(news_url)
    news_response.raise_for_status()
    news_data = news_response.json()

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
#  Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    article_list = news_data["articles"][0:3]

# # STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    headline_list = [title for source["title"] in article_list]
# TODO 9. - Send each article as a separate message via Twilio.



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

