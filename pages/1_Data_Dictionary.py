import streamlit as st
import pandas as pd
import json
from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()

filepath = './data/metadata.json'
with open(filepath, 'r') as file:
    json_string = file.read()
    metadata = json.loads(json_string)

st.json(metadata)
