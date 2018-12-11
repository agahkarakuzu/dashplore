# Data driven callbacks 
# Instead of this you can have a slider and chart interact with each other as well.as

import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

import pandas as pd

df = pd.read_csv('/Users/Agah/Desktop/DashAndDonuts/dash-workshop/gapminder.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H3(id='output-text', children=''),

    html.Hr(),

    dcc.Dropdown(
        id='my-dropdown-widget',
        value=df.country[0],
        options=[
            {'label': i, 'value': i} for i in
            df.country.unique()
        ]
    )

])

@app.callback(
    Output(component_id='output-text', component_property='children'),
    [Input(component_id='my-dropdown-widget', component_property='value')])
def update_text(selected_value):
    return 'Average GDP per Capita of {} since {} is ${}'.format(
        selected_value,
        df.year.min(),
        round(df[df.country == selected_value].gdpPercap.mean(), 2)
    )


if __name__ == '__main__':
    app.run_server(debug=True, port=8055)