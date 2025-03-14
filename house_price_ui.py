import streamlit as st
import joblib
import numpy as np

model = joblib.load('model.pkl')

st.title('🏡 House Price Prediction App')

area = st.number_input('Enter area (sq ft)', min_value=500, max_value=10000, step=50)
bedrooms = st.number_input('Enter number of bedrooms', min_value=1, max_value=10, step=1)
age = st.number_input('Enter house age (years)', min_value=1, max_value=100, step=1)

if st.button('Predict Price'):
    input_data = np.array([[area, bedrooms, age]])
    prediction = model.predict(input_data)[0]
    st.success(f'Estimated House Price: ₹{prediction:,.2f}')

st.markdown('---')
