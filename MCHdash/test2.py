import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import geopandas as gpd

# --------------------------------
# LOAD DATA
# --------------------------------
df = pd.read_csv("Data/Health.csv")

# READ SHAPEFILE
gdf = gpd.read_file(
    r"D:\Python Training\Dashbord\MCH\MCHdash\Data\Shapes/Addis.shp"
)

# Convert CRS
gdf = gdf.to_crs(epsg=4326)

# Merge shape and dataframe
merged = gdf.merge(
    df,
    left_on="Sub_City",
    right_on="Sub city",
    how="left"
)

# Dropdown values
subcities = df["Sub city"]

# --------------------------------
# DASH APP
# --------------------------------
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1.0"
        }
    ]
)

# --------------------------------
# APP LAYOUT
# --------------------------------
app.layout = dbc.Container([

    # ======================================
    # FIXED HEADER
    # ======================================
    dbc.Row([

        dbc.Col([
            html.H5(
                "LOGO",
                className="text-center fw-bold text-primary"
            )
        ], width=2),

        dbc.Col([
            html.H4(
                "Addis Ababa City MCH Dashboard",
                className="text-center text-primary fw-bold mb-1"
            ),

            html.H6(
                "የአዲስ እበባ ከተማ የእናቶች እና ህፃናት መረጃ ጥንቅር",
                className="text-center text-secondary"
            )
        ], width=8),

        dbc.Col([
            html.H5(
                "LOGO",
                className="text-center fw-bold text-primary"
            )
        ], width=2)

    ],
        style={
            "backgroundColor": "white",
            "position": "fixed",
            "top": "0",
            "left": "0",
            "right": "0",
            "width": "100%",
            "zIndex": "999",
            "padding": "15px",
            "boxShadow": "0px 2px 10px rgba(0,0,0,0.15)"
        },
        className="shadow"
    ),

    # ======================================
    # DROPDOWNS
    # ======================================
    dbc.Row([

        dbc.Col([

            dcc.Dropdown(
                id="health_value",

                options=[
                    {"label": "First Antenatal Care", "value": "anc1"},
                    {"label": "Second Antenatal Care", "value": "anc2"},
                    {"label": "Total Antenatal Care", "value": "anc"},
                    {"label": "Total Delivery", "value": "delivery"},
                    {"label": "Breech Delivery", "value": "BCG"},
                    {"label": "Spontaneous Vaginal Delivery", "value": "SVD"},
                    {"label": "Still Birth", "value": "SB"},
                    {"label": "Neonatal Death", "value": "ND"},
                    {"label": "Maternal Death", "value": "MD"},
                ],

                value="anc",
                clearable=False,
                className="shadow"

            )

        ], width=5),

        dbc.Col([

            dcc.Dropdown(
                id="subcity-dropdown",

                options=[
                    {
                        "label": i,
                        "value": i
                    }
                    for i in subcities
                ],

                value=subcities.iloc[0],
                clearable=False,
                className="shadow"
            )

        ], width=5)

    ],
        justify="around",
        className="mb-4"
    ),

    # ======================================
    # MAP + CARDS
    # ======================================
    dbc.Row([

        # MAP
        dbc.Col([

            dbc.Card([

                dbc.CardHeader(
                    html.H5(
                        "Addis Ababa MCH Map",
                        className="text-center"
                    )
                ),

                dbc.CardBody([

                    dcc.Graph(
                        id="Addis_map",
                        figure={}
                    )

                ])

            ], className="shadow")

        ], lg=5),

        # CARDS
        dbc.Col([

            dbc.Row([

                dbc.Col([

                    dbc.Card([

                        dbc.CardBody([

                            html.H6(
                                "Antenatal Care",
                                className="text-center"
                            ),

                            html.Hr(),

                            html.H3(
                                id="anc-card",
                                className="text-center text-primary"
                            )

                        ])

                    ],
                        className="shadow border-start border-5 border-success mb-3"
                    ),

                    dbc.Card([

                        dbc.CardBody([

                            html.H6(
                                "Neonatal Death",
                                className="text-center"
                            ),

                            html.Hr(),

                            html.H3(
                                id="ND-cart",
                                className="text-center text-danger"
                            )

                        ])

                    ],
                        className="shadow border-start border-5 border-danger"
                    )

                ], lg=6),

                dbc.Col([

                    dbc.Card([

                        dbc.CardBody([

                            html.H6(
                                "Delivery",
                                className="text-center"
                            ),

                            html.Hr(),

                            html.H3(
                                id="delivery-cart",
                                className="text-center text-success"
                            )

                        ])

                    ],
                        className="shadow border-start border-5 border-primary mb-3"
                    ),

                    dbc.Card([

                        dbc.CardBody([

                            html.H6(
                                "Still Birth",
                                className="text-center"
                            ),

                            html.Hr(),

                            html.H3(
                                id="SB-cart",
                                className="text-center text-warning"
                            )

                        ])

                    ],
                        className="shadow border-start border-5 border-warning"
                    )

                ], lg=6)

            ])

        ], lg=5)

    ],
        justify="around",
        className="mb-4"
    ),

    # ======================================
    # CHARTS
    # ======================================
    dbc.Row([

        dbc.Col([

            dbc.Card([

                dbc.CardBody([

                    dcc.Graph(
                        id="Bar_graphe"
                    )

                ])

            ], className="shadow")

        ], lg=5),

        dbc.Col([

            dbc.Card([

                dbc.CardBody([

                    dcc.Graph(
                        id="Pie_graphe"
                    )

                ])

            ], className="shadow")

        ], lg=5)

    ],
        justify="around",
        className="mb-4"
    ),

    # ======================================
    # LINE GRAPH
    # ======================================
    dbc.Row([

        dbc.Col([

            dbc.Card([

                dbc.CardBody([

                    dcc.Graph(
                        id="line_chart"
                    )

                ])

            ], className="shadow")

        ])

    ]),

    # ======================================
    # FOOTER
    # ======================================
    dbc.Row([

        dbc.Col([

            html.H6("MCH Dashboard"),

            html.P("Copyright © 2026"),

            html.P("All Rights Reserved")

        ], lg=6),

        dbc.Col([

            html.H6("Contact"),

            html.P("Email: example@gmail.com"),

            html.P("Phone: +251 900000000")

        ], lg=6)

    ],
        style={
            "marginTop": "30px",
            "backgroundColor": "#5570c8",
            "color": "white",
            "padding": "20px"
        }
    )

],
    fluid=True,

    style={
        "backgroundColor": "#f6f6f6",
        "paddingTop": "120px"
    }
)

