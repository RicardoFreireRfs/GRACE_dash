from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import numpy as np
import rasterio


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

# dataframes using Pandas to define the years and input data definition
years = np.arange(2004,2023)
year_df = pd.DataFrame(years, columns=['Year'])
input_def = {'Groundwater','Moisture'}
input_df = pd.DataFrame(input_def, columns=['input_select'])

app.layout = html.Div([
    # ------------ Title ------------ #
    html.Div([
        html.H1(id='H1', children='GRACE Groundwater and Soil Moisture Conditions Dashboard',
            style={'textAlign': 'center','marginTop': 40, 'marginBottom': 20,"font-family": "verdana"}),
        html.H2(id='H2', children='Pale Blue Dot: Visualization Challenge',
            style={'textAlign': 'center','marginTop': 5, 'marginBottom': 15,
                   "font-family": "Arial","font-size": '20px',"font-weight": "bold"}),
        html.H3(id='H3', children='by Ricardo F. da Silva',
            style={'textAlign': 'center', 'marginTop': 5, 'marginBottom': 15,
                   "font-family": "Arial", "font-size": '15px', "font-weight": "italic"})]),
    html.Div([
        html.H4(id='H4', children='Groundwater and soil moisture indicators are based on terrestrial water storage observations derived from GRACE-FO satellite data and integrated with other observations, using a sophisticated numerical model of land surface water and energy processes. This data product is GRACE Data Assimilation for Drought Monitoring (GRACE-DA-DM) Global Version 3.0 from a global GRACE and GRACE-FO data assimilation and drought indicator product generation (Li et al., 2019). It varies from the other GRACE-DA-DM products which are from the U.S. GRACE-based drought indicator product generation (Houborg et al., 2012). Source: https://disc.gsfc.nasa.gov/datasets/GRACEDADM_CLSM025GL_7D_3.0/summary',
                style={'textAlign': 'left', 'marginTop': 5, 'marginBottom': 15,
                       "font-family": "Arial", "font-size": '15px'})]),

# Input data selection - Left side
    html.Div([

        html.Div([
            html.Label("Select an input data:"),
            dcc.Dropdown(
                    input_df['input_select'].unique(),
                    'Groundwater',
                    id='crossfilter-input-data',
                    style={'width': '49%', "margin-left": "15px"}
                    )
        ],
            style={'width': '49%', 'display': 'inline-block'}),
# Input data selection - right side
        html.Div([
            html.Label("Select an input data:"),
            dcc.Dropdown(
                    input_df['input_select'].unique(),
                    'Groundwater',
                    id='crossfilter-input-data2',
                    style={'width': '49%', "margin-left": "15px"}
                    )
        ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
    ], style={
        'padding': '5px 1px'
    }),

# World map /Year bar - Left side
    html.Div([
        dcc.Graph(id='crossfilter_tif_image'),
        html.Label("Year:"),
        dcc.Slider(
            year_df['Year'].min(),
            year_df['Year'].max(),
            step=None,
            id='crossfilter-year--slider',
            value=year_df['Year'].max(),
            marks={str(year): str(year) for year in year_df['Year'].unique()}
        ),
# World map / Year bar - Right side
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
        dcc.Graph(id='crossfilter_tif_image2'),
        html.Label("Year:"),
        dcc.Slider(
            year_df['Year'].min(),
            year_df['Year'].max(),
            step=None,
            id='crossfilter-year--slider2',
            value=year_df['Year'].max(),
            marks={str(year): str(year) for year in year_df['Year'].unique()}
        ),
    ], style={'display': 'inline-block', 'width': '49%'}),
    html.Div(dcc.Graph(id='crossfilter_timeseries',style={'height': '90vh'})
             , )

])


@callback(
    Output('crossfilter_tif_image', 'figure'),
    Output('crossfilter_tif_image2', 'figure'),
    Output('crossfilter_timeseries', 'figure'),
    Input('crossfilter-input-data', 'value'),
    Input('crossfilter-year--slider', 'value'),
    Input('crossfilter-input-data2', 'value'),
    Input('crossfilter-year--slider2', 'value')
)

def update_graph(input_data,
                 year_value,input_data2,
                 year_value2):
    dff = year_df[year_df['Year'] == year_value]

    inputdata_str = str(input_data)
    tif_file = inputdata_str + "_" + str(dff)[-4:] + ".tif"

    # Load the geotiff file
    with rasterio.open(tif_file) as src:
        data = src.read(1)
    data[data == -999] = -1
    # Create the heatmap trace
    layout = go.Layout(title='Time Averaged Map' + " " + str(dff)[-4:])
    fig = go.Figure(layout=layout)

    hover_text = '<b>' + inputdata_str + ': %{z:.5f} </b>'
    fig.add_trace(go.Heatmap(
        z=np.fliplr(np.flip(data)),
        hovertemplate=hover_text, name=''
    ))
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    # fig.update_layout(
    #     xaxis=dict(
    #         tickmode='array',
    #         tickvals=np.arange(-180,180,10),
    #     ),
    #     yaxis = dict(
    #     tickmode='array',
    #     tickvals=np.arange(-90, 90,10),
    #     )
    # )

    dff2 = year_df[year_df['Year'] == year_value2]

    inputdata_str2 = str(input_data2)
    tif_file2 = inputdata_str2 + "_" + str(dff2)[-4:] + ".tif"

    # Load the geotiff file
    with rasterio.open(tif_file2) as src:
        data2 = src.read(1)
    data2[data2 == -999] = -1
    # Create the heatmap trace
    layout2 = go.Layout(title='Time Averaged Map' + " " + str(dff2)[-4:])
    fig2 = go.Figure(layout=layout2)

    hover_text2 = '<b>' + inputdata_str2 + ': %{z:.5f} </b>'
    fig2.add_trace(go.Heatmap(
        z=np.fliplr(np.flip(data2)),
        hovertemplate=hover_text2, name=''
    ))
    fig2.update_xaxes(visible=False)
    fig2.update_yaxes(visible=False)

# Plot time-series data
    df_ts = pd.read_csv('Global_groundwater_2004_2022.csv')
    df2_ts = pd.read_csv('Global_Soil_noisture_2004_2022.csv')

    fig3 = go.Figure(go.Scatter(
        x=df_ts['time'],
        y=df_ts['groundwater'], name='Groundwater'
    ))

    fig3.add_trace((go.Scatter(
        x=df2_ts['time'],
        y=df2_ts['moisture'], name='Moisture'
    )))
    fig3.update_layout(title_text='Time Series - Global Average')
    fig3.update_xaxes(title_text='Time')
    fig3.update_traces(hovertemplate='%{y}<br>Date: %{x}')
    fig3.update_yaxes(title_text='Time Averaged (percentile weekly)')
    fig3.update_xaxes(rangeslider_visible=True)

    return fig, fig2, fig3

if __name__ == '__main__':
    app.run(debug=True)
