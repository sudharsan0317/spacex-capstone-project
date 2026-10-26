"""
SpaceX Falcon 9 Landing Analysis Dashboard
Run: pip install dash plotly pandas
     python spacex_dashboard.py
Then open the local URL printed in the terminal (usually http://127.0.0.1:8050).
"""
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

df = pd.read_csv("Spacex.csv")
df["PAYLOAD_MASS__KG_"] = pd.to_numeric(df["PAYLOAD_MASS__KG_"], errors="coerce")
df["Landing_Success"] = df["Landing_Outcome"].astype(str).str.startswith("Success").astype(int)

app = Dash(__name__)
sites = sorted(df["Launch_Site"].dropna().unique())
app.layout = html.Div([
    html.H1("SpaceX Falcon 9 Landing Analysis"),
    html.P("Exploratory dashboard built from the supplied Spacex.csv dataset."),
    html.Label("Filter by launch site"),
    dcc.Dropdown(id="site", options=[{"label":"All sites","value":"ALL"}]+[{"label":s,"value":s} for s in sites],
                 value="ALL", clearable=False),
    html.Div(id="summary", style={"padding":"12px","fontWeight":"bold"}),
    dcc.Graph(id="outcomes"),
    dcc.Graph(id="payload")
], style={"fontFamily":"Arial, sans-serif","maxWidth":"1100px","margin":"auto","padding":"20px"})

@app.callback(
    Output("summary","children"), Output("outcomes","figure"), Output("payload","figure"),
    Input("site","value")
)
def update_dashboard(site):
    d = df if site == "ALL" else df[df["Launch_Site"] == site]
    rate = d["Landing_Success"].mean()*100 if len(d) else 0
    summary = f"Launches: {len(d)} | Labelled successful landings: {int(d['Landing_Success'].sum())} | Labelled success rate: {rate:.1f}%"
    fig1 = px.histogram(d, x="Landing_Outcome", title="Landing outcome categories", text_auto=True)
    fig1.update_layout(xaxis_title="Landing outcome", yaxis_title="Launch count")
    fig2 = px.strip(d, x="Landing_Success", y="PAYLOAD_MASS__KG_", color="Landing_Outcome",
                    title="Payload mass by binary landing label",
                    labels={"Landing_Success":"Labelled success (1=yes)","PAYLOAD_MASS__KG_":"Payload mass (kg)"})
    return summary, fig1, fig2

if __name__ == "__main__":
    app.run(debug=True)
