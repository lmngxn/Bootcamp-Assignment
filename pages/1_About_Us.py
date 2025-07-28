# Set up and run this Streamlit App
import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->


st.title("Project Scope")

st.markdown("""
## The Problem Statment
Currently, the Singapore Global Network (SGN) has a database of members that is stored in Salesforce and not easily searchable or filterable by users 
who are not familiar with the report function. Therefore, the objective of this project is to create a prototype that allows users to search and filter the database 
using natural language queries and then using LLM to break it down to query the database.

## Current Situation
Previously, SGN had onboarded more than 10 different agencies onto Salesforce but ost of them found it difficult to pick up. As the usage frequency was low, many times
despite multiple training sessions, the officers were not able to remember how to use the system. To solve this issue, SGN officers will instead help the agencies to extract
the data. However, even then internal users also found it difficult to search for the data they needed as they were also sometimes unfamiliar with the filters.

## Proposed Solution
A dashboard on Tableau (part of the Salesforce suite of products) that allows users to search for members in the database using simplier filters were built. However,
as the user needs evolved, the dashboard needed to be updated frequently, which was not ideal. Hence, the idea of using LLMs to filter the database was tested.

## Objectives
- To create a prototype that allows users to search and filter the database using natural language queries.
- To use LLMs to break down the natural language queries into structured queries that can be used to filter the database.
- To allow users to refine their search criteria based on the initial results.
- To easily update the prototype to accommodate new fields in the database by updating the prompts.

## Impact
Improved user experience of 10 - 15 agencies who are interested to tap on SGN's database but had found it troublesome to use the Salesforce system. Often, the agencies
would only approach SGN if there were specific use cases, but this solution would allow them to explore the database more freely and discover new insights without necessary concrete use case.
Future iterations would allow for also simple analytics of the data (e.g. % of members in each industry, etc.) to be displayed to the users.
""")

st.title("Data Source")

st.markdown("""
## Usage of Synthetic Data
Although the current data set is classified as Official (Closed) Sensitive Normal, due to the particular sensitive nature of the data (contains personal information), synthetic data 
is used in this prototype. The synthetic data was generated using Mirage, an AI tool developed by GovTech Singapore, based on the original data provided by SGN. 
The synthetic data is also only a subset of the original datasize. It also only contains the key fields within the SGN database and not all the fields that are 
available in the original database. The current prototype also only is able to extract 100 records at a time to limit the amount of data processed
in this prototype.
""")

st.title("Features")

st.markdown("""
## First Breakdown of the query
The app will take in a natural language query and break it down into the following categories:
- **Profile**: Information about the member's profile, such as nationality, current status (e.g. student, working professional), and other personal details.
- **Location**: Geographical information about the member, including city and country.
- **Occupation**: Details about the member's job, including job type, industry, job level, job title, and company.
- **Education**: Information about the member's educational background, such as course of study, qualification, and school name.

## Further refinement of the query
The app will then prompt the user to refine their search criteria in the 4 categories based on the initial breakdown. The user can then edit the suggested search criteria or add new ones 
in each category using natural language.

## Filtering from the database
The app will then use the refined search criteria to filter the database and retrieve the relevant records. The results will be displayed in a table format, allowing users to easily view and easy copy the data out.
Current implementation of the database is using Supabase as a way to mimic a typical postgreSQL database. The data dictionary is shared in the tab "Data Dictionary" of this app.
""")

with st.expander("How to use this App"):
    st.markdown('''
    1. Enter your search criteria in the input box.
    
    2. Click on the "Submit" button.

    3. The app will prompt you to then refine your search criteria based on your earlier inputs.
    
    4. Click on the "Search" button to retrieve the data based on your refined search criteria.
    
    5. Finally, it will display the filters used to retrieve the data and the data itself.
    ''')