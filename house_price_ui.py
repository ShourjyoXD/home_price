
import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('model.pkl')

# App UI
st.title('🏡 House Price Prediction App')

# Input fields for user data
area = st.number_input('Enter area (sq ft)', min_value=500, max_value=10000, step=50)
bedrooms = st.number_input('Enter number of bedrooms', min_value=1, max_value=10, step=1)
age = st.number_input('Enter house age (years)', min_value=1, max_value=100, step=1)

# Prediction logic
if st.button('Predict Price'):
    input_data = np.array([[area, bedrooms, age]])
    prediction = model.predict(input_data)[0]
    st.success(f'Estimated House Price: ₹{prediction:,.2f}')

# Footer
st.markdown('---')
st.markdown('**Created with ❤️ using Streamlit**')
    