# layout.py

import dash_bootstrap_components as dbc
from dash import dcc, html

def create_layout():
    # Navbar component
    navbar = dbc.NavbarSimple(
        brand="World Happiness Report Dashboard",
        brand_href="#",
        color="primary",
        dark=True,
        sticky="top",
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.NavItem(dbc.NavLink("Page 2", href="/page-2")),
            dbc.NavItem(dbc.NavLink("About", href="/about")),
            # Add more NavItems for additional options
        ]
    )
    
    layout = dbc.Container([
        navbar,
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
