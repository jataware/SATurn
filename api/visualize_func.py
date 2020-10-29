from fbprophet import Prophet
from matplotlib import pyplot as plt
import plotly.graph_objects as go

import pandas as pd
import correlations as fc
import json


# build search string to filter raw df from ISI based on user countries
def stringify_countries(countries_list):

    countries_string = ""
    temp_list = []
    for country in countries_list:
        temp = f"(country == '{country}')"
        temp_list.append(temp)
    
    countries_string = " or ".join(temp_list)
    
    return countries_string 

# Filter df and build Figure object: Figure Object requires post-processing code plot the figure
def plot_it(df, countries_string):

    # build smaller df to get useful data from ISI "download"
    df_plot = pd.DataFrame()
    df_plot["time"] = df["time"]
    df_plot["value"] = df["value"]
    df_plot["country"] = df["country"]
    df_plot["variable_id"] = df["variable_id"]
    

    # Filter df to only countries of interest
    chart_data = df_plot.query(f"""{countries_string}""")
    chart_data = chart_data.sort_values(['country', 'time'])

    # Convert to plot object
    charts = []
    line_cfg = {'line': {'shape': 'spline', 'smoothing': 0.3}, 'mode': 'lines'}
    charts.append(go.Scatter(x=chart_data['time'], y=chart_data['value'], name='value', **line_cfg))
    figure = go.Figure(data=charts, layout=go.Layout({
        'legend': {'orientation': 'h'},
        'title': {'text': 'value by time (No Aggregation)'},
        'xaxis': {'title': {'text': 'time'}},
        'yaxis': {'title': {'text': 'value (No Aggregation)'}}}))

    return figure.to_json()	