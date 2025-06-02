import yfinance as yf
import pandas as pd


def download():
    ticker = "MNQ=F"
    period = "2y"
    interval = "1h"
    file = f"{ticker}-{period}_{interval}.csv"
    try:
        data = yf.download(
            ticker, period=period, interval=interval, multi_level_index=False
        )
        data.to_csv(file)
    except Exception as e:
        print(f"Execption: {e}")

    return


download()
