"""
Page to inspect imported data from Kaggle et al.
"""
import streamlit as st

def inspect_data_body():
    st.write("### Import Data")
    st.write("Data to import")
    st.info('Information...')
    st.write("---")

    import requests
    response = requests.get('https://api.covid19api.com/summary')
    response

    st.write("### Inspect Data")