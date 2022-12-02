from dash import dcc,html
import dash_bootstrap_components as dbc
from UI import Style
def create_Keys_UI(pv,pk):
    return dbc.Col([
        html.H3("Private key",style=Style.YellowColor),
        dcc.Textarea(
            id='Private-key',value=pv,readOnly=True,
            style={'width': '100%', 'height': 300},),
        html.H3("Public key",style=Style.YellowColor),

        dcc.Textarea(
            id='Public-key',value=pk,readOnly=True,
            style={'width': '100%', 'height': 300, "margin-bottom":"50px"})]
        
    )