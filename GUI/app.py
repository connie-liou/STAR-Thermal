import os
import sys
from exceptions import *

import dash
from dash.dependencies import *
from dash.exceptions import PreventUpdate
from flask import Flask

from HelpPopups import popupCallbacks
from Layout import layout

sys.path.append("/classes/")

'''
Init dash and flask applications and add extra assests
'''
def find_data_file(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)

    return os.path.join(datadir, filename)
server = Flask('app')

app = dash.Dash(__name__, assets_folder=find_data_file('assets/'), server=server)

app.title = 'EPS Design Tool'

UPLOAD_DIRECTORY = "/project/api_uploaded_files"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)
layout(app)
#CallBacks #####################################################################################################

@app.callback([Output('complex-solar-container', 'style'), Output('simple-solar-container', 'style')], [Input('use-simple-solar', 'value')])
def showSolar(useSimpleSolar):
    if (useSimpleSolar == 'Simple'):
        return {'display': 'none'}, {'display': 'flex'}
    else:
        return {'display': ''}, {'display': 'none'}

@app.callback([Output('load-table-container', 'style'), Output('constant-load-container','style')], [Input('use-constant-load', 'value')])
def loadDisplay(useLoad):
    if (useLoad == 'constant'):
        return {'display': 'none'}, {'display': 'block'}
    else:
        return {'display': 'block'}, {'display': 'none'}

@app.callback([Output('spinner-inputs', 'style'), Output('use-sunangles','options'), Output('use-sunangles', 'value'), Output('Solar-Table', 'style_data_conditional')], [Input('use-spinner', 'value')])
def spinner(useSpinner):
    if (useSpinner == 'Yes'):
        options=[{'label': 'Yes', 'value': 'Yes', 'disabled':True},
                 {'label': 'No', 'value': 'No', 'disabled':True}]
        styleDataCond = [{'if': {'column_id': str(x)},
                        'backgroundColor': '#464646'} for x in ['roll','pitch']]
        return {'display': 'flex'}, options, 'No', styleDataCond
    else:
        options=[{'label': 'Yes', 'value': 'Yes'},
                 {'label': 'No', 'value': 'No'}]
        return {'display': 'none'}, options, 'No', None

@app.callback([Output('EOL-table-container', 'style'), Output('num-EOL', 'disabled')], [Input('use-EOL', 'value')])
def useEOLFact(useEOL):
    if useEOL == 'Yes':
        return [{'display':'block'}, False]
    else:
        return [{'display':'none'}, True]
@app.callback( 
    [Output(component_id='sun-angle-table-container', component_property='style'),
    Output(component_id='time-sun-angle-table-container', component_property='style'),
    Output(component_id='LEO-orbit-container', component_property='style'),
    Output(component_id='constant-orbit-container', component_property='style')],
    [Input('orbit-type', 'value'), Input('use-sunangles', 'value')])
def change_orbit(orbit, useSunAngles):
    if (orbit == 'L1' or orbit == 'L2'):
        if (useSunAngles == 'Yes'):
            return {'display': 'none'}, {'display': 'block'}, {'display': 'none'}, {'display': 'flex'}
        else:
            return {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'flex'}
    else: #LEO
        if(useSunAngles == 'Yes'):
            return {'display': 'block'}, {'display': 'none'}, {'display': 'flex'}, {'display': 'none'}
        else:
            return {'display': 'none'}, {'display': 'none'}, {'display': 'flex'}, {'display': 'none'}

@app.callback( #checks if rows and num sides are same, chaining inputs for import func
    [Output('num-sides','value')],
    [Input('Solar-Table', 'data')],
    [State('num-sides','value')])
def update_numSides_val(rows, numSides):
    if len(rows) != numSides:
        return [len(rows)]
    else:
        raise PreventUpdate

@app.callback( #checks if rows and num sides are same, chaining inputs for import func
    [Output('num-EOL','value')],
    [Input('Solar-Table-EOL', 'data')],
    [State('num-EOL','value')])
def update_numEOL_val(rows, numSides):
    if len(rows) != numSides:
        return [len(rows)]
    else:
        raise PreventUpdate
#determines power topology
@app.callback([Output('efficiency','disabled')],[Input('power-reg-type','value')])
def update_efficiency(regType):
    if regType =='DET':
        return [True]
    else: 
        return [False]

@app.callback(Output('confirm-zerodivision-error', 'displayed'), [Input('confirm-zerodivision-error', 'message')], [State('run_button', 'n_clicks'), State('prev_clicks_run', 'children')])
def display_confirm(value, clicks, prevClicks):
    if clicks is None:
        clicks = 0
    if prevClicks is None:
        prevClicks = 0
    if clicks == 0:
        raise PreventUpdate
    else:
        return True

@app.callback([Output('all-tab-container', 'className'), Output('show-container', 'style'), Output('hide-container', 'style')],
            [Input('hide-tabs', 'n_clicks'), Input('show-tabs', 'n_clicks')])
def hideTabs (hideClicks, showClicks):
    if hideClicks is None:
        hideClicks = 0
    if showClicks is None:
        showClicks = 0
    if showClicks == 0 and showClicks == hideClicks:
        return ['pretty_container fadein', {'display': 'none'}, {'display': 'flex'}]
    elif showClicks>=hideClicks:
        return ['pretty_container fadein', {'display': 'none'}, {'display': 'flex'}]
    else:
        return ['pretty_container fadein fadeout', {'display': 'flex'}, {'display': 'none'}]

popupCallbacks(app)
if __name__ == '__main__':
    app.run_server(host='0.0.0.0',debug=False, port=8050)
