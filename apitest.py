from alpha_vantage.timeseries import TimeSeries

app = TimeSeries('MHB9U3GRQ1OFCN7Q')
aapl = app.get_daily_adjusted('AAPL', outputsize='full')
with open('output.txt', 'a') as f:
    f.write(str(aapl))