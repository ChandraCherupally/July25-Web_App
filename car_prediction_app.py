import streamlit as st
import pandas as pd
import pickle

cars_df = pd.read_csv('cars24-car-price.csv')

st.write(""" 
### Car Price Prediction App
This app predicts the price of used cars based on various features.
""")

st.dataframe(cars_df.head())



# Load the encoding mapping
encode_df = pd.read_csv("encoding_mapping.csv")


# Layout
col1, col2,col3 = st.columns(3)

year = col1.selectbox("Select the year", cars_df['year'].astype(int).unique())
seller_type = col1.selectbox("Select the seller type", ["Dealer", "Individual","Trustmark Dealer"])
km_driven = col1.slider("Set the KM Driven", 1000, 300000, step=1000)
fuel_type = col2.selectbox("Select the fuel type", ["Diesel", "Petrol", "CNG", "LPG", "Electric"])
transmission_type = col2.selectbox("Select the transmission type", ["Manual", "Automatic"])
mileage = col2.slider("Set the Mileage", 0, 50, step=1)
engine = col3.slider("Set the Engine Power", 500, 5000, step=100)
max_power = col3.slider("Set the Max Power", 30, 500, step=10)
seats = col3.selectbox("Enter the number of seats", [4, 5, 7, 9, 11])


fuel_type_code = int(encode_df[(encode_df['category'] == 'fuel_type') & (encode_df['label'] == fuel_type)]['code'].values[0])
transmission_code = int(encode_df[(encode_df['category'] == 'transmission_type') & (encode_df['label'] == transmission_type)]['code'].values[0])
seller_type_code = int(encode_df[(encode_df['category'] == 'seller_type') & (encode_df['label'] == seller_type)]['code'].values[0])
input_features = [[year,seller_type_code,km_driven,fuel_type_code,transmission_code, mileage,engine,max_power,seats]]

# Read the model

def model_pred(input_features):
    with open("car_pred", "rb") as file:
        reg_model = pickle.load(file)
    return reg_model.predict(input_features)

if st.button('Predict Price'):
    # Filter by both category and label
    predicted_price = model_pred(input_features)
    st.write(f"The predicted price of the car is @: ₹{predicted_price[0]:,.2f} lac")



