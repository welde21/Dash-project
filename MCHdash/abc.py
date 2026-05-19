import dash
from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =====================================================
# SAMPLE DATA
# =====================================================

# Replace this with your real EMR/MCH dataset

df = pd.DataFrame({
    "Sub city": ["Bole", "Yeka", "Arada", "Lideta", "Kirkos"],
    "ANC": [12000, 15000, 9000, 11000, 13000],
    "Delivery": [5000, 6500, 4000, 4800, 5200],
    "BCG": [10000, 12000, 8500, 9300, 11000],
    "SVD": [3000, 4200, 2800, 3500, 3900]
})

# =====================================================
# DASH APP
# =====================================================

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.title = "Healthcare Dashboard"

# =====================================================
# KPI CARDS
# =====================================================


def create_card(title, value, color):

    return dbc.Card([

        dbc.CardBody([

            html.H6(
                title,
                className="text-muted"
            ),

            html.H2(
                f"{value:,}",
                className="fw-bold"
            )

        ])

    ],
    className=f"shadow-sm border-0 rounded-4 border-start border-5 border-{color}")


kpi_cards = dbc.Row([

    dbc.Col(
        create_card("Total ANC", df["ANC"].sum(), "primary"),
        xs=12, sm=6, md=3,
        className="mb-3"
    ),

    dbc.Col(
        create_card("Total Delivery", df["Delivery"].sum(), "success"),
        xs=12, sm=6, md=3,
        className="mb-3"
    ),

    dbc.Col(
        create_card("Total BCG", df["BCG"].sum(), "warning"),
        xs=12, sm=6, md=3,
        className="mb-3"
    ),

    dbc.Col(
        create_card("Total SVD", df["SVD"].sum(), "danger"),
        xs=12, sm=6, md=3,
        className="mb-3"
    )

])

# =====================================================
# FILTERS
# =====================================================

filters = dbc.Row([

    dbc.Col([

        html.Label("Select Indicator"),

        dcc.Dropdown(
            id="indicator-dropdown",
            options=[
                {"label": "ANC", "value": "ANC"},
                {"label": "Delivery", "value": "Delivery"},
                {"label": "BCG", "value": "BCG"},
                {"label": "SVD", "value": "SVD"},
            ],
            value="ANC",
            clearable=False
        )

    ], md=4)

], className="mb-4")

# =====================================================
# BAR GRAPH
# =====================================================


def create_bar_chart(value):

    sorted_df = df.sort_values(by=value, ascending=False)

    colors = [
        "#2563EB",
        "#10B981",
        "#F59E0B",
        "#EF4444",
        "#8B5CF6"
    ]

    fig = px.bar(
        sorted_df,
        x="Sub city",
        y=value,
        text=value,
        color="Sub city",
        color_discrete_sequence=colors,
        template="plotly_white"
    )

    fig.update_traces(

        texttemplate='%{y:,}',
        textposition='outside',

        hovertemplate=
        "<b>%{x}</b><br>" +
        f"{value}: " + "%{y:,}<extra></extra>"
    )

    fig.update_layout(

        title={
            "text": f"{value} by Sub City",
            "x": 0.5,
            "xanchor": "center"
        },

        height=500,

        paper_bgcolor="#f8f9fa",
        plot_bgcolor="#f8f9fa",

        showlegend=False,

        font=dict(
            family="Arial",
            size=14
        ),

        margin=dict(
            t=70,
            l=30,
            r=30,
            b=30
        ),

        hovermode="x unified",

        transition={
            "duration": 1200,
            "easing": "cubic-in-out"
        }
    )

    return fig

# =====================================================
# LINE GRAPH
# =====================================================


def create_line_chart(value):

    sorted_df = df.sort_values(by=value)

    fig = px.line(
        sorted_df,
        x="Sub city",
        y=value,
        markers=True,
        template="plotly_white"
    )

    fig.update_traces(

        line=dict(
            width=5,
            shape='spline'
        ),

        marker=dict(
            size=12,
            line=dict(width=2, color='white')
        ),

        hovertemplate=
        "<b>%{x}</b><br>" +
        f"{value}: " + "%{y:,}<extra></extra>",

        fill='tozeroy'
    )

    fig.update_layout(

        title={
            "text": f"{value} Trend",
            "x": 0.5
        },

        height=500,

        paper_bgcolor="#f8f9fa",
        plot_bgcolor="#f8f9fa",

        hovermode="x unified",

        transition={
            "duration": 1200
        }
    )

    return fig

# =====================================================
# LAYOUT
# =====================================================

app.layout = dbc.Container([

    # HEADER
    dbc.Row([

        dbc.Col([

            html.H2(
                "Healthcare Dashboard",
                className="fw-bold"
            ),

            html.P(
                "Maternal and Child Health Analytics",
                className="text-muted"
            )

        ])

    ], className="mt-4 mb-4"),

    # KPI CARDS
    kpi_cards,

    html.Br(),

    # FILTERS
    filters,

    # GRAPHS
    dbc.Row([

        dbc.Col([

            dbc.Card([

                dbc.CardBody([

                    dcc.Graph(
                        id="bar-chart",
                        animate=True,
                        config={
                            "displayModeBar": False
                        }
                    )

                ])

            ], className="shadow-sm border-0 rounded-4")

        ], md=6),

        dbc.Col([

            dbc.Card([

                dbc.CardBody([

                    dcc.Graph(
                        id="line-chart",
                        animate=True,
                        config={
                            "displayModeBar": False
                        }
                    )

                ])

            ], className="shadow-sm border-0 rounded-4")

        ], md=6)

    ])

],
fluid=True,
style={
    "backgroundColor": "#f4f6f9",
    "padding": "20px"
})

# =====================================================
# CALLBACK
# =====================================================

@callback(
    Output("bar-chart", "figure"),
    Output("line-chart", "figure"),
    Input("indicator-dropdown", "value")
)
def update_graphs(value):

    return (
        create_bar_chart(value),
        create_line_chart(value)
    )

# =====================================================
# RUN SERVER
# =====================================================

if __name__ == "__main__":
    app.run(debug=True)

