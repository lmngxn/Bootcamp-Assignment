import json
from helper_functions import llm
import streamlit as st


def categorize_user_query(user_message):
    system_prompt = f"""
    First, read the <request> carefully about the type of people in the network they are looking for. You role is to break down the request into one or more of the 5 categories:
    - 'Profile': If the request is asking for whether people are students, working professionals, business owners or entrepreneurs. It can ask for multiple profiles.
    - 'Nationality': If the request includes about the nationality of the people. The request can also include if they are permanent residents of Singapore or not.
    - 'Location': If the request includes about where the people are based.
    - 'Occupation': If the request includes the occupational details of the people.
    - 'Education': If the request includes the educational details of the people.

    Your response must be a json format with the key being the categories and value being what the request is asking for in this category. You can omit the category if the request is not asking for it.
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