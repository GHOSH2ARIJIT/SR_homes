from django.db import models
import yfinance as yf
import pandas as pd

def Profile():
    #Profile data for Arijit
    name = 'Arijit Ghosh'
    data = {
        'class_10th_result':'67 percent',
        'class_12th_result':'84 percent',
        'WBJEE_result':'96 percentile',
        'programming_languages':'Python, C++, Java',
        'Web_Development':'HTML, CSS, JavaScript',
        'Database_Management':'MySQL, MongoDB',
        'Tools':'Git, React, TensorFlow',
        'Education':'B.Tech in Computer Science',
        'college_name':'Kalyani Government Engineering College',
        'Year_of_Study':'from 2022 to 2026',
        'Relevant_Courses':' Data Structures, Algorithms, Object-Oriented Programming, Operating Systems',
        'weather_api_app':'it is an application made of python to show weather details using api',
        'voice_maker':'it is an application made of python to speakout the entered sentence ',
        

    }

    return data


def BSE_history_5days(start="2023-01-01",end="2023-12-31"):
    bse_ = yf.Ticker("^BSESN")
    hist = bse_.history(period="5d")
    #df = ticker.history(start , end )
    return pd.DataFrame(hist)
