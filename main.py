import requests
import time
import os
import pandas as pd
import numpy as np
from telegram import Bot

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
API_KEY = os.getenv("API_KEY")
PAIR = os.getenv("PAIR", "AUD/USD")
INTERVAL = os.getenv("INTERVAL", "1min")
CANDLES = int(os.getenv("CANDLES", "10"))

bot = Bot(TOKEN)

def get_candles(pair):
    from_symbol, to_symbol = pair.split("/")
    url = f"https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol={from_symbol}&to_symbol={to_symbol}&interval={INTERVAL}&apikey={API_KEY}"
    data = requests.get(url).json()
    try:
        candles = list(data[f'Time Series FX ({INTERVAL})'].items())[:CANDLES]
        return candles
    except KeyError:
        print("API дерегі жоқ немесе лимит өтілді")
        return []

def analyze(candles):
    closes = [float(c[1]['4. close']) for c in candles]
    opens = [float(c[1]['
