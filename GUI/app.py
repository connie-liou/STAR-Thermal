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
@app.callback([Output('node-table', 'columns'), Output('radiation-table', 'columns'), Output('radiation-table','data'), Output('conductance-table', 'columns'), Output('conductance-table', 'data')], 
            [Input('num-nodes', 'value')], 
            [State('node-table','columns'), State('radiation-table', 'columns'), State('radiation-table','data'), State('conductance-table', 'columns'), State('conductance-table', 'data')])
def addNodes(numNodes, nodeCols, radCols, radRows, condCols, condRows):
    
    if numNodes >= len(nodeCols):
        extra = numNodes - len(nodeCols) + 1
        for i in range (extra):
            nodeCols.append({
                        'id': ('node-'+str(len(nodeCols))), 'name': ('Node '+str(len(nodeCols))),
                        'renamable': True, 'deletable': False, 'editable':True
                        })
            radCols.append({
                        'id': ('radiation-'+str(len(nodeCols)-1)), 'name': ('Surface '+str(len(nodeCols)-1)),
                        'renamable': True, 'deletable': False, 'editable':True
                        })
            radRows.append({'surface-number':('Surface ' + str(len(nodeCols)-1))})
            condCols.append({
                        'id': ('conductance-'+str(len(nodeCols)-1)), 'name': ('Surface '+str(len(nodeCols)-1)),
                        'renamable': True, 'deletable': False, 'editable':True
                        })
            condRows.append({'surface-conductance-number':('Surface ' + str(len(nodeCols)-1))})
    elif numNodes < len(nodeCols)-1:
        nodeCols.pop()
        radCols.pop()
        radRows.pop()
        condCols.pop()
        condRows.pop()
    return [nodeCols, radCols, radRows, condCols, condRows]

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
    app.run_server(debug=True, port=8050)
