import matplotlib.pyplot as plt
import pandas as pd

data_file = "../data/FXCM-H1.csv"

if __name__ == "__main__":
    df = pd.read_csv(data_file, parse_dates=['date'])
    dates = df['date'].tolist()
    closing_bids = df['closebid'].tolist()
    plt.scatter(dates, closing_bids)
    plt.savefig('closing_bids.png')
    
