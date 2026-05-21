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
gdf = gpd.read_file("D:\Python Training\Dashbord\MCH\MCHdash\Data\Shapes/Addis.shp")
numeric_cols = df["Sub city"]
colors = [
    "#4F46E5",   # Indigo
    "#06B6D4",   # Cyan
    "#10B981",   # Green
    "#F59E0B",   # Amber
    "#EF4444"    # Red
]
# ----------------------------- 
# App
# ----------------------------- 
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
           meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]           
           )
#print(gdf["Sub_City"])
#print(df["Sub city"])

merged = gdf.merge(
    df,
    left_on="Sub_City",   # shapefile column
    right_on="Sub city",
    how="left"
)

gdf = gdf.to_crs(epsg=4326)

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
                html.H5("Addis Ababa City MCH Dashboard", className="text-center mb-1 text-primary"),
                html.H6('የአዲስ እበባ ከተማ የእናቶች እና ህፃናት መረጃ ጥንቅር',className="text-center m-2 text-secondary"),
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
                        {"label": "First Antenatal care", "value": "anc1"},
                        {"label": "Second Antenatal care", "value": "anc2"},
                        {"label": "Total Antenatal car ", "value": "anc"},
                        {"label": "Total delivery", "value": "delivery"},
                        {"label": "Breech delivery", "value": "BCG"},
                        {"label": "Spontaneous Vaginal Delivery", "value": "SVD"},
                        {"label": "Still birth n (Per 1000 births)", "value": "SB"},
                        {"label": "Neonatal death (Per 1000 live births)", "value": "ND"},
                        {"label": "Maternal death (Per 100,000 births)", "value": "MD"}                      
                        
                    ],value='anc',
                    clearable=False,className="p-1"
                     ),
               ],width={'size':5,'offset':1}),
                dbc.Col ([
                     dcc.Dropdown(
                    id="subcity-dropdown",
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
                dcc.Graph(id="Addis_map",figure={})
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
                                   
                                    html.H6("Antenatal car"),
                                    html.Hr(),
                                    html.H5(id="anc-card")
                                ],
                                ),
                            )
                        ],className="mb-3 text-center border-start border-success border-5 shadow"),
                        dbc.Row([
                            dbc.Card(
                                dbc.CardBody([
                                    html.H6("Neonatal death Per 1000 live births"),
                                    html.Hr(),
                                    html.H5(id="ND-cart")
                                ],
                                ),
                            )
                        ],className="mb-3 text-center border-start border-success border-5 shadow"),
                        dbc.Row([
                            dbc.Card(
                                dbc.CardBody([
                                    html.H6("Breech delivery"),
                                    html.Hr(),
                                    html.H5(id="BD-cart")
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
                                    html.H6("Spontaneous Vaginal Delivery"),
                                    html.Hr(),
                                    html.H5(id="SVD-cart")
                                ],
                                ),
                            )
                        ],className="mb-3 text-center border-start border-success border-5 shadow"),
                        dbc.Row([
                            dbc.Card(
                                dbc.CardBody([
                                    html.H6("Total delivery"),
                                    html.Hr(),
                                    html.H5(id="delivery-cart")
                                ],
                                ),
                            )
                        ],className="mb-3 text-center border-start border-success border-5 shadow"),
                        dbc.Row([
                           dbc.Card(
                                dbc.CardBody([
                                    html.H6("Still birth Per 1000 "),
                                    html.Hr(),
                                    html.H5(id="SB-cart")
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
                dcc.Graph(id="Bar_graphe", figure= {})
            ],xs=12, sm=12, md=12, lg=5, xl=5),
             
            dbc.Col([
                html.P("pie chart",className="text-center" ),
               dcc.Graph(id="Pie_graphe",figure= {})
            ],xs=12, sm=12, md=12, lg=5, xl=5),
    ], justify="around",className="mt-4 mb-4"),
    # for line graphe
    dbc.Row([
        dcc.Graph(id="line_chart",animate=True)
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
    Output("Addis_map","figure"),
    Input("health_value", "value")
)
def update_charts(value):

    sorted_df = df.sort_values(by=value, ascending=False)

    # BAR CHART
    bar_fig = px.bar(
        sorted_df,
        x="Sub city",
        y=value,
        height=500,
        template="plotly_white",   
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
        template="plotly_white", 
        title=f"{value} Trend by Sub city",
        markers=True
        
    )
    # Make line attractive
    line_fig.update_traces(
    line=dict(
        width=5,
        shape="spline"   # smooth curve
    ),

    marker=dict(
        size=12,
        line=dict(width=2, color="white")
    ),
    hovertemplate= "<b>%{x}</b><br>" +
    f"{value}: "+"%{y}<extra></extra>"
    )
    line_fig.update_layout(

    height=500,

    title={
        "x": 0.5,
        "xanchor": "center",
        "font": {
            "size": 24
        }
    },

    xaxis_title="Sub City",
    yaxis_title=value,

    hovermode="x unified",

    paper_bgcolor="white",
    plot_bgcolor="white",

    font=dict(
        family="Arial",
        size=14
    ),

    margin=dict(
        t=80,
        l=40,
        r=40,
        b=40
    ),

    transition={
        "duration": 1200,
        "easing": "cubic-in-out"
    }
    )
    
    
    # display map 
    fig_map = px.choropleth_mapbox(
    merged,
    geojson=gdf.__geo_interface__,
    locations=merged.index,
    color=value,
    mapbox_style="carto-positron",
    #mapbox_style="open-street-map",
    center={"lat": 8.96, "lon": 38.80},
    zoom=10.0,
    opacity=0.7,
     hover_name="Sub city",
     color_continuous_scale=px.colors.sequential.Peach_r,
     # title=f"Addis Ababa MCH "
    )
    fig_map.update_layout(margin={"r":6,"t":6,"l":6,"b":6})

    return bar_fig, pie_fig,line_fig,fig_map
@app.callback(
      Output("anc-card", "children"),
      Output("ND-cart", "children"),
      Output("BD-cart", "children"),
      Output("SVD-cart", "children"),
      Output("delivery-cart", "children"),
      Output("SB-cart", "children"),

      Input("subcity-dropdown", "value")
      )

def update_Data(subcity):
    Tanc = df[df["Sub city"]==subcity]
    anc=Tanc["anc"].iloc[0]
    nd=Tanc["ND"].iloc[0]
    Bd=Tanc["BCG"].iloc[0]
    svd=Tanc["SVD"].iloc[0]
    TDs=Tanc["delivery"].iloc[0]
    TDs=Tanc["delivery"].iloc[0]
    SBs=Tanc["SB"].iloc[0]

    
    return anc,nd,Bd,svd,TDs,SBs
if __name__ == "__main__":
    app.run(debug=True)