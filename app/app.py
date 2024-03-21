import streamlit as st

st.header("Hello from Cloud Run !")

button = st.button("Show balloons!")

if button:
    st.balloons()
