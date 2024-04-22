import dash
from dash import dcc, html, callback_context
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Read the formatted sales data
df = pd.read_csv("formatted_sales_data.csv")

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Sort by date
df = df.sort_values(by='date')

# Get unique regions
regions = df['region'].unique()

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualizer", style={'textAlign': 'center'}),
    
    dcc.RadioItems(
        id='region-filter',
        options=[
            {'label': region, 'value': region} for region in ['All'] + list(regions)
        ],
        value='All',
        labelStyle={'display': 'inline-block', 'margin-right': '20px'}
    ),
    
    dcc.Graph(id='sales-chart'),
    html.H3("The question is : Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?"),
    html.H3("The answer is : Sales were higher after the Pink Morsel price increase on the 15th of January, 2021"),
])

# Define callback to update the chart based on selected region
@app.callback(
    Output('sales-chart', 'figure'),
    [Input('region-filter', 'value')]
)
def update_chart(selected_region):
    if selected_region == 'All':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
    
    fig = px.line(filtered_df, x='date', y='sales', color='region', title='Pink Morsel Sales Over Time')
    return fig

# Run the app
# app.css.append_css({"external_url": "styles.css"})
if __name__ == '__main__':
    app.run_server(debug=True)

