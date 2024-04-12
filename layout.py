# layout.py

import dash_bootstrap_components as dbc
from dash import dcc, html

def create_layout():
    layout = dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("World Happiness Report Dashboard", className="display-4"), width=12)
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='column-dropdown',
                    options=[
                        {'label': 'Happiness Score', 'value': 'Ladder score'},
                        {'label': 'Standard error of ladder score', 'value': 'Standard error of ladder score'},
                        # Add more options for other columns
                    ],
                    value='Ladder score',
                    className="mb-3"
                ),
                width=6, xs=12
            ),
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(id='happiness-bar-chart'),
                width=12
            )
        ])
    ], fluid=True, className="mt-4")
    
    return layout
