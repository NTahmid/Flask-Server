import openai
import pandas as pd
import os
from IPython.display import display, HTML
import json
from redlines import Redlines
from IPython.display import display, Markdown
import re
import urllib.request as urllib2
import requests
from bs4 import BeautifulSoup
from IPython.display import Javascript
from string import Template
import IPython.display as dp
import time
import ast

# gpt-4 (Steves)
openai.api_key = "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"


def get_completion(prompt, model='gpt-4'):
    messages = [{'role': 'user', 'content': prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, )
    return response.choices[0].message["content"]


def str2dict(string_data):
    start = []
    stop = []
    for index, char in enumerate(string_data):
        if char == "{":
            start.append(index)
        if char == "}":
            stop.append(index)
    # Character not found
    try:
        a = start[0]
        b = stop[-1]
        dict_str = string_data[a: b + 1]
        dict_str = dict_str.replace("\'", "\"")
        #         print(dict_str)
        nested_dict = json.loads(dict_str)
        print(type(nested_dict))
        return nested_dict
    except:
        return string_data


def curriculum_chart_without_seperate_data(html_code):
    prompt = f"""
    Suppose you are a tacher, you want to teach a non-expert students how to interpret data from chart. Give list of topics to teach a non-expert about this chart and how to understand the data to get insights from this chart. Give your answer inside pyhton dictonary format like '1': 'topic 1' , '2' - 'topic 2'. No extra information other than python dictonary format.
    The html code is inside this backtick.
    ```{html_code}```    
    """
    response = get_completion(prompt)
    response = str2dict(response)
    print(type(response))
    print(response)
    return response


def curriculum_chart_with_seperate_data(html_code, data):
    prompt = f"""
    Suppose you are a tacher, you want to teach a non-expert students how to interpret data from chart. Give list of topics to teach a non-expert about this chart and how to understand the data to get insights from this chart. Give your answer inside pyhton dictonary format like '1': 'topic 1' , '2' - 'topic 2'. No extra information other than python dictonary format.
    The html code is inside this backtick.
    ```{html_code}```
    Data associated with this chart is inside this backtick.
    ```{data}```    
    """
    response = get_completion(prompt)
    response = str2dict(response)
    print(type(response))
    print(response)
    return response


def lessons_with_seperate_data(topics, topic_no, html_code):
    key_at_index = list(topics.keys())[topic_no - 1]
    value_at_index = topics[key_at_index]
    # print("--------------")
    # print(value_at_index)
    prompt = f"""
        Give contextual explanation of {value_at_index} from this chart. Don't give any explanation about coding, just focus on data interpretation from chart. No extra information other than python dictonary format.
        The chart is inside this backtick.
        ```{html_code}```
        """
    explanation = get_completion(prompt)
    explanation = str2dict(explanation)
    # print(explanation)
    return explanation


def contextual_explanation(topic_title, html_code, data):
    # print("--------------")
    # print(value_at_index)
    prompt = f"""
        Give contextual explanation of {topic_title} from this chart. Don't give any explanation about coding, just focus on data interpretation from chart. No extra information other than python dictonary format.
        The chart is inside this backtick.
        ```{html_code}```
        The data associate with it is inside this backtick.
        ```{data}```
        """
    explanation = get_completion(prompt)
    explanation = str2dict(explanation)
    # print(explanation)
    return explanation


def is_annotation_needed(topic_list, html_code, data):
    prompt = f"""
    Suppose you are a teacher and are handed a topic list for a chart. The topic list in question is:{topic_list}. Given this topic list, for which topics do you think the chart should be annotated. 
    You do not need an annotated chart for every topic. Only answer for which topics is an annotated chart more necessary than the other topics.
    Give your answer as a python dictionary format where the format is {{'1': Yes or No, '2': Yes or No,...}}. Only return the dictionary format
    The chart is inside this backtick. 
        ```{html_code}```
        The data associate with it is inside this backtick.
        ```{data}```
    """
    explanation = get_completion(prompt)
    explanation = str2dict(explanation)
    # print(explanation)
    return explanation


def annotate_code(topic_title, topic_explanation, html_code, data):
    prompt = f"""
    Suppose you are a teacher who is explaining a chart to a student. Given the topic title:{topic_title} and the corresponding explanation: {topic_explanation},
        modify the chart code and add annotations to it in accordance to the topic title and explanation. The colour of the annotations should NOT match the colors used in the chart.
        Shapes such as arrows, circles, lines etc can be used for annotations in addition to textual annotations. Use bright colors for annotations EXCEPT the colors that are already being used in the chart.
        Only return the whole code after modification. No other information is needed in the answer.
        The chart is inside this backtick.
        ```{html_code}```
        The data associate with it is inside this backtick.
        ```{data}```
    """

    explanation = get_completion(prompt)
    explanation = explanation.replace("```","")
    return explanation

