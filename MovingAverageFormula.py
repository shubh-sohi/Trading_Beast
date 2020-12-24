import pandas as pd
import matplotlib.pyplot as plt

def moving_average(days, stock_data):
    sma = pd.DataFrame()
    sma["adjusted_close"] = stock_data["adjusted_close"].rolling(window=days).mean()
    return sma

def visualize(data, stock, plot):
    plt.figure(figsize=(12, 5))

    if plot[0]:
        plt.plot(data[stock], label=stock, linewidth=2.0)
    if plot[1]:
        plt.plot(data["SMA30"], label="SMA30", linewidth=2.0)
    if plot[2]:
        plt.plot(data["SMA100"], label="SMA100", linewidth=2.0)
    plt.ylabel("Adjusted close price(USD)")
    plt.xlabel("Date")
    plt.legend(loc="upper left")

    plt.draw()
    plt.show()

def buy_sell_signal():
    return None