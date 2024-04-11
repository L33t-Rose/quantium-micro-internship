# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("./output.csv")

fig = px.line(df, x="date", y="sales")
locations = ["all", "north", "south", "east", "west"]
sales_graph_selector = "sales-graph"
locations_selector = "location"
app.layout = html.Div(
    id="main",
    className="sales",
    children=[
        html.H1(
            className="sales__heading",
            children="Sales of Pink Morsel from 2018 to 2022",
        ),
        html.Div(
            className="sales__region__wrapper",
            children=[
                html.B("Region:", style={"font-size": "1.25rem"}),
                dcc.RadioItems(
                    className="sales__region",
                    labelClassName="sales__region__button",
                    value="all",
                    options=locations,
                    id=locations_selector,
                    inline=True,
                ),
            ],
        ),
        dcc.Graph(id=sales_graph_selector, figure=fig),
    ],
)


@callback(Output(sales_graph_selector, "figure"), Input(locations_selector, "value"))
def update_graph(location):
    if location == "all":
        return px.line(df, x="date", y="sales", title="Sales in all regions")

    filtered_df = df[df.region == location]
    fig = px.line(filtered_df, x="date", y="sales", title=f"Sales in {location} region")
    fig.update_layout(transition_duration=500)
    return fig


if __name__ == "__main__":
    app.run(debug=True)
