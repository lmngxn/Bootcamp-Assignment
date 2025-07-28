import streamlit as st
import pandas as pd
import json
from helper_functions.utility import check_password  

st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)

# Check if the password is correct.  
if not check_password():  
    st.stop()

# Define your data dictionary
data_dict = {
    "unique_id": "Unique identifier for each record. Primary Key",
    "Occupation": "Classifies the member as Student, Working Professional, Business Owner/Entrepreneur, or Other.",
    "Nationality": "Country of citizenship.",
    "Country, City, State": "Geographical location of the member. State is only applicable for US locations.",
    "Employee Count": "Number of full-time employees.",
    "Industry, Sector, Company Name": "In the industry of the member's company and the name of the company. Sector is applicable only for Banking and Finance industry.",
    "Job Function, Area of Specialization, Job Level, Job Title": "Details about the member's job role including function, specialization, level, and title.",
    "Year of Graduation, School Name, Course of Study, Qualification": "Details about the member's educational background."
}

# Convert to DataFrame
df = pd.DataFrame(list(data_dict.items()), columns=["Field Name", "Description"])

# Display as table
st.dataframe(df)  # or use st.table(df) for static

st.write("Examples of each field type as per below:")

st.divider()

filepath = './data/metadata.json'
with open(filepath, 'r') as file:
    json_string = file.read()
    metadata = json.loads(json_string)

st.json(metadata)
