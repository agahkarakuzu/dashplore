
# https://dash-workshop.plot.ly/
# You can create assests folder and place some css files in it. 

import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__)

app.layout = html.Div([ # One html div here 

	html.H1('Dash and donuts'), # More formatting can go here. This is H1 
  	
  	# dcc is core components. Where interactive widgets live. 

	dcc.Dropdown(options=[
					{'label':i,'value':i}
					for i in ['Montreal','NYC']
	],
	multi = True,
	value = ['NYC']),

	# You can use plotly chart generator to make it easier 

	# They are working on a jupyter lab integration. 
	# You can render text as markdown as well. 
	# The full set of components is of course available @ docs. 
	# See more at dash core components. 

	dcc.Graph(figure={'data':[{
			    'x':[1,2,3],
			    'y':[3,2,1],
			    'type':'bar'	
				},
				{
			    'x':[1,2,3],
			    'y':[3,2,1],
			    'type':'line'	
				},
		]})
	])

if __name__ == '__main__':
	app.run_server(debug=True)
