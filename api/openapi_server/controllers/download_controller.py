import connexion
import six
from openapi_server import util

from requests import get,post,put,delete
from io import StringIO
import pandas as pd
import configparser
import requests
import os

import isi_functions as fn

# Get Credentials
wrk_dir = os.getcwd()
wrk_dir = wrk_dir + '/' 

config = configparser.ConfigParser()
configFile = wrk_dir + 'config.ini'
config.read(configFile)

user = config['CREDS']['user']
pwd = config['CREDS']['password']

data_location = "ISI"

def download_variables_data_location_dataset_id_post(dataset_id, body):

    datamart_api_url = f'https://{user}:{pwd}@dsbox02.isi.edu:8888/datamart-api-wm'
    
    downloaded = fn.download_isi(dataset_id, body, datamart_api_url)   
    
    return downloaded