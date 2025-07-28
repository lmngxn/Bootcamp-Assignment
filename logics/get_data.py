import streamlit as st
from supabase import create_client, Client
import json

filepath = './data/metadata.json'
with open(filepath, 'r') as file:
    json_string = file.read()
    metadata = json.loads(json_string)

# create a Supabase client
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def call_data(profile, location, occupation, education):
    """
    Call the Supabase database with a filter.
    filter will be in a dictionary/json format.
    Example: {"Occupation": "Working Professional", "Industry": "Education"}
    """
    search = supabase.table("profile data").select("*")
    
    if profile:
        for key in profile:
            search = search.in_(key, profile[key])

    if location:
        for key in location:
            search = search.in_(key, location[key])
            
    if occupation:
        if 'Job Level' in occupation:
            search = search.in_("Job Level", occupation["Job Level"])
        
        search_field_coy = ""
        search_field_ind = ""
        search_field_sec = ""
        search_field_jf = ""
        search_field_aos = ""
        search_field_jt = ""
        
        # Handle Company Name, Industry, and Sector as or search as they have overlaps
        if 'Company Name' in occupation:
            search_field_coy = ",".join([f'"Company Name".ilike.%{val}%' for val in occupation['Company Name']])
        if 'Industry' in occupation:
            search_field_ind = format_search_string("Industry", occupation["Industry"])
        if 'Sector' in occupation:
            search_field_sec = format_search_string("Sector", occupation["Sector"])

        search_joined_1 = ",".join([search_field_coy, search_field_ind, search_field_sec]).strip(",")
        if search_joined_1:
            search = search.or_(search_joined_1)

        # Handle Job Function, Area of Specialization, and Job Title as or search as they have overlaps
        if 'Job Function' in occupation:
            search_field_jf = format_search_string("Job Function", occupation["Job Function"])
        if 'Area of Specialization' in occupation:
            search_field_aos = format_search_string("Area of Specialization", occupation["Area of Specialization"])
        if 'Job Title' in occupation:
            search_field_jt = ",".join([f'"Job Title".ilike.%{val}%' for val in occupation['Job Title']])

        search_joined_2 = ",".join([search_field_jf, search_field_aos, search_field_jt]).strip(",")
        if search_joined_2:
            search = search.or_(search_joined_2)

    if education:
        if 'Year of Graduation' in education:
            search = search.in_("Year of Graduation", education["Year of Graduation"])
        if 'School Name' in education:
            search_field = ",".join([f"name.ilike.%{val}%" for val in education['School Name']])
            search = search.or_(search_field)
        if 'Course of Study' in education:
            search_field = format_search_string("Course of Study", education["Course of Study"])
            print(search_field)
            search = search.or_(search_field)
        if 'Qualification' in education:
            search_field = format_search_string("Qualification", education["Qualification"])
            search = search.or_(search_field)
    
    response = search.execute()

    return response.data


def format_search_string(key, value):
    search_text = ""
    non_picklist = []
    picklist = []
    
    # Check if the value is part of picklist, if not perform free text search on the others column
    for item in value:
        if item in metadata[key]:
            picklist.append(item)
        else:
            non_picklist.append(f'"{key} Others".ilike.%{item}%')
    if non_picklist:
        search_text += ",".join(non_picklist)
        
    #standardize picklist search
    if picklist:
        search_text += f',"{key}".in.({'"' + '","'.join(picklist) + '"'})'
    
    return search_text.strip(",")