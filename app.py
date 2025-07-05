import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the formatted sales data
df = pd.read_csv("formatted_sales_data.csv")

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Sort by date
df = df.sort_values('date')

# Aggregate sales by date
daily_sales = df.groupby('date')['sales'].sum().reset_index()

# Create the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualiser"),
    dcc.Graph(
        id='sales-line-chart',
        figure=px.line(
            daily_sales,
            x='date',
            y='sales',
            title="Total Daily Sales of Pink Morsels",
            labels={'date': 'Date', 'sales': 'Sales ($)'}
        )
    )
])

if __name__ == '__main__':
    app.run(debug=True)