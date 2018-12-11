import dash
import dash_html_components as html
import pandas as pd

# This is now a really cool template to create heatmaps. 
# 


app = dash.Dash(__name__)
file = '/Users/Agah/Desktop/DashAndDonuts/dash-workshop/school_earnings.csv'


COLORS = [
    {
        'background': '#f1eef6',
        'text': 'rgb(30, 30, 30)'
    },
    {
        'background': '#bdc9e1',
        'text': 'rgb(30, 30, 30)'
    },
    {
        'background': '#74a9cf',
        'text': 'rgb(30, 30, 30)'
    },
    {
        'background': '#0570b0',
        'text': 'white'
    },
]

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def cell_style(value, min_value, max_value):
    style = {}
    if is_numeric(value):
        relative_value = (value - min_value) / (max_value - min_value)
        if relative_value <= 0.25:
            style = {
                'backgroundColor': COLORS[0]['background'],
                'color': COLORS[0]['text']
            }
        elif relative_value <= 0.5:
            style = {
                'backgroundColor': COLORS[1]['background'],
                'color': COLORS[1]['text']
            }
        elif relative_value <= 0.75:
            style = {
                'backgroundColor': COLORS[2]['background'],
                'color': COLORS[2]['text']
            }
        elif relative_value <= 1:
            style = {
                'backgroundColor': COLORS[3]['background'],
                'color': COLORS[3]['text']
            }
    return style

def getTable(filename,max_rows):
    
    df = pd.read_csv(filename)
    hdr = []
    for col in df.columns:
        hdr.append(html.Th(col))
    hdr = html.Tr(hdr)     

    rows = []

    for ii in range(min(len(df),max_rows)):
        max_value = df.max(numeric_only=True).max()
        min_value = df.min(numeric_only=True).max()
        row = []
        for col in df.columns:
            val = df.iloc[ii][col]
            if is_numeric(val):
                style = cell_style(val, min_value, max_value)
                row.append(html.Td(round(val, 2), style=style))
            else:
                row.append(html.Td(df.iloc[ii][col]))
        rows.append(html.Tr(row))

    return html.Table([
        html.Thead(hdr),
        html.Tbody(rows)
    ])   

app.layout = html.Div(children=[
    html.H4(children='University Wage Gap'),
    getTable(file,10)
])




if __name__ == '__main__':
    app.run_server(debug=True)