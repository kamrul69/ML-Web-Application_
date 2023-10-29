import streamlit as st
import yfinance as yf


st.write('''
         # Simple Stock Price App
         ''')

# to define Ticker symbol
tickerSymbol='GOOGL'
# to get the data on this ticker

tickerData=yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf_daily= tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
st.write('''
         #### Shown are ***daily*** the stock ***closing price*** and ***volumn*** of Google!
         ''')
tickerDf_daily
st.write(
    '''
    ##### Closing Price
    '''
)
st.line_chart(tickerDf_daily.Close)

st.write(
    '''
    ##### Volumn Price
    '''
)
st.line_chart(tickerDf_daily.Volume)
st.write('-----------------------------------------')
#get the historical prices for this ticker
tickerDf_monthly= tickerData.history(period='1mo', start='2010-5-31', end='2020-5-31')
st.write('''
         #### Shown are ***monthly*** the stock ***closing price*** and ***volumn*** of Google!
         ''')
tickerDf_monthly
st.write(
    '''
    ##### Closing Price
    '''
)
st.line_chart(tickerDf_monthly.Close)

st.write(
    '''
    ##### Volumn Price
    '''
)
st.line_chart(tickerDf_monthly.Volume)