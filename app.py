import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Read the formatted sales data
df = pd.read_csv("formatted_sales_data.csv")

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Sort by date
df = df.sort_values(by='date')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualizer created by Mehmet Hilmi Emel"),
    
    dcc.Graph(
        id='sales-chart',
        figure=px.line(df, x='date', y='sales', color='region', title='Pink Morsel Sales Over Time')
    ),
    html.H3("The question is : Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?"),
    html.H3("The answer is : Sales were higher after the Pink Morsel price increase on the 15th of January, 2021"),
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
