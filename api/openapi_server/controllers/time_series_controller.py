import connexion
import six

from openapi_server.models.ids import Ids 
from openapi_server import util

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

import timeseries_func as ft
import correlations as fc

# Get Credentials
wrk_dir = os.getcwd()
wrk_dir = wrk_dir + '/' 

config = configparser.ConfigParser()
configFile = wrk_dir + 'config.ini'
config.read(configFile)

user = config['CREDS']['user']
pwd = config['CREDS']['password']

def timeseries_post(body):

    # ISI base url
    datamart_api_url = f'https://{user}:{pwd}@dsbox02.isi.edu:8888/datamart-api-wm'

    # get raw data from ISI DM 
    df_raw = fc.raw_to_df(body, datamart_api_url)
     
    #...and convert to "Prophet" friendly dataframe
    df_slim = ft.filter_df(df_raw, body)

    # call function to get fit and forecast; return "forecast" dataframe
    forecast = ft.fit_ts(df_slim)

    return forecast.to_csv(index=False)



