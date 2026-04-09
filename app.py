import pickle
import numpy as np
import streamlit as st
from PIL import Image

# Title
st.markdown("<h1 style='text-align: center; color: cyan;'>💳 Credit Card Fraud Detection</h1>", unsafe_allow_html=True)

# Image
st.image("images.jpg")

# Description
st.write("This model predicts whether a transaction is fraudulent or legitimate using Machine Learning.")

# Instruction
st.info("Enter 29 comma-separated values (V1 to V28 + Amount)")

# Example
st.write("Example: -1.35, -0.07, 2.53, 1.37, ..., 149.62")

# ---------------- SESSION STATE ----------------
if "input_df" not in st.session_state:
    st.session_state.input_df = ""

# ---------------- BUTTONS ----------------
col1, col2 = st.columns(2)

with col1:
    if st.button("Use Sample Legitimate Data"):
        st.session_state.input_df = "-1.359807, -0.072781, 2.536347, 1.378155, -0.338321, 0.462388, 0.239599, 0.098698, 0.363787, 0.090794, -0.551600, -0.617801, -0.991390, -0.311169, 1.468177, -0.470401, 0.207971, 0.025791, 0.403993, 0.251412, -0.018307, 0.277838, -0.110474, 0.066928, 0.128539, -0.189115, 0.133558, -0.021053, 149.62"

with col2:
    if st.button("Use Sample Fraud Data"):
        st.session_state.input_df = "-2.312227, 1.951992, -1.609851, 3.997906, -0.522188, -1.426545, -2.537387, 1.391657, -2.770089, -2.772272, 3.202033, -2.899907, -0.595222, -4.289254, 0.389724, -1.140747, -2.830056, -0.016822, 0.416956, 0.126911, 0.517232, -0.035049, -0.465211, 0.320198, 0.044519, 0.177840, 0.261145, -0.143276, 0.00"

# ---------------- INPUT ----------------
input_df = st.text_input("Enter transaction details:", value=st.session_state.input_df)

# ---------------- PREDICT ----------------
submit = st.button("Predict")

if submit:
    try:
        input_df_split = input_df.split(',')
        features = np.asarray(input_df_split, dtype=np.float64)

        model = pickle.load(open('model.pkl', 'rb'))
        prediction = model.predict(features.reshape(1, -1))

        if prediction[0] == 0:
            st.success("✅ Legitimate Transaction")
        else:
            st.error("🚨 Fraudulent Transaction")

    except:
        st.warning("⚠️ Please enter valid comma-separated numeric values")