from datetime import date
import numpy as np


#import re
#from textwrap import wrap
import dash
from dash import Dash, html, Input, Output, dcc
import dash_bootstrap_components as dbc
#import plotly.graph_objs as go
#import pandas as pd
#import glob
import os

def build_hours_slider():
    total_hrs_ints = list(np.arange(1,7,1))
    total_hrs_strs = [str(x) for x in total_hrs_ints]
    slider_hrs_dict = dict(zip(total_hrs_strs, total_hrs_strs))
    return slider_hrs_dict

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

#now = datetime.utcnow()
#endyear = now.year + 1
root_dir = 'C:/data/'
#root_dir = '/home/tjturnage/'
#DATA_DIR = root_dir + 'TEXT_DATA'
#FSW_OUT_DATA = os.path.join(root_dir,'FSW_OUTPUT/fsw_output.txt')
#print(FSW_OUT_DATA)


app.layout = dbc.Container(
    html.Div([
        dbc.Row(dbc.Col(html.Div(html.Hr()))),
        dbc.Row(
            html.Div([
    dcc.DatePickerSingle(
        id='my-date-picker-single',
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed=date(2017, 9, 19),
        initial_visible_month=date(2017, 8, 5),
        date=date(2017, 8, 25)
    ),
    html.Div(id='output-container-date-picker-single')            
            ])
        )
    ])

)

@app.callback(
    Output('output-container-date-picker-single', 'children'),
    Input('my-date-picker-single', 'date'))
def update_output(date_value):
    string_prefix = 'You have selected: '
    if date_value is not None:
        date_object = date.fromisoformat(date_value)
        date_string = date_object.strftime('%B %d, %Y')
        return string_prefix + date_string

if __name__ == '__main__':
    app.run_server(debug=True)