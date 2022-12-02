from dash import dcc,html
import dash_bootstrap_components as dbc
from UI import Style
def create_sign_item(*args):
    return dbc.Col([
        html.H3("Private key",style=Style.YellowColor),
        dcc.Textarea(
            id='private-keys',
            style={'width': '100%', 'height': 300},
            placeholder="Enter Private keys"),

        html.H3("Message",style=Style.YellowColor),

        dcc.Textarea(
            id='message',
            placeholder="Enter your message",
            style={'width': '100%', 'height': 300, "margin-bottom":"50px"}),
        dbc.Button(f"Sing message", color="warning", className="mt-auto",
                    id="Sign-btn",n_clicks=0
                        ),
        dcc.Textarea(id="sign-value",readOnly=True,style={'width': '100%', 'height': 300},className="mt-5 mb-5"),
    
        ]
        
    )
