from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware

from src.targeting.context_analyzer import analyze_context
from src.targeting.ad_matcher import match_ads

# Initialize the FastAPI app
app = FastAPI()

# Initialize the Dash app
dash_app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], server=app, url_base_pathname='/')

# Define the layout of the Dash app
dash_app.layout = dbc.Container([
    html.H1("Contextual Targeting Dashboard"),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            html.H3("User Context"),
            dcc.Dropdown(id='user-dropdown', options=[{'label': f'User {i}', 'value': i} for i in range(1, 11)]),
            html.Div(id='user-context-output')
        ], width=6),
        dbc.Col([
            html.H3("Ad Recommendations"),
            html.Div(id='ad-recommendations-output')
        ], width=6)
    ])
])

@dash_app.callback(
    [Output('user-context-output', 'children'),
     Output('ad-recommendations-output', 'children')],
    [Input('user-dropdown', 'value')]
)
def update_output(user_id):
    if user_id is None:
        return "Please select a user.", "No recommendations yet."
    
    context = analyze_context(user_id)
    recommendations = match_ads(context)
    
    context_output = [html.P(f"{k}: {v}") for k, v in context.items()]
    recommendations_output = [html.P(f"Ad {i+1}: {ad}") for i, ad in enumerate(recommendations)]
    
    return context_output, recommendations_output

# Mount the Dash app
app.mount("/", WSGIMiddleware(dash_app.server))

# This is needed for Gunicorn to work with Dash
server = app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
