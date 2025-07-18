# Set up and run this Streamlit App
import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("About this App")

st.markdown("This is a Streamlit App that demonstrates how to use the OpenAI API to filter a database.")
with st.expander("How to use this App"):
    st.markdown('''
    1. Enter your search criteria in the input box.
    
    2. Click on the "Submit" button.
    
    3. The app will generate a json format text to suggest how to filter the database based on your prompt.
    ''')