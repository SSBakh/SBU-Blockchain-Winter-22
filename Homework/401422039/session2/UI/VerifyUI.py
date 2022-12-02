from dash import dcc,html
import dash_bootstrap_components as dbc
from UI import Style

def create_UI_Verify(*args):
    
    return dbc.Col([

        dbc.Alert(id="alert-message",
            dismissable=True,
            is_open=False,
            style=Style.PositionSticky
            ),
        html.H3("Public key",style=Style.YellowColor),
        dcc.Textarea(
            id='public-key',
            style={'width': '100%', 'height': 200},),
        
        html.H3("message",style=Style.YellowColor),
        dcc.Textarea(
            id='message',
            style={'width': '100%', 'height': 150, "margin-bottom":"50px"}),
        
        html.H3("sign",style=Style.YellowColor),
        dcc.Textarea(
            id='sign',
            style={'width': '100%', 'height': 70, "margin-bottom":"50px"}),
    
        dbc.Button(f"Vrify message", color="warning", className="mt-auto",
                    id="vrify-btn",n_clicks=0
                        ),
        
        ]
        
    )
    pass