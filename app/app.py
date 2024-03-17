import streamlit as st


st.header("Hello from Cloud Run !")

show_balloons = st.button("Show balloons!")

st.write("This change has been deployed via a CICD powered by Cloudbuild")

if show_balloons:
    st.balloons()
    st.write("🎈")
