import pandas as pd
import pandas_datareader as pdm
import matplotlib.pyplot as plt



def plot_by_year(df):
    """
    Plots the returns distribution by year from 1999 to 2019 in subplots. 
    """
    plt.style.use('ggplot')

    # convert to Series for charting
    ts = pd.Series(df['daily_return'].values, index=df['price_date'])
    
    for a, i in enumerate(range(1999, 2019),1):
        plt.subplot(7,4, a)
        plt.subplots_adjust(top = 0.9, bottom= 0.1, hspace = 0.9)
        plt.hist(ts[str(i)], 100, alpha=0.75)
        plt.title(i)
        plt.suptitle("S&P500 Returns Distribution by Year")
    
    plt.show()
    


# Get symbol to lookup
symbol = input("Enter a symbol: ")

df = pdm.get_data_yahoo(symbol, start_date ='1999-01-01')


# daily return
df['daily_return'] = df['close_price'].pct_change(1)*100

# drop any NaN
df.dropna(inplace=True)


plot_by_year(df)
 
  
