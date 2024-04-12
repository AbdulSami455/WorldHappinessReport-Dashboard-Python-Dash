from dash import dcc, html

def create_layout():
    return html.Div([
        html.H1("World Happiness Report Dashboard"),
        dcc.Dropdown(
            id='column-dropdown',
            options=[
                {'label': 'Happiness Score', 'value': 'Ladder score'},
                {'label': 'Standard error of ladder score', 'value': 'Standard error of ladder score'},
                # Add more options for other columns
            ],
            value='Ladder score'
        ),
        dcc.Graph(id='happiness-bar-chart'),
    ])
