import requests
from datetime import date, timedelta
import os
from email.message import EmailMessage
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
# date formmat = 2025-10-31
today = date.today()
yesterday = today - timedelta(days=1)
day_before = today - timedelta(days=2)

news_url = "https://newsapi.org/v2/everything?"
news_api = os.getenv("NEWS_API_KEY")
news_params = {
    "q": COMPANY_NAME,
    "from": str(day_before),
    "to": str(yesterday),
    "pageSize": 1,
    "language": "en",
    "sortBy": "popularity",
    "apiKey": news_api,
}
stock_url = "https://www.alphavantage.co/query"
stock_api = os.getenv("STOCK_API_KEY")
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": stock_api,
}

stock_response = requests.get(url=stock_url, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()

yesterday_data = stock_data["Time Series (Daily)"][str(yesterday)]
day_before_data = stock_data["Time Series (Daily)"][str(day_before)]
yesterday_close = float(yesterday_data["4. close"])
day_before_close = float(day_before_data["4. close"])
percentage_differnce = ((yesterday_close - day_before_close) / day_before_close) * 100

if abs(percentage_differnce) > 2:
    news_response = requests.get(url=news_url, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"][0]
    news_headline = news_data["title"]
    news_description = news_data["description"].replace("[Alternate URL.]", "").replace("\n", "")
    news_url = news_data["url"]
    icon_sign = "🔺"
    if percentage_differnce < 0:
        icon_sign = "🔻"
    subj = f"{STOCK}: {icon_sign} {abs(percentage_differnce)}%"
    msg = f"Headline: {news_headline}\nBrief: {news_description}"



    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_TOKEN")
    number = os.getenv("TWILIO_NUMBER")
    my_number = os.getenv("MY_NUMBER")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"{subj}\n{msg}",
        from_= number,
        to=my_number,
    )

print(message.body)
