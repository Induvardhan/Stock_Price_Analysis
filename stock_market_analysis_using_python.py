pip install yfinance #Mandatory

import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px

today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=365)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

data = yf.download('ADANIENT.NS',
                      start=start_date,
                      end=end_date,
                      progress=False)
data["Date"] = data.index
data = data[["Date", "Open", "High", "Low",
             "Close", "Adj Close", "Volume"]]
data.reset_index(drop=True, inplace=True)
print(data.head())

"""Whenever you analyze the stock market, always start with a candlestick chart. A candlestick chart is a handy tool to analyze the price movements of stock prices. Here’s how you can visualize a candlestick chart of Google’s stock prices:

### Reading a Candle
![here](https://ih1.redbubble.net/image.2255911038.6803/st,small,845x845-pad,1000x1000,f8f8f8.jpg)
"""

figure = go.Figure(data=[go.Candlestick(x=data["Date"],
                                        open=data["Open"], high=data["High"],
                                        low=data["Low"], close=data["Close"])])
figure.update_layout(title = "Google Stock Price Analysis", xaxis_rangeslider_visible=False)
figure.show()

"""A bar plot is also a handy visualization to analyze the stock market, specifically in the long term. Here’s how to visualize the close prices of Google’s stock using a bar plot:


"""

figure = px.bar(data, x = "Date", y= "Close")
figure.show()

"""One of the valuable tools to analyze the stock market is a range slider. It helps you analyze the stock market between two specific points by interactively selecting the time period. Here’s how you can add a range-slider to analyze the stock market:"""

figure = px.line(data, x='Date', y='Close',
                 title='Stock Market Analysis with Rangeslider')
figure.update_xaxes(rangeslider_visible=True)
figure.show()

"""Another interactive feature you can add for stock market analysis is time period selectors. Time period selectors are like buttons that show you the graph of a specific time period. For example, a year, three months, six months, etc. Here is how you can add buttons for selecting the time period for stock market analysis:"""

figure = px.line(data, x='Date', y='Close',
                 title='Stock Market Analysis with Time Period Selectors')

figure.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
figure.show()

"""The weekend or holiday season always affects the stock market. So if you want to remove all the records of the weekend trends from your stock market visualization, below is how you can do it:

"""

figure = px.scatter(data, x='Date', y='Close', range_x=['2021-07-12', '2022-07-11'],
                 title="Stock Market Analysis by Hiding Weekend Gaps")
figure.update_xaxes(
    rangebreaks=[
        dict(bounds=["sat", "sun"])
    ]
)
figure.show()

"""## Summary

So this is how you can use the Python programming language to analyze the stock market interactively. Stock Market Analysis means analyzing the current and historical trends in the stock market to make future buying and selling decisions. I hope you liked this article on Stock Market Analysis using Python. Feel free to ask valuable questions in the comments section below.
"""
