from requests import get,post,put,delete
from io import StringIO
import pandas as pd
import configparser
import requests
import json
import os

from fbprophet import Prophet
from matplotlib import pyplot as plt
import plotly.graph_objects as go


import numpy as np
from PIL import Image
from matplotlib.backends.backend_agg import FigureCanvasAgg


#filter to single country of interest and reduce to "ds"=time and "y"=value only
def filter_df(df, body):

    # country filter
    country = body["country"][0]
    df_country = df[df["country"] == country]
             
    # pare down to time and value columns for ts fit and rename to match "Prophet" naming convention                                                    
    df_slim = df_country[["time", "value"]]
    df_slim.columns = ['ds', 'y']

    return df_slim


# Fit the ts by implementing Facebook Prophet module
def fit_ts(df):

    m = Prophet(weekly_seasonality=False)

    proph = m.fit(df)
    future = m.make_future_dataframe(periods=1)
    forecast = m.predict(future)    
    
    # ...this crashes python...
    #print('Plot saved to your working directory as "test.png"')
    #m.plot(forecast).savefig('test.png')
    
    print(proph)
    return forecast


