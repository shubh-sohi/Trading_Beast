import MovingAverageFormula as MAF
import Data as data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


if __name__ == "__main__":
    plt.style.use("fivethirtyeight")
    stock = "AAPL"
    data.generateCSV(stock)

    # store the data
    stock_data = pd.read_csv(stock + ".csv")

    # visualize the data
    plt.figure(figsize=(12.5, 4.5))
    plt.plot(stock_data["Adj Close Price"])
