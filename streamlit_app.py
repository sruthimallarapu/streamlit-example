import streamlit as st

st.sidebar.title('Smart Farm Surveillance')
st.sidebar.subheader('Settings')

base_genre = st.sidebar.selectbox("Choose your preference",('About Smart Farm Surveillance','Livestock Monitoring','Object Detection in Farm'))
