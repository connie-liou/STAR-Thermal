import os
import sys
from exceptions import *

import dash
from dash.dependencies import *
from dash.exceptions import PreventUpdate
from flask import Flask
import pandas as pd
import numpy as np

from HelpPopups import popupCallbacks
from Layout import layout


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

layout(app)
#CallBacks #####################################################################################################
@app.callback([Output('node-table', 'columns'), Output('radiation-table', 'columns'), 
            Output('radiation-table','data'), Output('conductance-table', 'columns'), 
            Output('conductance-table', 'data'), Output('prev_num_nodes', 'children'),
            Output('rad-matrix-error', 'style'), Output('cond-matrix-error', 'style')], 
            [Input('num-nodes', 'value'), Input('radiation-table','data_timestamp'), Input('conductance-table','data_timestamp')], 
            [State('node-table','columns'), State('radiation-table', 'columns'), 
            State('radiation-table','data'), State('conductance-table', 'columns'), 
            State('conductance-table', 'data'),State('prev_num_nodes', 'children')])
def addNodes(numNodes, radActive, condActive, nodeCols, radCols, radRows, condCols, condRows,prevNumNodes):
    if prevNumNodes is None:
        prevNumNodes = 0
    
    if(numNodes == prevNumNodes):
        rad_df= pd.DataFrame(radRows)
        rad_arr = rad_df.values[:, 1:]
        isRadSymm = True
        # print(rad_arr)

        cond_df= pd.DataFrame(condRows)
        cond_arr = cond_df.values[:, 1:]
        isCondSymm = True
        # print(cond_arr)
        

        radStyle = {'display':'none'}
        condStyle = {'display':'none'}

        for i in range (0, numNodes):
            for j in range (0, numNodes):
                if i == j:
                    if rad_arr[i][j]!=0:
                        isRadSymm = False
                        radStyle = {'display':'block'}
                    if cond_arr[i][j]!=0:
                        isCondSymm = False
                        condStyle = {'display':'block'}
                else: 
                    if rad_arr[i][j] != rad_arr[j][i]:
                        isRadSymm = False
                        radStyle = {'display':'block'}
                    if cond_arr[i][j] != cond_arr[j][i]:
                        isCondSymm = False
                        condStyle = {'display':'block'}
        # print(isRadSymm, isCondSymm)
        # print('----')
        return [nodeCols, radCols, radRows, condCols, condRows, numNodes, radStyle, condStyle]
    else:        
        if numNodes >= len(nodeCols):
            extra = numNodes - len(nodeCols) + 1
            for i in range (extra):
                nodeCols.append({
                            'id': ('node-'+str(len(nodeCols))), 'name': ('Node '+str(len(nodeCols))),
                            'renamable': True, 'deletable': False, 'editable':True, 'type': 'numeric'
                            })
                radCols.append({
                            'id': ('radiation-'+str(len(nodeCols)-1)), 'name': ('Surface '+str(len(nodeCols)-1)),
                            'renamable': True, 'deletable': False, 'editable':True, 'type': 'numeric'
                            })
                newRow = {**{radCols[0]['id']:('Surface ' + str(len(nodeCols)-1))},** {i['id']:0 for i in radCols[1:]}}
                radRows.append(newRow)
                condCols.append({
                            'id': ('conductance-'+str(len(nodeCols)-1)), 'name': ('Surface '+str(len(nodeCols)-1)),
                            'renamable': True, 'deletable': False, 'editable':True, 'type': 'numeric'
                            })
                newRow = {**{condCols[0]['id']:('Surface ' + str(len(nodeCols)-1))}, **{i['id']:0 for i in condCols[1:]}}
                condRows.append(newRow)
        elif numNodes < len(nodeCols)-1:
            nodeCols.pop()
            radCols.pop()
            radRows.pop()
            condCols.pop()
            condRows.pop()


        return [nodeCols, radCols, radRows, condCols, condRows, numNodes, dash.no_update, dash.no_update]

# @app.callback([Output('radiation-table', 'style-cell'), Output('conductance-table', 'style-cell')], 
#             [Input('radiation-table','data'), Input('conductance-table', 'data')], 
#             [State('num-nodes', 'value'),State('radiation-table', 'columns'), State('conductance-table', 'columns')])
# def addNodes(radData, condData, numNodes, radCols, condCols):
    


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

@app.callback( 
    [Output(component_id='LEO-orbit-container', component_property='style'),
    Output(component_id='constant-orbit-container', component_property='style')],
    [Input('orbit-type', 'value')])
def change_orbit(orbit):
    if (orbit == 'L1' or orbit == 'L2'):
        return {'display': 'none'}, {'display': 'block'}

    else:
        return {'display': 'block'}, {'display': 'none'}

@app.callback(
    [Output(component_id='simple-orbit-container', component_property='style'),
    Output(component_id='complex-orbit-container', component_property='style')],
    [Input('use-simple-orbit', 'value')])
def use_simple_orbit(orbitType):
    if (orbitType == 'Simple'):
        return {'display': 'block'}, {'display': 'none'}
    else:
        return {'display': 'none'}, {'display': 'block'}
        
popupCallbacks(app)
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
