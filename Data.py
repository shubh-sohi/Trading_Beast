import alpha_vantage.timeseries as avt
import csv
import pandas as pd
import os

API_KEY = 'MHB9U3GRQ1OFCN7Q'

def generateCSV(name):
    app = avt.TimeSeries(API_KEY)
    result = app.get_daily_adjusted('AAPL', outputsize='full')
    relevant_data = result[0]
    days_available = list(result[0].keys())
    days_available = days_available[0:101]

    days_available.reverse()

    with open(name + ".csv", "w") as csvfile:
        filewriter = csv.writer(csvfile)
        filewriter.writerow(["date", "open", "high", "low", "close", "adjusted_close", "volume"])
        for day in days_available:
            cur_day = relevant_data[day]
            filewriter.writerow([day, cur_day["1. open"], cur_day["2. high"], cur_day["3. low"], cur_day["4. close"], cur_day["5. adjusted close"], cur_day["6. volume"]])

def generate_pandas_data(filename):
    stock_data = pd.read_csv(filename)
    os.remove(filename)
    return stock_data

def combine_data(sma30, sma100, average, stock):
    data = pd.DataFrame()
    data[stock] = average["adjusted_close"]
    data["SMA30"] = sma30["adjusted_close"]
    data["SMA100"] = sma100["adjusted_close"]
    return data

if __name__ == "__main__":
    generateCSV("AAPL")
    print(generate_pandas_data("AAPL.csv"))