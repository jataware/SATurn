import connexion
import six

from openapi_server.models.ids import Ids
from openapi_server import util


from requests import get,post,put,delete
from io import StringIO
import pandas as pd
import configparser
import requests
import os

import correlations as fc

# Get Credentials
wrk_dir = os.getcwd()
wrk_dir = wrk_dir + '/' 

config = configparser.ConfigParser()
configFile = wrk_dir + 'config.ini'
config.read(configFile)

isi_user = config['CREDS']['user']
isi_pwd = config['CREDS']['password']


def correlation_post(body):

    datamart_api_url = f'https://{isi_user}:{isi_pwd}@dsbox02.isi.edu:8888/datamart-api-wm'
    
    df_raw = fc.raw_to_df(body, datamart_api_url)
    countries = fc.filter(body, df_raw)
    df_pivot = fc.pivot_it(body, df_raw, countries)
    corr_matrix = fc.corr(body, df_pivot)

    #result = corr_matrix.to_csv()
    if type(df_pivot) == str:
    	result = df_pivot
    else:
        result = corr_matrix.to_csv()	
        
    return result
