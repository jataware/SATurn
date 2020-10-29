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
import visualize_func as fv

# Get Credentials
wrk_dir = os.getcwd()
wrk_dir = wrk_dir + '/' 

config = configparser.ConfigParser()
configFile = wrk_dir + 'config.ini'
config.read(configFile)

user = config['CREDS']['user']
pwd = config['CREDS']['password']

def visualization_post(body):

    # ISI base url
    datamart_api_url = f'https://{user}:{pwd}@dsbox02.isi.edu:8888/datamart-api-wm'

    # search ISI and return df with variables and selected time/countries from openapi json
    df_raw = fc.raw_to_df(body, datamart_api_url)

    # Remove any user-selected countries not in dataset and return list with "good" countries
    countries_list= fc.filter(body, df_raw)
    
    # loop over countries and build single string to filter df
    countries_string = fv.stringify_countries(countries_list)
    
    # get figure object and convert to json
    plot_json = fv.plot_it(df_raw, countries_string)

    ## OR...could return a csv with the (time, value, country, variable_id)
    ## Either csv or figure requires post-porcessing to "see" the plot
    
    # plot_csv = chart_data
    # return plot_csv

    return plot_json
