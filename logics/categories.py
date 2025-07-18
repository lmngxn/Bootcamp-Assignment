import json
from helper_functions import llm
import streamlit as st

filepath = './data/metadata.json'
with open(filepath, 'r') as file:
    json_string = file.read()
    metadata = json.loads(json_string)

def filter_by_profile(query):
    system_prompt = f"""\
    First, read the <request> carefully about the type of occupation being asked. You role is to suggest filters for each of the following datafields based on the metadata as follows:
    - 'Occupation': list is {metadata['Type']}.

    Your response must be a json format with the key being the categories and value being the possible filter the request is asking for in this category. You can omit the category if the request is not asking for it.
    """

    messages =  [
    {'role':'system',
    'content': system_prompt},
    {'role':'user',
    'content': f"<request>{query}</request>"},
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

def filter_by_nationality(query):
    system_prompt = f"""\
    First, read the <request> carefully about the type of nationality being asked. You role is to suggest filters for each of the following datafields based on the metadata as follows:
    - 'Nationality': list is {metadata['Nationality']}.
    - 'Permanent Resident of Singapore': Yes or No, whether the person holds a permanent resident status in Singapore.

    Your response must be a json format with the key being the categories and value being the possible filter the request is asking for in this category. You can omit the category if the request is not asking for it.
    """

    messages =  [
    {'role':'system',
    'content': system_prompt},
    {'role':'user',
    'content': f"<request>{query}</request>"},
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

def filter_by_location(query):
    system_prompt = f"""\
    First, read the <request> carefully about location being asked. You role is to suggest filters for each of the following datafields based on the metadata as follows:
    - 'Country': free text of country name, only suggest countries if there are specific countries requested.
    - 'State': 2 letter representation of US state, only suggest states if the request is asking for US and states can help to suggest the location.
    - 'City': free text of city name, only suggest cities within the country or state requested

    Your response must be a json format with the key being the categories and value being the possible filter the request is asking for in this category. You can omit the category if the request is not asking for it.
    """

    messages =  [
    {'role':'system',
    'content': system_prompt},
    {'role':'user',
    'content': f"<request>{query}</request>"},
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

def filter_by_occupation(query):
    system_prompt = f"""\
    First, read the <request> carefully about the type of occupation being asked. You role is to suggest filters for each of the following datafields based on the metadata as follows:
    - 'Company Name': free text of company name, only suggest companies if there are specific companies requested.
    - 'Industry': list of industry is {metadata['Industry']}. only suggest is there are specific job levels requested.
    - 'Sector': list of sector is {metadata['Sector']}, only applicable for banking and finance industry.
    - 'Job Function': list of job function is {metadata['Job Function']}. can also suggest some keywords to search using not in the list in a separate category.
    - 'Area of Specialization': list of area of specialization is {metadata['Area of Specialization']}. only applicable when Job Function is Technology. can also suggest some keywords to search using not in the list in a separate category.
    - 'Job Level': list of job level is {metadata['Job Level']}. only suggest is there are specific job levels requested.
    - 'Job Title': free text, suggest key words of titles that are relevant to the request.

    Your response must be a json format with the key being the categories and value being the possible filter the request is asking for in this category. You can omit the category if the request is not asking for it.
    """

    messages =  [
    {'role':'system',
    'content': system_prompt},
    {'role':'user',
    'content': f"<request>{query}</request>"},
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

def filter_by_education(query):
    system_prompt = f"""\
    First, read the <request> carefully about the education background. You role is to suggest filters for each of the following datafields based on the metadata as follows:
    - 'School Name': free text of school name, only suggest schools if there are specific schools requested.
    - 'Course of Study': list of course of study is {metadata['Course of Study']}. only suggest is there are field of study requested. you may suggest keywords outside of the list in a separate category.
    - 'Qualification': list of qualification is {metadata['Qualification']}, only suggest if they are looking for specific qualifications. you may suggest keywords outside of the list in a separate category.
    - 'Year of Graduation': value available is only between 2024 - 2040, only suggest if relevant to the request.

    Your response must be a json format with the key being the categories and value being the possible filter the request is asking for in this category. You can omit the category if the request is not asking for it.
    """

    messages =  [
    {'role':'system',
    'content': system_prompt},
    {'role':'user',
    'content': f"<request>{query}</request>"},
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