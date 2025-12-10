# Forex Trading Signal Telegram Bot

## Overview
A Python-based Telegram bot that sends forex trading signals. The bot fetches candlestick data from Alpha Vantage API, performs technical analysis using moving averages, and sends buy/sell signals via Telegram.

## Project Architecture
- `main.py` - Main bot script that runs continuously
- `requirements.txt` - Python dependencies

## Key Dependencies
- `python-telegram-bot==13.15` - Telegram bot API
- `requests` - HTTP requests for API calls
- `pandas` - Data analysis
- `numpy` - Numerical operations

## Environment Variables Required
The following environment variables must be set:
- `TOKEN` - Telegram bot token
- `CHAT_ID` - Telegram chat ID to send messages to
- `API_KEY` - Alpha Vantage API key

## How to Run
Run the bot using:
```bash
python main.py
```

The bot will continuously fetch forex data every 60 seconds and send trading signals to the configured Telegram chat.

## Currency Pairs Monitored
AUD/CAD, AUD/CHF, CAD/CHF, EUR/RUB, EUR/TRY, EUR/USD, NGN/USD, UAH/USD, USD/ARS, USD/CHF, USD/DZD, USD/INR, USD/JPY, USD/MXN, USD/MYR, USD/THB, USD/VND, AUD/NZD

## Intervals
1min, 2min, 3min
