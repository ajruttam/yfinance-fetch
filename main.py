import yfinance as yf

tickers = [
    "NIFTYBEES.NS", "HDFCBANK.NS", "INFY.NS", "ONGC.NS", "RELIANCE.NS",
    "MID150BEES.NS", "IDEA.NS", "UNIONBANK.NS", "HINDPETRO.NS",
    "HDFCSML250.NS", "HINDCOPPER.NS", "IIFL.NS", "DELHIVERY.NS",
    "GOLDBEES.NS", "SILVERBEES.NS",
    "ASTRAZEN.NS",
    "AAPL", "MSFT", "NVDA", "AMZN", "TSLA",
    "LICNETFGSC.NS", "SETF10GILT.NS", "LIQUIDBEES.NS",
    "BTC-USD", "ETH-USD"
]

for tick in tickers:
    df = yf.download(tick,start="1900-01-01")
    # print(df)
    filename = tick.replace(".", "_")
    df.to_csv(f"{filename}.csv")
    print(tick, len(df))