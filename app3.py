# Dash callbacks !!!

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt

app = dash.Dash(__name__)

app.layout = html.Div([

    # dash_html_components's common properties include
    # `children` and `style`.
    html.H3(
        children='Declarative Components',
        style={
            'borderBottom': 'thin grey solid'
        }
    ),

    # Dropdown has properties `options`, `value`, and others
    dcc.Dropdown(
        options=[
            {'label': 'New York', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'Los Angeles', 'value': 'LA'}
        ],
        value='MTL'
    ),

    # The main property of Graph is `figure`
    dcc.Graph(
        id='my-graph',
        figure={
            'data': [{
                'x': [1, 2, 3],
                'y': [3, 1, 2],
                'type': 'bar'
            }],
            'layout': {
                'margin': {
                    'l': 30, 'r': 10, 'b': 30, 't': 20
                }
            }
        }
    )

])


if __name__ == '__main__':
    app.run_server(debug=True)
