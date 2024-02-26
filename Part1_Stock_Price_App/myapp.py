import yfinance as yf
import streamlit as st
from datetime import date

today=date.today()

st.write("""
# Simple Stock Price App

Shown are the stock ***closing price*** and **volume** of ****Google****!

""")

today=date.today()

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end=today )
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""**Clossing Price**""")
st.line_chart(tickerDf.Close)

st.write("""**Volume**""")
st.line_chart(tickerDf.Volume)


