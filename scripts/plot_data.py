import matplotlib.pyplot as plt
import pandas as pd

data_file = "../data/FXCM-H1.csv"
total_to_plot = 9400

if __name__ == "__main__":
    df = pd.read_csv(data_file, parse_dates=['date'])
    dates = df['date'].tolist()[:total_to_plot]
    closing_bids = df['closebid'].tolist()[:total_to_plot]
    volume = df['totalticks'].tolist()[:total_to_plot]
    plt.scatter(dates, closing_bids)
    plt.savefig('closing_bids.png')
    plt.scatter(dates, volume)
    plt.savefig('volume.png')
    
