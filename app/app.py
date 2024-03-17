import streamlit as st


st.header("Hello from Cloud Run !")

show_balloons = st.button("Show balloons!")

if show_balloons:
    st.balloons()
    st.write("🎈")
