from dash import html
import dash_bootstrap_components as dbc
menu_list=['Create Private and Public keys' ,"Sign message","Verify sign","Mine"]
from UI import Style
def create_card_content(Text):
    card_content = [
        dbc.CardHeader(Text),
        dbc.CardBody(
            [
                html.H5(Text, className="card-title"),
                
                dbc.Button(
                            f"Go {Text}", color="warning", className="mt-auto",href=f"/{Text}"
                        ),
            ]
        ),
    ]
    return card_content

def create_single_row(Text):
    row=dbc.Row([
                dbc.Col(dbc.Card(create_card_content(Text), color="warning", outline=True)),
                ],style=Style.MARGINBottom)
    return row

def create_two_rows(Text1,Text2):
    row=dbc.Row([
                dbc.Col(dbc.Card(create_card_content(Text1), color="warning", outline=True)),
                dbc.Col(dbc.Card(create_card_content(Text2), color="warning", outline=True))
                ],style=Style.MARGINBottom)
    return row

def Create_Card():
    col=dbc.Col([])
    col.children.append(create_two_rows(menu_list[0],menu_list[1]))
    col.children.append(create_two_rows(menu_list[2],menu_list[3]))
    # col.children.append(create_single_row(menu_list[4]))
    return col
