

import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='simple-dropdown-element',
        options=[
            {'label': 'Montreal', 'value': 'Montreal'},
            {'label': 'New York City', 'value': 'New York City'},
            {'label': 'Cincinnati', 'value': 'Cincinnati'},
        ],
        value='Montreal'
    ),
    html.Div(children='', id='simple-output-element')
])

# What are the inputs and outputs are defined in this decorator
# Our functions are gonna get these vals and pass automatically 
# Speficiy the id of the component and its property 

# We will update childeren property of simple-output-element
# Based on the input listened from simple-dropdown-element (value property)
@app.callback(
    Output(component_id='simple-output-element', component_property='children'),
    [Input(component_id='simple-dropdown-element', component_property='value')])
# These functions can habve any name, as well as the arguments
def display_value(dropdown_value):
    return 'You have selected "{}"'.format(dropdown_value)


if __name__ == '__main__':
    app.run_server(debug=True, port=8054)