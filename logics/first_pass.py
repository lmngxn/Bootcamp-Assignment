import json
from helper_functions import llm
import streamlit as st


def categorize_user_query(user_message):
    system_prompt = f"""
    First, read the <request> carefully about the type of people in the network they are looking for. You role is to break down the request into one or more of the 5 categories. the query can go into multiple categories:
    - 'Profile': If the request is asking for about nationality, or whether they are students, working professionals, business owners or entrepreneurs. It can ask for multiple profiles.
    - 'Location': If the request includes about where the people are based like country, city or region.
    - 'Occupation': If the request includes the occupational or professions detail of the people like job function, industry, company name, job level.
    - 'Education': If the request includes the educational details of the people.

    Your response must be a json format with the key being the categories and value being what the request is asking for in this category. 
    Do not create sub categories embedded in each category, only return everything as a list of values.
    Do not create any new categories that are not listed above.
    You can omit the category if the request is not asking for it.
    """

    messages =  [
    {'role':'system',
    'content': system_prompt},
    {'role':'user',
    'content': f"<request>{user_message}</request>"},
    ]

    response = llm.get_completion_by_messages(messages)

    try:
        # If content is clean JSON
        result = json.loads(response)

    except json.JSONDecodeError:
        # If content has extra text, try to extract just the JSON block
        import re
        match = re.search(r'{.*}', response, re.DOTALL)
        if match:
            json_str = match.group(0)
            result = json.loads(json_str)
        else:
            raise ValueError("No valid JSON object found in response")
    
    
    return result