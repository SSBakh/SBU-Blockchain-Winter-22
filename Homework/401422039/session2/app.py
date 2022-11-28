import dash_bootstrap_components as dbc
import dash_daq as daq
from dash import html,Input,Output,State,dcc,Dash
from UI import menu,Style,KeysUI,Sign,VerifyUI,MineUI
from CryptographyBlockchain import CreateKeys,SignMessage,Verify,Mine
from urllib.parse import unquote

app=Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout=html.Div([dcc.Location(id="url"),dbc.Row([dbc.Col(menu.Create_Card())],id="Main"),dbc.Row(children=[],id="item")],id="root",className="container-fluid",style=Style.MarginTop)


#click btn in Mine page call this function
@app.callback(
    Output(component_id="hash",component_property= 'value'), 
    Output(component_id="nonce",component_property="value"),
    Output(component_id="alert-mine",component_property="is_open"),
    Input(component_id="mine-btn",component_property="n_clicks"),
    State(component_id="block-num",component_property="value"),
    State(component_id="data-text",component_property="value"),
    State(component_id="prev",component_property="value"),
)
def Mine_callback(btn_click,Block_number,data,hash_prev):
    hash,nonce=Mine.min_data(str(data),str(hash_prev),str(Block_number))
    return hash,nonce,True


#click btn in Sign message page call this function
@app.callback(
    Output(component_id="sign-value",component_property= 'value'), 
    Input(component_id="Sign-btn",component_property="n_clicks"),
    State(component_id="private-keys",component_property="value"),
    State(component_id="message",component_property="value"),
)
def Sign_message(btn_click,private_key,message):
    sing=SignMessage.sign_message(message,private_key)
    return sing

#click btn in vrify message page call this function
@app.callback(
    Output(component_id="alert-message",component_property= 'color'), 
    Output(component_id="alert-message",component_property= 'children'), 
    Output(component_id="alert-message",component_property= 'is_open'), 
    Input(component_id="vrify-btn",component_property="n_clicks"),
    State(component_id="public-key",component_property="value"),
    State(component_id="message",component_property="value"),
    State(component_id="sign",component_property="value"),
)
def vrify_message(btn_click,public_key,message,sign):
    res=Verify.get_verify_sign_message(public_key,sign,message)
    status={True:("success","sign is valid",True),False:("danger","sign not valid",True)}
    return status[res]


@app.callback(
    Output(component_id="Main",component_property= 'style'),
    Output(component_id="item",component_property= 'children'),
    Input(component_id="url",component_property="pathname"),
)
def render(pathname):
    if pathname=='/':
        return Style.DisplayBlock,[]
    else:
        url=unquote(pathname)[1:]
        if url in menu.menu_list:
            # dectionry for  select function for url
            functions={"Create Private and Public keys":KeysUI.create_Keys_UI,
                        "Sign message":Sign.create_sign_item,
                        "Verify sign":VerifyUI.create_UI_Verify,
                        "Mine":MineUI.create_UI_Mine}
            
            private_key,public_key=CreateKeys.Create_keys()

            #select functio in url if create private and public keys send args 
            d=functions[url](private_key,public_key)
            return Style.DisplayNone,d
        else:
            return Style.DisplayBlock,[]
        

if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port=9999)