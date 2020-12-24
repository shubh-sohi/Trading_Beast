import MovingAverageFormula as MAF
import Data as data
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    plt.style.use("fivethirtyeight")
    stock = "AAPL"
    data.generateCSV(stock)

    # store the data
    stock_data = data.generate_pandas_data(stock + ".csv")

    # sma for 30 days
    sma30 = MAF.moving_average(30, stock_data)
    #sma for 100 days
    sma100 = MAF.moving_average(100, stock_data)

    #combine data
    combined_data = data.combine_data(sma30, sma100, stock_data, stock)

    # visualize the data
    plot = [True, True, True] # keeps track of the plots to be made in the order: [average, sma30, sma100]
    MAF.visualize(combined_data, stock, plot)