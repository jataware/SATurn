#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  22 14:23:55 2020

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


##### GET DATA ######

# Send list of variables to ISI API to download a dataset
def raw_to_df(body, datamart_api_url):

    df_all_variables = pd.DataFrame()
    
    ids = body['ids']

    if ids == []:
        err = {"Search requires at least one variable"}
        return f'{err}', 405, {'x-error': 'method not allowed'}

    # add all variables to a single dataframe
    else:
        for key in ids.keys():
        
            dataset_id = ids[key]["dataset_id"]
            var = ids[key]["variable_id"]

            response = get(f'{datamart_api_url}/datasets/{dataset_id}/variables/{var}')
            df_temp = pd.read_csv(StringIO(response.text))
        
            #if first variable...
            if df_all_variables.shape[0] == 0:
                df_all_variables = df_temp

            else:
                df_all_variables = df_all_variables.append(df_temp)

        #clean it up for return
        df_all_variables = df_all_variables.reset_index().drop(columns=['index'])
        
        # Convert timestamp to date format
        df_all_variables.loc[:, 'time'] = pd.Series(pd.to_datetime(df_all_variables['time'], infer_datetime_format=True), name='time', index=df_all_variables['time'].index)


        # ADD time filter
        if body.get('time', "None") != "None":

            start = body["time"].get("start", "None")
            end = body["time"].get("end", "None")
            
            print(f'Time filter applied: {start} < timestamp < {end}')

            # START and END time
            if start != "None" and end != "None":
                df_all_variables.loc[:, 'time'] = pd.Series(pd.to_datetime(df_all_variables['time'], infer_datetime_format=True), name='time', index=df_all_variables['time'].index)
                df_all_variables = df_all_variables.query(f"time >= Timestamp('{start}') and time <= Timestamp('{end}')")

            # START ONLY
            if start != "None" and end == "None":
                df_all_variables.loc[:, 'time'] = pd.Series(pd.to_datetime(df['time'], infer_datetime_format=True), name='time', index=df_all_variables['time'].index)
                df_all_variables = df.query(f"time >= Timestamp('{start}')")

            # END ONLY
            if start == "None" and end != "None":
                df_all_variables.loc[:, 'time'] = pd.Series(pd.to_datetime(df_all_variables['time'], infer_datetime_format=True), name='time', index=df_all_variables['time'].index)
                df_all_variables = df_all_variables.query(f"time <= Timestamp('{end}')")                
        
        return df_all_variables      

#### Filter by time and country
def filter(body, df):

    # Filter out countries not indicated by user
    countries = body["country"]
    
    lister = list(df['country'])
    inds = []
    
    # get indices of "bad" countries and delete from countries list
    i=0
    for country in countries:
        if country not in lister:
            print(f"{country} not in dataset...skipping")
            inds.append(i)
        i += 1    
    for ind in sorted(inds, reverse=True):
        del countries[ind] 
    
    # Print to terminal...
    print(f'Country filter applied: {*countries,}')

    return countries

# PIVOT TABLE: turn data so countries=columns, rows=timestamp
def pivot_country(body, df, countries):
    
    if countries != []:
        # For future? use...right
        correlator = body["correlators"]

        df = pd.pivot_table(df, index=['time'], columns=['country'], values=['value'], aggfunc='mean')
        df.columns = df.columns.droplevel(0)
        df = df.rename_axis(None, axis=1)

        if isinstance(df, (pd.DatetimeIndex, pd.MultiIndex)):
            df = df.to_frame(index=False)

        # remove any pre-existing indices for ease of use
        df = df.reset_index().drop('index', axis=1, errors='ignore')
        df.columns = [str(c) for c in df.columns]  # update columns to strings in case they are numbers
        
        df = df[countries]

        return df
    else:
        e = f"Your contries where not in the dataset for the set time frame"
        return e

# PIVOT TABLE: FOR ONE COUNTRY/GEO: turn data so variables=columns, rows=timestamp 
def pivot_vars(body, df, country):
    
    if country != []:
        # For future? use...right
        correlator = body["correlators"]

        df = pd.pivot_table(df, index=['time'], columns=['variable_id'], values=['value'])

        df.columns = df.columns.droplevel(0)
        df = df.rename_axis(None, axis=1)

        if isinstance(df, (pd.DatetimeIndex, pd.MultiIndex)):
            df = df.to_frame(index=False)

        # remove any pre-existing indices for ease of use
        df = df.reset_index().drop('index', axis=1, errors='ignore')
        df.columns = [str(c) for c in df.columns]  # update columns to strings in case they are numbers
        

        return df
    else:
        e = f"Your country/geo was not in the dataset for the set time frame"
        return e

# take selected variables and get the Pearson correlation coeff matrix
def corr(body, df):

    # Not currently used: correlations are from pivot table that are for a single variable_id
    correlations = body["correlators"]
    
    corr_data = df.corr(method='pearson')
    corr_data.index.name = str('column')
    corr_data = corr_data.reset_index()

    # Round correlation to four decimals
    corr_data = corr_data.round(4)   

    return corr_data







