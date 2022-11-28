from dash import dcc, html
import dash_bootstrap_components as dbc
from UI import Style


def create_UI_Mine(*args):

    return dbc.Col([
        dbc.Alert(
            "successfully mine",
            color="success",
            id="alert-mine",
            dismissable=True,
            is_open=False,
            style=Style.PositionSticky
            
            ),
        dbc.Row([
            dbc.Col(
                html.H5("Block #:", style=Style.YellowColor),width=2
            ),
            dbc.Col(
                dcc.Input(
                    type="number",
                    id='block-num',
                    style={'width': '100%'},
                    value=1
                )
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H5("Nonce :", style=Style.YellowColor),width=2
            ),
            dbc.Col(
                dcc.Input(
                    type="text",
                    id='nonce',
                    style={'width': '100%'},
                    readOnly=True,
                    value=69712
                )
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H5("Data :", style=Style.YellowColor),width=2
            ),
            dbc.Col(
                dcc.Textarea(
                    id='data-text',
                    style={'width': '100%', 'height': 200},
                )
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H5("Prev :", style=Style.YellowColor),width=2
            ),
            dbc.Col(
                dcc.Input(
                    type="text",
                    id='prev',
                    style={'width': '100%',},
                    readOnly=True,
                    value='0'*64
                )
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H5("Hash :", style=Style.YellowColor),width=2
            ),
            dbc.Col(
                dcc.Input(
                    type="text",
                    id='hash',
                    style={'width': '100%'},
                    readOnly=True,
                    value="000015783b764259d382017d91a36d206d0600e2cbb3567748f46a33fe9297cf"
                )
            )
        ]),

        dbc.Button(f"Mine", color="warning", className="mt-5",
                   id="mine-btn", n_clicks=0
                   ),

    ],style=Style.Margin50

    )
