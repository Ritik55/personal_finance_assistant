import plotly.graph_objs as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd

class FinanceDashboard:
    def __init__(self):
        self.app = dash.Dash(__name__)
        self.app.layout = html.Div([
            html.H1("Personal Finance Dashboard"),
            dcc.Graph(id='spending-chart'),
            dcc.Graph(id='savings-chart')
        ])

        @self.app.callback(
            Output('spending-chart', 'figure'),
            Input('spending-chart', 'id')
        )
        def update_spending_chart(_):
            return self.create_spending_chart()

        @self.app.callback(
            Output('savings-chart', 'figure'),
            Input('savings-chart', 'id')
        )
        def update_savings_chart(_):
            return self.create_savings_chart()

    def create_spending_chart(self):
        categories = ['Food', 'Rent', 'Utilities', 'Entertainment', 'Transport']
        amounts = [300, 1000, 200, 150, 250]

        fig = go.Figure(data=[go.Bar(x=categories, y=amounts)])
        fig.update_layout(title='Monthly Spending by Category', xaxis_title='Category', yaxis_title='Amount ($)')
        return fig

    def create_savings_chart(self):
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        savings = [500, 600, 550, 700, 800, 900]

        fig = go.Figure(data=[go.Scatter(x=months, y=savings, mode='lines+markers')])
        fig.update_layout(title='Monthly Savings Trend', xaxis_title='Month', yaxis_title='Savings ($)')
        return fig

    def run(self):
        self.app.run_server(debug=True)
