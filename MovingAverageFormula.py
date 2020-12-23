import pandas as pd
import matplotlib.pyplot as plt

def moving_average(days, stock_data):
    sma = pd.DataFrame()
    sma["adjusted_close"] = stock_data["adjusted_close"].rolling(window=days).mean()
    return sma

def visualize(data, stock):
    plt.figure(figsize=(12.5, 4.5))
    plt.plot(data[stock], label=stock)
    plt.plot(data["SMA30"], label="SMA30")
    plt.plot(data["SMA100"], label="SMA100")
    plt.ylabel("Adjusted close price(USD)")
    plt.legend(loc="upper left")
    plt.draw()
    plt.show()

def buy_sell_signal():
    return None