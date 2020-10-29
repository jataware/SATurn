#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:13:55 2020

@author: travishartman
"""

from requests import get,post,put,delete
from io import StringIO
import pandas as pd
import configparser
import requests
import json
import copy
import os


############ SEARCH FUNCTIONS ############ 

# Search ISI API
def isi_search(body, base_url):

    # verify that the search has proper (and at least one) parameter(s)
    param_errors = isi_search_validate(body)  

    if param_errors != []:
        return f'{param_errors}', 405, {'x-error': 'method not allowed'}

    else:
        # KEYWORD SEARCH
        # call urlify function to format url search string, searches " OR" keywords (not "and")
        search_url = urlify_search_keywords(body, base_url)
        
        print(search_url)

        #send get call to server
        response = get(search_url)
        json_string = response._content
        raw_results = json.loads(json_string)
        
        # call schema function to get into swagger schema format
        isi_keyword_results = isi_schema_results(raw_results)

        return isi_keyword_results
  
# This function prints an "error" and exits search if filter has unsupported filters
def isi_search_validate(body):

    vlad= []
    get_data ={"keywords": body.get("keywords", {}),
               "geo": body.get('area_name', {})
              }       

    #overall check, ensure not null search
    tah = [v for k,v in get_data.items() if v != {}]

    if len(tah) == 0:
        err = "Search requires at least one parameter"
        vlad.append(err)
 
    return vlad 

# Take user's keywords and format into url string to send to ISI server    
def urlify_search_keywords(body, base_url):
  
    # base_url: ...        /metadata/variables?
    # keywords ONly        /metadata/variables?keyword=
    # Country Only:        /metadata/variables?country=Ethiopia
    # Keyword and Country: /metadata/variables?keyword=road&country=Ethiopia

    amp_keywords = []
    amp_country = []

    keywords = body.get('keywords', "None")
    countries = body.get('area_name', "None")
    try:
        # Keywords and maybe Country:         
        if keywords != "None":
            for words in body['keywords']:
                new_word = words.replace(" ", "%20")
                amp_keywords.append(new_word)
        
            keyword_string ='&'.join(amp_keywords).strip()
        
            if countries != "None":
                for country in body['area_name']:
                    new_country = country.replace(" ", "%20")
                    amp_country.append(new_country)
        
                country_string = '&'.join(amp_country).strip()
                keyword_string =  keyword_string.strip() + '&country=' + country_string

            search_url = base_url + 'keyword=' + keyword_string

        # Country ONLY:    
        if keywords == "None" and countries != "None":
            for country in body['area_name']:
                new_country = country.replace(" ", "%20")
                amp_country.append(new_country)
        
            country_string = '&'.join(amp_country).strip()
            keyword_string =  keyword_string.strip() + '&country=' + country_string

            search_url = base_url + 'keyword=' + keyword_string

        return search_url

    except Exception as e:  
        return e


# transform raw return into schema format
def isi_schema_results(raw_results):
    
    isi_schema = []
    temp_dict = {}
    for result in raw_results:
        
        data_location = "ISI Datamart"
        dataset_id = result.get('dataset_id', "None")
        variable_id = result.get('variable_id', "None")
        name = result.get('name', "None")
        descr = "None"
        score = result.get('rank', "None")
    
        temp_dict= {"data_location": data_location,
                    "dataset_id": dataset_id,
                    "variable_id": variable_id,
                    "name": name,
                    "description": descr,
                    "score": score}
        
        isi_schema.append(temp_dict)
    
    # Testing...    
    # schema_results = json.dumps(isi_schema_results, indent = 4)
    
    return isi_schema

############ DOWNLOAD FUNCTION ############# 

# send list of variables to ISI API to download a dataset
def download_isi(dataset_id, body, datamart_api_url):

    df_all_variables = pd.DataFrame()
    
    variable_ids = body

    if variable_ids == []:
        err = {"Search requires at least one variable"}
        return f'{err}', 405, {'x-error': 'method not allowed'}
    
    else:
        for var in variable_ids:

            response = get(f'{datamart_api_url}/datasets/{dataset_id}/variables/{var}')
            df = pd.read_csv(StringIO(response.text))
            
            #if first variable...
            if df_all_variables.shape[0] == 0:
                df_all_variables = df

            else:
                df_all_variables = df_all_variables.append(df)

        #clean it up and covert to csv
        df_all_variables = df_all_variables.reset_index().drop(columns=['index'])
        df_all_variables = df_all_variables.to_csv()     

        return df_all_variables      
