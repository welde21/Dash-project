import pandas as pd
import plotly.express as px 
from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc 
import geopandas as gpd
# -----------------------------
# Load Data 
# -----------------------------
df = pd.read_csv("Data/Health.csv") 
# read shapefile 
gdf = gpd.read_file("Data/shape/new_boundary/AA_SUB_CITY_BOUNDARY_08_MARCH_2023.shp")
numeric_cols = df.select_dtypes(include="number").columns
# ----------------------------- 
# App
# ----------------------------- 
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
           meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]           
           )
gdf = gdf.to_crs(epsg=4326)

fig = px.choropleth_mapbox(
    gdf,
    geojson=gdf.__geo_interface__,
    locations=gdf.index,
    mapbox_style="carto-positron",
    center={"lat": 9.03, "lon": 38.74},
    zoom=10,
    opacity=0.5
)
# -----------------------------
# App Layout
# -----------------------------
app.layout = dbc.Container([
  
        #header
    dbc.Row([
        dbc.Col([
        html.P(" image here",className="text-center" )                
        ]),
        dbc.Col([
            dbc.Row([
                html.H4("MCH Dashboard", className="text-center mb-4 text-primary"),
            ],style={"margin":10}),
            dbc.Row([
                 html.H4("የሀናቶች እና ህፃናት መረጃ ", className="text-center m-2 text-secondary" )
             ]),
         ]),
        dbc.Col([
        html.P(" image here",className="text-center" )                
        ]
        ),
    ],style={"backgroundColor": "#ffffff", "marginBottom": "10px"},className="shadow"
    
    ),
        #Drwopdown
           dbc.Row([
            dbc.Col([
           dcc.Dropdown(
                    id="health_value",
                    options=[
                        {"label": col.replace("_", " ").title(), "value": col}
                        for col in numeric_cols
                        
                    ],value=numeric_cols[0],
                    clearable=False,className="p-1"
                     ),
               ],width={'size':5,'offset':1}),
                dbc.Col ([
                     dcc.Dropdown(
                    id="health_value2",
                    options=[
                        {"label": col.replace("_", " ").title(), "value": col}
                        for col in numeric_cols
                        
                    ],value=numeric_cols[3],
                    clearable=False,className="p-1"
                    
                     ),
               ],width={'size':5}),
                
            ],justify="start",className="mt-4"),
                   
        # for mape and cart 
        dbc.Row([   
            dbc.Col([
                 html.P("map here",className="text-center" ) ,
                dcc.Graph(figure=fig)
            ],xs=12, sm=12, md=12, lg=5, xl=5),
             
             # cart her 
            dbc.Col([
                # cart 1
               dbc.Row([
                    dbc.Col([
                        html.P("cart here",className="text-center" ),
                        dbc.Row([
                            dbc.Card(
                                dbc.CardBody([
                                   
                                    html.H4("ANC"),
                                    html.Hr(),
                                    html.H5("230")
                                ],
                                ),
                            )
                        ],className="mb-3 text-center border-start border-success border-5 shadow"),
                        dbc.Row([
                            dbc.Card(
                                dbc.CardBody([
                                    html.H4("ANC"),
                                    html.Hr(),
                                    html.H5("230")
                                ],
                                ),
                            )
                        ],className="mb-3 text-center border-start border-success border-5 shadow"),
                        dbc.Row([
                            dbc.Card(
                                dbc.CardBody([
                                    html.H4("ANC"),
                                    html.Hr(),
                                    html.H5("230")
                                ],
                                ),
                            )
                        ],className="mb-3 text-center border-start border-success border-5 shadow"
                    ),
                         #dcc.Graph(id="cart1",figure= {})

                    ], className="m-3 gx-2"),
                    dbc.Col([
                        html.P("cart here 2",className="text-center" ),
                        dbc.Row([
                            dbc.Card(
                                dbc.CardBody([
                                    html.H4("ANC"),
                                    html.Hr(),
                                    html.H5("230")
                                ],
                                ),
                            )
                        ],className="mb-3 text-center border-start border-success border-5 shadow"),
                        dbc.Row([
                            dbc.Card(
                                dbc.CardBody([
                                    html.H4("ANC"),
                                    html.Hr(),
                                    html.H5("230")
                                ],
                                ),
                            )
                        ],className="mb-3 text-center border-start border-success border-5 shadow"),
                        dbc.Row([
                           dbc.Card(
                                dbc.CardBody([
                                    html.H4("ANC"),
                                    html.Hr(),
                                    html.H5("230")
                                ],
                                ),
                            )
                        ],className="mb-3 text-center border-start border-success border-5 shadow"),
                       # dcc.Graph(id="cart2",figure= {})

                    ],className="m-3 gx-2"),
               ]),
                
            ],xs=12, sm=12, md=12, lg=5, xl=5),

        ], justify="around",className="mt-4"),
    # for graphe
    dbc.Row([

         dbc.Col([
                 html.P("Bar chart",className="text-center" ) ,
                dcc.Graph(id="Bar_graphe",figure= {})
            ],xs=12, sm=12, md=12, lg=5, xl=5),
             
            dbc.Col([
                html.P("pie chart",className="text-center" ),
               dcc.Graph(id="Pie_graphe",figure= {})
            ],xs=12, sm=12, md=12, lg=5, xl=5),
    ], justify="around",className="mt-4 mb-4"),
    # for line graphe
    dbc.Row([
        dcc.Graph(id="line_chart",figure= {})
    ]),
    # footer 
    dbc.Row([
        dbc.Row([
            dbc.Col([
           html.P(" ",className="text-center" ),
           html.P("Copyright © 2024 MCH Dashboard.") ,
           html.P(" All rights reserved.", className="text-left" ) ,    
            ],xs=12, sm=12, md=12, lg=5, xl=5),
            dbc.Col([
                html.P("Contact : weldemariam Bahre", className="text-left" ),
                html.P("Email : weldemariambahre@gmaiol.com", className="text-left" ),
                html.P("Phone : +251 946674151", )

            ],xs=12, sm=12, md=12, lg=5, xl=5),
        ]),

               
    ], style={"marginTop": "20px",
    "backgroundColor": "#5570c8",
    "color": "white"}),
],fluid=True, style={"backgroundColor": "#f6f6f6"})

@callback(
    Output("Bar_graphe", "figure"),
    Output("Pie_graphe", "figure"),
    Output("line_chart", "figure"),
    Input("health_value", "value")
)
def update_charts(value):

    sorted_df = df.sort_values(by=value, ascending=False)

    # BAR CHART
    bar_fig = px.bar(
        sorted_df,
        x="Sub city",
        y=value,
        title=f"{value} by Sub city"
    )

    # PIE CHART
    pie_fig = px.pie(
        sorted_df,
        names="Sub city",
        values=value,
        title=f"{value} Distribution",
        hole=0.4
    )
    # line graphe 
    line_fig = px.line(
        sorted_df,
        x="Sub city",
        y=value,
        title=f"{value} Trend by Sub city",
        markers=True
    )

    return bar_fig, pie_fig,line_fig


if __name__ == "__main__":
    app.run(debug=True)