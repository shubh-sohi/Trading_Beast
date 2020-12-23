import alpha_vantage.timeseries as avt
import csv

API_KEY = 'MHB9U3GRQ1OFCN7Q'

def generateCSV(name):
    app = avt.TimeSeries(API_KEY)
    result = app.get_daily_adjusted('AAPL', outputsize='full')
    relevant_data = result[0]
    days_available = list(result[0].keys())
    days_available.reverse()

    with open(name + ".csv", "w") as csvfile:
        filewriter = csv.writer(csvfile)
        filewriter.writerow(["date", "open", "high", "low", "close", "adjusted_close", "volume"])
        for day in days_available:
            cur_day = relevant_data[day]
            filewriter.writerow([day, cur_day["1. open"], cur_day["2. high"], cur_day["3. low"], cur_day["4. close"], cur_day["5. adjusted close"], cur_day["6. volume"]])