import connexion
import six

from openapi_server.models.search_result import SearchResult  # noqa: E501
from openapi_server import util


from itertools import chain
from requests import get,post,put,delete
from io import StringIO
import pandas as pd
import configparser
import requests
import json
import copy
import os
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


def search_post(body):

    print(body)

    search_url= f'https://{user}:{pwd}@dsbox02.isi.edu:8888/datamart-api-wm/metadata/variables?'
    search_results = fn.isi_search(body, search_url)

    return search_results

