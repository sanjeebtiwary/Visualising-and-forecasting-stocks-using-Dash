from dash import Dash, html, dcc
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
from alpha_vantage.timesereies import Timeseries
from datetable import datetable as dt
app=dash.Dash(_name_)
server=app.server
app.layout = html.Div([item1, item2])
html.Div(
[
html.P("Welcome to the Stock Dash App!", className="start"),
html.Div([
# stock code input

]),
html.Div([
# Date range picker input
]),
html.Div([
# Stock price button
# Indicators button
# Number of days of forecast input
# Forecast button
]),
],
className="nav")