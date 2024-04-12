from dash.dependencies import Output, Input
import plotly.express as px

def register_callbacks(app):
    @app.callback(
        Output('happiness-bar-chart', 'figure'),
        [Input('column-dropdown', 'value')]
    )
    def update_graph(selected_column):
        fig = px.bar(happiness_data, x='Country name', y=selected_column, 
                     title=f'{selected_column} by Country',
                     labels={'Country name': 'Country', selected_column: selected_column})
        return fig
