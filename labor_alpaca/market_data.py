import alpaca_trade_api as tradeapi

api = tradeapi.REST(APCA_API_KEY_ID,
                    APCA_API_SECRET_KEY,
                    APCA_API_BASE_URL)

# Get daily price data for AAPL over the last 5 trading days.
barset = api.get_barset('AAPL', 'day', limit=5)
barset_min = api.get_barset('AAPL', 'hour', limit=5000)
aapl_bars = barset['AAPL']

# See how much AAPL moved in that timeframe.
week_open = aapl_bars[0].o
week_close = aapl_bars[-1].c
percent_change = (week_close - week_open) / week_open * 100
print('AAPL moved {}% over the last 5 days'.format(percent_change))
