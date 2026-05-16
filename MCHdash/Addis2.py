# ============================================
# SUPER SIMPLE DASHBOARD FOR BEGINNERS
# Addis Ababa MCH Data Dashboard
# ============================================

# Step 1: Import what we need
import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np

# Step 2: Create fake data (replace this with your real data later)
Hdata = pd.read_csv('Data/Health.csv')
def create_sample_data():
    Hdata = pd.read_csv('Data/Health.csv')
    return Hdata

# Step 3: Create the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Step 4: Design the layout (what the user sees)
app.layout = dbc.Container([
    
   # === HEADER ===
# === HEADER WITH LOGO ===
dbc.Row([
    # Left side - Logo
    dbc.Col([
        html.Img(
            src='/assets/Ethiopia.jpg',  # Your logo file path
            style={
                'height': '80px',
                'width': '80px',
               # 'borderRadius': '50%'  # Makes it circular (optional)
            }
        )
    ], width=2, style={'textAlign': 'center'}),  # Logo takes 2 columns
    
    # Right side - Titles
    dbc.Col([
        html.H1("Addis Ababa MCH Dashboard", 
                style={
                    'textAlign': 'center', 
                    'color': 'black', 
                    'padding': '5px',
                    'margin': '0',
                    'fontSize': '28px'
                }),
        
        html.H3("የአዲስ አበባ የሕፃናት እና የእናቶች ጤና ዳሽቦርድ", 
                style={
                    'textAlign': 'center', 
                    'color': 'black', 
                    'padding': '5px',
                    'margin': '0',
                    'fontSize': '20px'
                }),
    ], width=10),  # Titles take 10 columns
    
], style={
    'backgroundColor': "#ffffff",
    #'borderRadius': '10px',
    'marginBottom': '20px',
    #'padding': '15px',
    'boxShadow': '0 4px 8px rgba(0,0,0,0.2)',
    'alignItems': 'center'  # Centers items vertically
}),
    # === FILTERS ===
    dbc.Row([
        dbc.Col([
            html.Label("select sub-city:"),
            dcc.Dropdown(
                id='subcity-dropdown',
                options=Hdata['Sub city'].unique(),
                value='Gullel'  # Default value
            ),
        ], width=3),
        
    ], className="mb-4"),
    
    # === GRAPHS ===
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='line-chart')  # First graph (line chart)
        ], width=4),
        
        dbc.Col([
            # left side with 6 cards (2 rows of 3 cards each)
dbc.Col([
    # Row 1 (3 cards with graphs)
    dbc.Row([
        # Card 1 - Deliveries Trend
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6("Total Deliveries", className="text-primary text-center"),
                    html.H3("1,234", className="text-center text-primary"),
                    dcc.Graph(
                        id='graph-deliveries',
                        figure=px.bar(x=Hdata['Sub city'].unique(), y=Hdata['delivery']),
                        config={'displayModeBar': False},
                        style={'height': '120px'}
                    )
                ])
            ], style={'boxShadow': '0 2px 4px rgba(0,0,0,0.1)', 'borderRadius': '8px'})
        ], width=4),
        
        # Card 2 - ANC Visits Trend
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6("ANC Visits", className="text-success text-center"),
                   # html.H3("567", className="text-center text-success"),
                    dcc.Graph(
                        id='graph-anc',
                        figure=px.bar(x=Hdata['Sub city'].unique(), y=Hdata['anc']),
                        style={'height': '120px'}
                    )
                ])
            ], style={'boxShadow': '0 2px 4px rgba(0,0,0,0.1)', 'borderRadius': '8px'})
        ], width=4),
        
       ], className="mb-3"),
    
]),
        ]),
    ]),
   
    
], fluid=True,
 style={
    'padding': '10px',
    'backgroundColor': '#f8f9fa',
    'fontFamily': 'Arial, sans-serif'})

# Step 5: Add interactivity (make dropdowns work)
   

# Step 6: Run the app
if __name__ == '__main__':
    app.run(debug=True)