import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("output.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Create app
app = Dash(__name__)

app.layout = html.Div(
    style={"fontFamily": "Arial", "padding": "20px", "backgroundColor": "#f5f5f5"},
    children=[

        html.H1(
            "Pink Morsel Sales Dashboard",
            style={"textAlign": "center", "color": "#333"}
        ),

        html.Div([
            html.Label("Select Region:", style={"fontWeight": "bold"}),

            dcc.RadioItems(
                id="region-filter",
                options=[
                    {"label": "All", "value": "all"},
                    {"label": "North", "value": "north"},
                    {"label": "East", "value": "east"},
                    {"label": "South", "value": "south"},
                    {"label": "West", "value": "west"},
                ],
                value="all",
                labelStyle={"display": "inline-block", "marginRight": "15px"}
            ),
        ], style={"marginBottom": "20px"}),

        dcc.Graph(id="sales-chart")
    ]
)

# Callback to update graph
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"].str.lower() == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title="Sales Over Time",
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="#f5f5f5",
        xaxis_title="Date",
        yaxis_title="Sales",
    )

    return fig


# Run app
if __name__ == "__main__":
    app.run(debug=True)