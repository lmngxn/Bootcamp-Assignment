# Set up and run this Streamlit App
import streamlit as st
# from helper_functions import llm # <--- This is the helper function that we have created 🆕
from logics import first_pass as first
from helper_functions.utility import check_password  
from logics import categories as cat

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

# Check if the password is correct.  
# if not check_password():  
#     st.stop()

st.title("Search Query Prototype")

default_data = {
    "Profile": "",
    "Nationality": "",
    "Location": "",
    "Occupation": "",
    "Education": ""
}

for key in default_data:
    if key not in st.session_state:
        st.session_state[key] = default_data[key]

if "first_submit" not in st.session_state:
    st.session_state.first_submit = False

with st.form("Search Query"):
    user_prompt = st.text_input("Enter your request for types of members in the network")
    submitted1 = st.form_submit_button("Submit")
    if submitted1:
        st.toast(f"User Input Submitted - {user_prompt}")
        for key in default_data:
            st.session_state[key] = ''
        # Simulate calling a function
        response = first.categorize_user_query(user_prompt)
        st.write(response)
        if len(response) == 0:
            st.error("No categories found in the request. Please provide more details in your query.")
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
            st.session_state[key] = st.text_input(key, value=st.session_state[key])

        submitted2 = st.form_submit_button("Submit")
        st.session_state['query'] = False  # Reset query state for new search
        # st.json({k: st.session_state[k] for k in default_data})
        if submitted2:
            if all(not st.session_state.get(k) for k in default_data):
                st.error("No inputs found in any categoriy. Please provide more details in your categories.")
                st.stop()
                
            st.divider()
            with st.spinner("Searching... Please wait."):
                if st.session_state["Profile"]: 
                    profile = cat.filter_by_profile(st.session_state["Profile"])
                    if len(profile) != 0:
                        st.session_state['query'] = True
                if st.session_state["Nationality"]: 
                    nationality = cat.filter_by_nationality(st.session_state["Nationality"])
                    if len(nationality) != 0:
                        st.session_state['query'] = True
                if st.session_state["Location"]: 
                    location = cat.filter_by_location(st.session_state["Location"])
                    if len(location) != 0:
                        st.session_state['query'] = True
                if st.session_state["Occupation"]: 
                    occupation = cat.filter_by_occupation(st.session_state["Occupation"])
                    if len(occupation) != 0:
                        st.session_state['query'] = True
                if st.session_state["Education"]: 
                    education = cat.filter_by_education(st.session_state["Education"])
                    if len(education) != 0:
                        st.session_state['query'] = True
            
            if not st.session_state['query']:
                st.error("No filters found in the request. Please refine your query.")
                st.stop()

            st.subheader("Search Query Results")

            if st.session_state["Profile"]: 
                st.markdown("**Profile Filters**")
                st.write(profile)
            if st.session_state["Nationality"]: 
                st.markdown("**Nationality Filters**")
                st.write(nationality)
            if st.session_state["Location"]: 
                st.markdown("**Location Filters**")
                st.write(location)
            if st.session_state["Occupation"]: 
                st.markdown("**Occupation Filters**")
                st.write(occupation)
            if st.session_state["Education"]: 
                st.markdown("**Education Filters**")
                st.write(education)

        # df = pd.DataFrame(course_details)
        # st.divider()
        # st.dataframe(df)