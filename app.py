import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from data import load_happiness_data
from layout import create_layout
from callbacks import register_callbacks

# Load data
happiness_data = load_happiness_data()

# Create Dash app
app = dash.Dash(__name__)

# Set layout
app.layout = create_layout()

# Register callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
