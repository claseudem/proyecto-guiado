import yfinance as yf

def download_stock_data_bronze(tickers, period='1mo'):
    data = yf.download(tickers, period=period)["Close"]
    data.reset_index(inplace=True)
    data = data.astype(str)
    return data


def download_stock_data_between(tickers, period=None, start=None, end=None):
    if period:
        data = yf.download(tickers, period=period)["Close"]
    else:
        data = yf.download(tickers, start=start, end=end)["Close"]
    data.reset_index(inplace=True)
    return data