# ======================================
# CHART CALLBACK
# ======================================
@callback(
    Output("Bar_graphe", "figure"),
    Output("Pie_graphe", "figure"),
    Output("line_chart", "figure"),
    Output("Addis_map", "figure"),

    Input("health_value", "value")
)
def update_chart(value):

    sorted_df = df.sort_values(
        by=value,
        ascending=False
    )

    # BAR CHART
    bar_fig = px.bar(
        sorted_df,
        x="Sub city",
        y=value,
        color="Sub city",
        template="plotly_white",
        title=f"{value} by Sub City"
    )

    # PIE CHART
    pie_fig = px.pie(
        sorted_df,
        names="Sub city",
        values=value,
        hole=0.5,
        title=f"{value} Distribution"
    )

    # LINE CHART
    line_fig = px.line(
        sorted_df,
        x="Sub city",
        y=value,
        markers=True,
        template="plotly_white",
        title=f"{value} Trend"
    )

    line_fig.update_traces(
        line=dict(width=4),
        marker=dict(size=10)
    )

    # MAP
    fig_map = px.choropleth_mapbox(
        merged,
        geojson=gdf.__geo_interface__,
        locations=merged.index,
        color=value,
        mapbox_style="carto-positron",
        center={"lat": 8.96, "lon": 38.80},
        zoom=10,
        opacity=0.7,
        hover_name="Sub city",
        color_continuous_scale=px.colors.sequential.Peach
    )

    # BLACK BORDERS
    fig_map.update_traces(
        marker_line_color="black",
        marker_line_width=2
    )

    fig_map.update_layout(
        margin={
            "r": 0,
            "t": 0,
            "l": 0,
            "b": 0
        }
    )

    return (
        bar_fig,
        pie_fig,
        line_fig,
        fig_map
    )

# ======================================
# CARD CALLBACK
# ======================================
@callback(
    Output("anc-card", "children"),
    Output("ND-cart", "children"),
    Output("delivery-cart", "children"),
    Output("SB-cart", "children"),

    Input("subcity-dropdown", "value")
)
def update_cards(subcity):

    temp = df[df["Sub city"] == subcity]

    anc = temp["anc"].iloc[0]
    nd = temp["ND"].iloc[0]
    delivery = temp["delivery"].iloc[0]
    sb = temp["SB"].iloc[0]

    return anc, nd, delivery, sb

# ======================================
# RUN APP
# ======================================
if __name__ == "__main__":
    app.run(debug=True)