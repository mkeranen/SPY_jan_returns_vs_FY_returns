# -*- coding: utf-8 -*-
"""
Spyder Editor

This script compares January SPY returns to FY returns.
"""

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

#Read stock data into dataframe from .csv and use date as index
df = pd.read_csv('SPY_10yr_daily_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index(['Date'])

starting_year = 2008
ending_year = 2019

#Initialize dict for storing SPY returns information
returns = {}


#Function
def get_returns(year, df):
    """This function returns the january and full year (FY) growth of
    the stock passed in via dataframe for the specified year. The daily close
    price is used for all calculations"""
    
    year = str(year)
    
    jan_start_date = year + '-01-01'
    jan_end_date = year + '-01-31'
    
    FY_start_date = jan_start_date
    FY_end_date = year + '-12-31'
    
    jan_df = df.loc[jan_start_date:jan_end_date]
    FY_df = df.loc[FY_start_date:FY_end_date]
    
    jan_first_day_close = float(jan_df.iloc[0,3])
    jan_last_day_close = float(jan_df.iloc[-1,3])
    
    FY_first_day_close = jan_first_day_close
    FY_last_day_close =float(FY_df.iloc[-1,3])
    
    jan_return = (jan_last_day_close - jan_first_day_close) / jan_first_day_close
    FY_return = (FY_last_day_close - FY_first_day_close) / FY_first_day_close
    
    return jan_return, FY_return

if __name__ == "__main__":
    
    #For each year in the dataset, create a dict entry and then plot Jan vs FY returns
    for year in range(starting_year,ending_year):
        
        #Get returns for Jan and FY calling 'get_returns' function
        jan_returns, FY_returns = get_returns(year,df)
        
        #Create dict entry w/ year as key. Store tuple with jan & FY returns.
        returns[str(year)] = (100*jan_returns, 100*FY_returns)
        #print('Year: {}, January Return: {:.2%}, FY Return: {:.2%}'.format(year,jan_returns,FY_returns))
        plt.scatter(*returns[str(year)])
        plt.annotate(str(year),(100*jan_returns,100*FY_returns))
        
    
    #Format plot
    plt.axhline(color='grey', linewidth=0.5)
    plt.axvline(color='grey', linewidth=0.5)
    plt.title('SPY Jan Returns vs FY Returns')
    plt.xlabel('Jan Returns [%]')
    plt.ylabel('FY Returns [%]')
    plt.tight_layout()
    plt.savefig('SPY_Jan_Returns_vs_FY_Returns.pdf')
    plt.show()