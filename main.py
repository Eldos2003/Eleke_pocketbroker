import requests
import time
import os
import pandas as pd
from telegram import Bot

# Telegram және API параметрлері (Koyeb Env Variables арқылы беріледі)
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
API_KEY = os.getenv("API_KEY")

# Валюталық жұптар
PAIRS = [
    "AUD/CAD", "AUD/CHF", "CAD/CHF", "EUR/RUB", "EUR/TRY",
    "EUR/USD", "NGN/USD", "UAH/USD", "USD/ARS", "USD/CHF",
    "USD/DZD", "USD/INR", "USD/JPY", "USD/MXN", "USD/MYR",
    "USD/THB", "USD/VND", "AUD/NZD"
]

INTERVALS = ["1min", "2min", "3min"]  # Интервалдар тізімі
CANDLES = 10

bot = Bot(TOKEN)

def get_candles(pair, interval):
    from_symbol, to_symbol = pair.split("/")
    url = f"https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol={from_symbol}&to_symbol={to_symbol}&interval={interval}&apikey={API_KEY}"
    data = requests.get(url).json()
    try:
        candles = list(data[f'Time Series FX ({interval})'].items())[:CANDLES]
        return candles
    except KeyError:
        print(f"API дерегі жоқ немесе лимит өтілді: {pair} {interval}")
        return []

def analyze(candles):
    closes = [float(c[1]['4. close']) for c in candles]
    opens = [float(c[1]['1. open']) for c in candles]
    df = pd.DataFrame({'open': opens, 'close': closes})
    df['MA5'] = df['close'].rolling(window=5).mean()
    df['MA10'] = df['close'].rolling(window=10).mean()
    last_close = df['close'].iloc[-1]
    ma5 = df['MA5'].iloc[-1]
    ma10 = df['MA10'].iloc[-1]
    if ma5 > ma10:
        confidence = min(95, 50 + (last_close - ma10)*100)
        signal = f"BUY ({confidence:.0f}% confidence)"
    elif ma5 < ma10:
        confidence = min(95, 50 + (ma10 - last_close)*100)
        signal = f"SELL ({confidence:.0f}% confidence)"
    else:
        signal = "WAIT"
    return signal

while True:
    for INTERVAL in INTERVALS:
        for PAIR in PAIRS:
            candles = get_candles(PAIR, INTERVAL)
            if candles:
                signal = analyze(candles)
                message = f"{PAIR} ({INTERVAL}) next candle: {signal} OTC+92%"
                print(message)
                bot.send_message(CHAT_ID, message)
    time.sleep(60)
