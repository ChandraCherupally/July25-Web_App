import streamlit as st
import pandas as pd


st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.write("Hello, *World!* :sunglasses:")


df = pd.read_csv('cars24-car-price.csv')

st.write(df)

agree = st.checkbox("I agree")
if agree:
    st.write("Great!")


genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")