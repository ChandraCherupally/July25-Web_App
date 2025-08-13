import pytz
import yfinance as yf
import streamlit as st
import datetime


text_input = st.text_input(
        "Enter Stock Ticker Symbol (e.g., BTC-USD,AAPL,GOOGL,TSLA)",
        "BTC-USD"
    )

col1, col2 = st.columns(2)
with col1:
    d = st.date_input("Start Date:", datetime.date(2024, 8, 1))
with col2:
    e = st.date_input("End Date:", datetime.date(2025, 8, 12))


ticker_data = yf.Ticker(text_input)
ticker_df = ticker_data.history(start=d, end=e)

## ticker_df = ticker_data.history(period="60d", interval="5m")
# Convert from UTC to IST
#ticker_df.index = ticker_df.index.tz_convert(pytz.timezone("Asia/Kolkata"))
# Sort so latest is first
##ticker_df = ticker_df.sort_values(by="Datetime", ascending=False)


st.header("Stock Market Analyzer")
st.subheader("This webapp shows information about the stock market.")
st.write(f"Showing data for {text_input}.")
st.dataframe(ticker_df)

st.write(f"Closing Price chart for {text_input}.")
st.line_chart(ticker_df["Close"])

st.write(f"Volume chart for {text_input}.")
st.line_chart(ticker_df["Volume"])
