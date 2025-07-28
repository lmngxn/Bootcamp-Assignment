# Set up and run this Streamlit App
import streamlit as st
from logics import first_pass as first
from helper_functions.utility import check_password  
from logics import categories as cat
from logics.get_data import call_data
import pandas as pd
import json

filepath = './data/metadata.json'
with open(filepath, 'r') as file:
    json_string = file.read()
    metadata = json.loads(json_string)

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

# Check if the password is correct.  
if not check_password():  
    st.stop()

st.title("Search Query Prototype")

default_data = {
    "Profile": "E.g. Working Professional, Student, Nationality",
    "Location": "E.g. City, Country",
    "Occupation": "E.g. Job Type, Industry, Job Level, Job Title, Company",
    "Education": "E.g. Course of Study, Qualification, School Name"
}

# Initialize session state for default data
for key in default_data:
    if key not in st.session_state:
        st.session_state[key] = ""

# Initialize session state for first submit
if "first_submit" not in st.session_state:
    st.session_state.first_submit = False

with st.expander("Disclaimer"):
    st.markdown("""
    IMPORTANT NOTICE: This web application is developed as a proof-of-concept prototype. The information provided here is NOT intended for actual usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

    Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

    Always consult with qualified professionals for accurate and personalized advice.
    """)
    
with st.form("Search Query"):
    user_prompt = st.text_input("Enter your request for types of members in the network")
    submitted1 = st.form_submit_button("Submit")
    if submitted1:
        st.toast(f"Input Submitted - {user_prompt}")
        
        # Reset session state before the new query
        for key in default_data:
            st.session_state[key] = ""
            
        with st.spinner("Understanding... Please wait."):
            response = first.categorize_user_query(user_prompt)

        st.write(response)
        if len(response) == 0:
            st.error("No appropriate categories found in the request. Please provide more details in your query.")
        else:
            for key, value in response.items():
                st.session_state[key] = ", ".join(value) if isinstance(value, list) else value
            st.session_state.first_submit = True


if st.session_state.first_submit:
    st.divider()
    with st.form("Search Query Refinement"):
        st.subheader("Edit Fields")
        st.write("Please further refine the search query based on the categories below. You can leave the field empty if you do not want to filter by that category.")
        
        # Use session_state to prefill and retain values
        for key in default_data:
            st.session_state[key] = st.text_input(key, value=st.session_state[key], help=default_data[key])

        search = st.form_submit_button("Search")
        st.session_state['query'] = False  # Reset query state for new search
        
        # Debugging output
        # st.json({k: st.session_state[k] for k in default_data})
        
        if search:
            st.toast(f"Query is being refined to match the metadata of the database")
            
            # Check if all fields are empty
            if all(not st.session_state.get(k) for k in default_data):
                st.error("No inputs found in any category. Please provide more details in your categories.")
                st.stop()
                
            st.divider()
            final_id = set()
            profile = location = occupation = education = None
            
            selection = dict()
                        
            with st.spinner("Refining... Please wait."):
                if st.session_state["Profile"]: 
                    profile = cat.filter_by_profile(st.session_state["Profile"])
                    for key in profile:
                        selection[key] = profile[key]
                if st.session_state["Location"]: 
                    location = cat.filter_by_location(st.session_state["Location"])
                    for key in location:
                        selection[key] = location[key]
                if st.session_state["Occupation"]: 
                    occupation = cat.filter_by_occupation(st.session_state["Occupation"])
                    for key in occupation:
                        selection[key] = occupation[key]
                if st.session_state["Education"]: 
                    education = cat.filter_by_education(st.session_state["Education"])
                    for key in education:
                        selection[key] = education[key]

            # Check if any results were found
            if not (profile or location or occupation or education):
                st.error("Your request is too broad or the data cannot be found in the system. Please refine your query.")
                st.stop()
         
            st.subheader("Search Filters by fields")

            for key, value in selection.items():
                if key in metadata:
                    st.multiselect(key, options=metadata[key], default=value, key=key)
                else:
                    st.text_input(key, value=', '.join(value), key=key)

            st.divider()
            with st.spinner("Now filtering from the database... Please wait."):
                data = call_data(profile, location, occupation, education)
                
            st.subheader("Search Results")
            df = pd.DataFrame(data)
            st.dataframe(df.head(10), use_container_width=True)