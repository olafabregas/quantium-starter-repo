import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load the formatted sales data
df = pd.read_csv("formatted_sales_data.csv")
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

regions = ['all', 'north', 'east', 'south', 'west']

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualiser", style={
        'textAlign': 'center',
        'color': '#e75480',
        'fontFamily': 'Arial Black',
        'marginBottom': '30px'
    }),
    html.Div([
        html.Label("Select Region:", style={'fontWeight': 'bold', 'fontSize': '18px'}),
        dcc.RadioItems(
            id='region-radio',
            options=[{'label': r.capitalize(), 'value': r} for r in regions],
            value='all',
            inline=True,
            style={'margin': '10px 0'}
        ),
    ], style={'textAlign': 'center', 'marginBottom': '20px'}),
    html.Div([
        dcc.Graph(id='sales-line-chart')
    ], style={'backgroundColor': "#26269c", 'padding': '20px', 'borderRadius': '10px', 'boxShadow': '0 2px 8px #e7548033'})
], style={'maxWidth': '800px', 'margin': 'auto', 'padding': '40px', 'backgroundColor': '#fffbe7', 'borderRadius': '15px', 'boxShadow': '0 4px 16px #e7548044'})

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-radio', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered = df
        title = "Total Daily Sales of Pink Morsels (All Regions)"
    else:
        filtered = df[df['region'] == selected_region]
        title = f"Total Daily Sales of Pink Morsels ({selected_region.capitalize()})"
    daily_sales = filtered.groupby('date')['sales'].sum().reset_index()
    fig = px.line(
        daily_sales,
        x='date',
        y='sales',
        title=title,
        labels={'date': 'Date', 'sales': 'Sales ($)'}
    )
    fig.update_layout(
        plot_bgcolor='#fffbe7',
        paper_bgcolor='#fffbe7',
        font_family='Arial',
        font_color='#222',
        title_font_color='#e75480',
        title_font_size=22
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)