# Set up and run this Streamlit App
import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Methodology")

st.markdown("""
## First Pass of the Query
The app will take in a natural language query and break it down into the 4 categories:
- **Profile**: Information about the member's profile, such as nationality, current status (e.g. student, working professional), and other personal details.
- **Location**: Geographical information about the member, including city and country.
- **Occupation**: Details about the member's job, including job type, industry, job level, job title, and company.
- **Education**: Information about the member's educational background, such as course of study, qualification, and school name.

## First Display of the Results
The app will then display the results based on the first pass of the query. The results will be displayed in 4 free text boxes, one for each category. 
The user can then refine the search criteria by adding, removing or shifting the suggested filters from the free text boxes.

## Refinement of the Query
The app will then take the input from each category and pass them through different prompts to refine the query. 
The relevant metadata of each fields in the database is also shared wit the LLM to help it adjust the query to the database structure.

## Second Display of the Results
The app will then display the results based on the refined query, as well as the filters used for the search. 
""")

with open('./data/Assignment Flowchart.drawio.svg', "r") as f:
    svg = f.read()

st.image(svg)