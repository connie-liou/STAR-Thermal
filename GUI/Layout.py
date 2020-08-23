import os
from os import listdir
from os.path import abspath, isfile, join

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
import dash_table
import plotly.graph_objs as go


'''
This file contains the HTML layout of the application.
'''
def layout(app):
    bV = go.Scatter(
        x=[0],
        y=[0],
        name='Voltage (V)',
        mode='lines', line=dict(color='rgb(255,0,0)')
    )
    ahrChange = go.Scatter(
        x=[0],
        y=[0],
        name='Ahr Change',
        mode='lines', line=dict(color='rgb(210,194,49)'),
        yaxis='y4'
    )
    SOC = go.Scatter(
        x=[0],
        y=[0],
        name='SOC',
        yaxis='y2',
        mode='lines', line=dict(color='rgb(0, 255, 100)')
    )
    current = go.Scatter(
        x=[0],
        y=[0],
        name='Current (A)',
        yaxis='y3',
        mode='lines', line=dict(color='rgb(0,0,255)')
    )
    power = go.Scatter(
        x=[0],
        y=[0],
        name='Power (W)',
        yaxis='y2',
        mode='lines', line=dict(color='rgb(0, 255, 100)')
    )
    lc = go.Scatter(
        x=[0],
        y=[0],
        name='Load Current (A)',
        yaxis='y3',
        mode='lines', line=dict(color='rgb(0, 0, 255)')
    )
    lv = go.Scatter(
        x=[0],
        y=[0],
        name='Load Voltage (V)',
        mode='lines', line=dict(color='rgb(255,0,0)')
    )

    sP = go.Scatter(
        x=[0],
        y=[0],
        name='Power (W)',
        yaxis='y2',
        mode='lines', line=dict(color='rgb(255,0,255)')
    )
    sI = go.Scatter(
        x=[0],
        y=[0],
        name='Current (A)',
        yaxis='y3',
        mode='lines', line=dict(color='rgb(0, 0, 255)')
    )
    sV = go.Scatter(
        x=[0],
        y=[0],
        name='Voltage (V)',
        mode='lines', line=dict(color='rgb(255,0,0)')
    )
    power = go.Scatter(
        x=[0],
        y=[0],
        name='Load Power (W)',
        yaxis='y4',
        mode='lines', line=dict(dash='dot', color='rgb(255, 0, 255)')
    )

    solarAP = go.Scatter(
        x=[0],
        y=[0],
        name='Solar Array Power',
        yaxis='y2',
        legendgroup='array',
        mode='lines', line=dict(color='rgb(255,0,0)')
    )
    solarAI = go.Scatter(
        x=[0],
        y=[0],
        name='Solar Array Current',
        legendgroup='array',
        mode='lines', line=dict(color='rgb(0,0,255)')
    )

    # systempath = os.getcwd() + '/Presets/System/'
    # batterypath = os.getcwd() + '/Presets/Battery/'
    # loadpath = os.getcwd() + '/Presets/Load/'
    # orbitpath = os.getcwd() + '/Presets/Orbit/'
    # solarpath = os.getcwd() + '/Presets/Solar/'
    # systemfiles = [f for f in listdir(systempath) if isfile(join(systempath, f))]
    # batteryfiles = [f for f in listdir(batterypath) if isfile(join(batterypath, f))]
    # loadfiles = [f for f in listdir(loadpath) if isfile(join(loadpath, f))]
    # orbitfiles = [f for f in listdir(orbitpath) if isfile(join(orbitpath, f))]
    # solarfiles = [f for f in listdir(solarpath) if isfile(join(solarpath, f))]
    # optionList = []
    # optionList.append({'label': 'Custom...', 'value': 'custom'})
    # optionList.append({'label': '=========System=========', 'value': '', 'disabled': True})
    # for i in systemfiles:
    #     optionList.append({'label': i, 'value': systempath + i})
    # optionList.append({'label': '=========Battery========', 'value': '', 'disabled': True})
    # for i in batteryfiles:
    #     optionList.append({'label': i, 'value': batterypath + i})
    # optionList.append({'label': '=========Load===========', 'value': '', 'disabled': True})
    # for i in loadfiles:
    #     optionList.append({'label': i, 'value': loadpath + i})
    # optionList.append({'label': '=========Orbit==========', 'value': '', 'disabled': True})
    # for i in orbitfiles:
    #     optionList.append({'label': i, 'value': orbitpath + i})
    # optionList.append({'label': '======Solar Array=======', 'value': '', 'disabled': True})
    # for i in solarfiles:
    #     optionList.append({'label': i, 'value': solarpath + i})
    app.layout = html.Div([
        html.Div(id='junk'), 
        html.Div(id='prev_clicks_run', hidden=True), 
        html.Div(id = 'prev_clicks_import', hidden = True),
        html.Div(id = 'prev_num_sides', hidden = True),
        html.Div(id = 'prev_num_EOL', hidden = True),
        html.Div(id = 'prev_num_nodes', hidden = True),
        dcc.ConfirmDialog(
            id='exportRaw'
        ),
        dcc.ConfirmDialog(
            id='confirm-zerodivision-error',
            message='Please fill out all fields or check for zero values',
        ),   
        html.Div([
            
            html.Div([
                html.Div([
                    # html.Img(src=app.get_asset_url('nasa-logo.png'), id='logo'),
                    html.Img(src=app.get_asset_url('eps design tool logo.png'), id = 'title'),
                ],id = 'logo-title-header'),
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('show.png'), id = 'show-tabs', className = 'icon'), 
                        html.Div(html.P('Show Tabs')),
                        ], id = 'show-container', className = 'input-container'),
                    html.Div([
                        html.Img(src=app.get_asset_url('collapse.png'), id = 'hide-tabs', className = 'icon'),
                        html.Div(html.P('Hide Tabs')),
                        ], id = 'hide-container', className = 'input-container'),
                ]),
            ]),
            html.Div([ #naming
                html.Div([
                    html.Div([html.Img(src=app.get_asset_url('satellite icon.png'), className='icon'), html.P('System:', id='systemName')], className = 'input-container magnify'),
                    html.Div(children=[html.Img(src=app.get_asset_url('battery icon.png'), className='icon'), html.P('Battery:', id='batteryName')], className = 'input-container magnify'),
                    html.Div(children=[html.Img(src=app.get_asset_url('flash icon.png'), className='icon'), html.P('Load:', id='loadName')], className = 'input-container magnify')
                ], id='left-name'),
                html.Div([
                    html.Div([html.Img(src=app.get_asset_url('orbit.png'), className='icon'), html.P('Orbit:', id='orbitName')], className = 'input-container magnify'),
                    html.Div([html.Img(src=app.get_asset_url('solar panel.png'), className='icon'), html.P('Solar Array:', id='solarName')], className = 'input-container magnify')
                ], id='right-name') 
            ], id='name-container'),
            html.Div([
                html.Div([dcc.Dropdown(id='input_dropdown'),]),
                html.Div([
                    html.Button('Update', id='import-button', hidden = True, className='button')
                ], id = 'import-button-container', style = {'display':'none'}),
            ], style = {'padding':'none'}),
            
            html.Div([
                dcc.Upload(
                id='import-upload',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                    ])
                )
            ], id = 'import-upload-container', style={'display':'none'}),
            
            
        ], className = 'input-container', id = 'header'),

        html.Div(children=[dcc.Loading(id='loadingRunButton', type='default', children=[html.A("Run", className='runButton', id='run_button')]), ], className='sticky', id='run-container'),
        # html.Div([html.Img(src=app.get_asset_url('blank-nasa-logo.png'), id='logo-button')]),
        html.Div([  # row with tabs and graphs
            # tabs
            html.Div([  # tabs
                dcc.Tabs(id="custom-tabs", children=[
                    #######################################################################################################
                    dcc.Tab(label='Nodes', children=[
                        html.Div([
                            html.Div([html.H6("Input nodes"),],),
                            html.Div([daq.NumericInput(
                                        id='num-nodes',
                                        label='Number of Nodes',
                                        labelPosition='top',
                                        max=100,
                                        min=1,
                                        value=2,
                                    ),
                                    ]),
                            
                            html.Div([
                                dash_table.DataTable(
                                    id = 'node-table',
                                    columns=[{
                                            'name': 'Properties',
                                            'id': 'node-column',
                                            'deletable': False,
                                            'renamable': False,
                                            'clearable': False,
                                            'editable': False
                                        }, {
                                            'name': 'Node 1',
                                            'id': 'node-1',
                                            'type': 'numeric',
                                            'deletable': False,
                                            'renamable': False,
                                            'clearable': True
                                        }, {
                                            'name': 'Node 2',
                                            'id': 'node-2',
                                            'type': 'numeric',
                                            'deletable': False,
                                            'renamable': False,
                                            'clearable': True
                                        }],
                                        data=[
                                            {'node-column':'Name'},
                                            {'node-column':'Initial Temp (K)'},
                                            {'node-column':'Surface Area (m^2)'},
                                            {'node-column':'Thickness(m)'},
                                            {'node-column':'Density(kg/m^3)'},
                                            {'node-column':'Specific Heat(J/kg/K)'},
                                            {'node-column':'absorptivity'},
                                            {'node-column':'emissivity'},
                                            {'node-column':'Heat Dissipation (W)'},],
                                        editable=True,
                                        row_deletable=False,
                                        export_headers='display',
                                        style_cell={
                                            'color': 'black',
                                            'whiteSpace': 'normal',
                                            'height': 'auto',
                                            'maxWidth': 50,
                                        }
                                )
                                ], className='table-container', id='node-table-container'),
                            
                            html.Hr(),
                            html.Div([
                                html.P("Click for detailed help"),
                                html.Img(src=app.get_asset_url('help.png'), className = 'helpButton', id='general-help-button'),
                            ], className='help-button-container')
                        ], className='tab-container')
                    ], className='custom-tab')
                    ######################################################################################################################3
                    , dcc.Tab(label='Radiation', children=[
                        html.Div([
                            html.H6('Radiation View Factors'),
                            html.Div([
                                dash_table.DataTable(
                                    id = 'radiation-table',
                                    
                                        columns=[
                                            {"name": "Surface #", "id": "surface-number"},
                                            {
                                                'name': 'Surface 1',
                                                'id': 'radiation-1',
                                                'type': 'numeric',
                                                'deletable': False,
                                                'renamable': False,
                                                'clearable': True
                                            },
                                            {
                                                'name': 'Surface 2',
                                                'id': 'radiation-2',
                                                'type': 'numeric',
                                                'deletable': False,
                                                'renamable': False,
                                                'clearable': True
                                            },
                                        ],
                                        data=[
                                            {'surface-number': 'Surface 1', 'radiation-1': 0, 'radiation-2':0},
                                            {'surface-number': 'Surface 2', 'radiation-1': 0, 'radiation-2':0}
                                            ],
                                        merge_duplicate_headers=True,
                                        editable=True,
                                        row_deletable=False,
                                        export_headers='display',
                                        style_cell={
                                            'color': 'black',
                                            'whiteSpace': 'normal',
                                            'height': 'auto',
                                            'maxWidth': 50,
                                        },
                                        # style_data_conditional=[
                                        #     {
                                        #         'if': {
                                        #             'filter_query': '{{{col}}} > 5',
                                        #             'column_id': '{Surface 1}'
                                        #         },
                                        #     'backgroundColor': 'salmon',
                                        #     } 
                                        # ]
                                )
                            ],className='table-container'),
                        ], id = 'radiation-table-container',className='tab-container '),
                        html.Div([html.H6('Check Matrix Symmetry', style={'color': 'red'})], id = 'rad-matrix-error',hidden=True),
                        html.Hr(),
                        html.Div([
                            html.P("Click for detailed help"),
                            html.Img(src=app.get_asset_url('help.png'), className = 'helpButton', id='battery-help-button'),
                        ], className='help-button-container')
                    ], className='custom-tab')
                    ##################################################################################################
                    , dcc.Tab(label='Conductance', children=[
                        html.Div([
                            html.Div([
                                html.H6('Conductance between nodes'),
                                html.Div([
                                    dash_table.DataTable(
                                        id = 'conductance-table',
                                            columns=[
                                                {"name": "Surface #", "id": 'surface-conductance-number'},
                                                {
                                                    'name': 'Surface 1',
                                                    'id': 'conductance-1',
                                                    'type': 'numeric',
                                                    'deletable': False,
                                                    'renamable': False,
                                                    'clearable': True
                                                },
                                                {
                                                    'name': 'Surface 2',
                                                    'id': 'conductance-2',
                                                    'type': 'numeric',
                                                    'deletable': False,
                                                    'renamable': False,
                                                    'clearable': True
                                                },
                                            ],
                                                data=[
                                                    {'surface-conductance-number': 'Surface 1', 'conductance-1': 0, 'conductance-2':0},
                                                    {'surface-conductance-number': 'Surface 2', 'conductance-1': 0, 'conductance-2':0}  
                                                    
                                                    ],
                                                merge_duplicate_headers=True,
                                                editable=True,
                                                row_deletable=False,
                                                export_headers='display',
                                                style_cell={
                                                    'color': 'black',
                                                    'whiteSpace': 'normal',
                                                    'height': 'auto',
                                                    'maxWidth': 50,
                                                }
                                    )
                                ],className='table-container'),
                            ], id = 'conductance-table-container'),
                            html.Div([html.H6('Check Matrix Symmetry', style={'color': 'red'})], id = 'cond-matrix-error',hidden=True),
                            html.Hr(),
                            html.Div([
                                html.P("Click for detailed help"),
                                html.Img(src=app.get_asset_url('help.png'), className = 'helpButton', id='load-help-button'),
                            ], className='help-button-container')
                        ], className='tab-container')
                    ], className='custom-tab')
                    #######################################################################################################################3
                    , dcc.Tab(label='Orbit', children=[
                        html.Div([
                            html.Div([
                                html.H6('Select Orbit Model'),
                                dcc.RadioItems(
                                        options=[
                                            {'label': 'Simple', 'value': 'Simple'},
                                            {'label': 'Complex', 'value': 'Complex'}
                                        ],
                                        value='Simple',
                                        id='use-simple-orbit'
                                ),
                            ], className='save-container'),
                            html.Hr(),                        
                            #Simple Orbit Container
                            html.Div([
                                html.Div([
                                    html.P("Orbit Type", className='sc-bwzfXH.eYbLCt orbit-label'),
                                    dcc.Dropdown(
                                        id='orbit-type',
                                        className = 'orbit-dropdown',
                                        options=[
                                            {'label': 'L1', 'value': 'L1'}, {'label': 'L2', 'value': 'L2'},
                                            {'label': 'LEO', 'value': 'LEO'}],
                                        value='LEO'
                                    ),
                                ], className='orbit-container'),
                                # html.P("Note: Choose a time interval less than or equal to your data time steps"),
                                html.Div([
                                    html.Div([
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("Start Time (mins)"),
                                                dbc.Input(
                                                    type = "number", 
                                                    min = 0, 
                                                    max = 1000000000, 
                                                    step=0.0001,
                                                    id = 'start-time',
                                                    value=0,
                                                    className = 'styled-numeric-input',
                                                    debounce=True)
                                            ]),
                                    ]),
                                    html.Div([
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("End Time (mins)"),
                                                dbc.Input(
                                                    type = "number", 
                                                    min = 0, 
                                                    max = 10000000000, 
                                                    step=0.0001,
                                                    id = 'end-time',
                                                    value=600,
                                                    className = 'styled-numeric-input',
                                                    debounce=True)
                                            ]),
                                    ]),
                                    html.Div([
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("Time Interval (mins)"),
                                                dbc.Input(
                                                    type = "number", 
                                                    min = 0, 
                                                    max = 100000000, 
                                                    step=0.0001,
                                                    id = 'timestep',
                                                    value=1,
                                                    className = 'styled-numeric-input',
                                                    debounce=True)
                                            ]),
                                    ]),
                                ], className='save-container'),
                                html.Div([
                                    html.Div([
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("Orbit Period (mins)"),
                                                dbc.Input(
                                                    type = "number", 
                                                    min = 0, 
                                                    max = 10000000, 
                                                    step=0.0001,
                                                    id = 'period',
                                                    value=92,
                                                    className = 'styled-numeric-input',
                                                    debounce=True)
                                            ]),
                                    ]),
                                    html.Div([
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("Eclipse Length (mins)"),
                                                dbc.Input(
                                                    type = "number", 
                                                    min = 0, 
                                                    max = 10000000, 
                                                    step=0.0001,
                                                    id = 'eclipse-length',
                                                    value=31,
                                                    className = 'styled-numeric-input',
                                                    debounce=True)
                                            ]),
                                    ]),
                                ], id='LEO-orbit-container', className='save-container'),
                                html.Div([
                                    html.Div([
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("Eclipse Start Time (mins)"),
                                                dbc.Input(
                                                    type = "number", 
                                                    min = 0, 
                                                    max = 100000000, 
                                                    step=0.0001,
                                                    id = 'eclipse-start',
                                                    value=10,
                                                    className = 'styled-numeric-input',
                                                    debounce=True)
                                            ]),
                                    ]),
                                    html.Div([
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("Eclipse End Time (mins)"),
                                                dbc.Input(
                                                    type = "number", 
                                                    min = 0, 
                                                    max = 10000000000, 
                                                    step=0.0001,
                                                    id = 'eclipse-end',
                                                    value=100,
                                                    className = 'styled-numeric-input',
                                                    debounce=True)
                                            ]),
                                    ]),
                                ], id='constant-orbit-container', className='save-container'),
                            ], id = 'simple-orbit-container', className = 'save-container'),
                            
                            
                            html.Div([ #Complex Orbit Container
                                
                                    
                                    html.Div([ #Start/End Times row
                                        html.Div([
                                            dbc.FormGroup(
                                                [
                                                    dbc.Label("Start Time (mins)"),
                                                    dbc.Input(
                                                        type = "number", 
                                                        min = 0, 
                                                        max = 1000000000, 
                                                        step=0.0001,
                                                        id = 'start-time-complex',
                                                        value=0,
                                                        className = 'styled-numeric-input',
                                                        debounce=True)
                                                ]),
                                        ]),
                                        html.Div([
                                            dbc.FormGroup(
                                                [
                                                    dbc.Label("End Time (mins)"),
                                                    dbc.Input(
                                                        type = "number", 
                                                        min = 0, 
                                                        max = 10000000000, 
                                                        step=0.0001,
                                                        id = 'end-time-complex',
                                                        value=600,
                                                        className = 'styled-numeric-input',
                                                        debounce=True)
                                                ]),
                                        ]),
                                        html.Div([
                                            dbc.FormGroup(
                                                [
                                                    dbc.Label("Time Interval (mins)"),
                                                    dbc.Input(
                                                        type = "number", 
                                                        min = 0, 
                                                        max = 100000000, 
                                                        step=0.0001,
                                                        id = 'timestep-complex',
                                                        value=1,
                                                        className = 'styled-numeric-input',
                                                        debounce=True)
                                                ]),
                                        ]),
                                    ], className='save-container'),
                                    html.Div([
                                        html.P("Spacecraft Configuration?", className='sc-bwzfXH.eYbLCt orbit-label'),
                                        dcc.Dropdown(
                                            id='spacecraft-config',
                                            className='orbit-dropdown',
                                            options=[
                                                {'label': 'Rectangle', 'value': 'rect'}, {'label': 'Triangle', 'value': 'tri'},
                                                {'label': 'Hexagonal', 'value': 'hex'}],
                                            value='rect'
                                        ),
                                    ], className='orbit-container'),
                                    
                                    html.P('Orbital Elements'),
                                    html.Div([ #Orbital Elements cluster
                                        html.Div([
                                            dbc.FormGroup(
                                                [
                                                    dbc.Label("Inclination (deg)"),
                                                    dbc.Input(
                                                        type = "number", 
                                                        min = -360, 
                                                        max = 360, 
                                                        step=0.0001,
                                                        id = 'inclination',
                                                        value=0,
                                                        className = 'styled-numeric-input',
                                                        debounce=True)
                                                ]),
                                            ]),
                                        html.Div([
                                            dbc.FormGroup(
                                                [
                                                    dbc.Label("Right Ascencion of Ascenidng node"),
                                                    dbc.Input(
                                                        type = "number", 
                                                        min = 0, 
                                                        max = 10000000000, 
                                                        step=0.0001,
                                                        id = 'right-ascension',
                                                        value=0,
                                                        className = 'styled-numeric-input',
                                                        debounce=True)
                                                ]),
                                            ]),
                                        html.Div([
                                            dbc.FormGroup(
                                                [
                                                    dbc.Label("Argument of Periapsis"),
                                                    dbc.Input(
                                                        type = "number", 
                                                        min = 0, 
                                                        max = 100000000, 
                                                        step=0.0001,
                                                        id = 'periapsis',
                                                        value=1,
                                                        className = 'styled-numeric-input',
                                                        debounce=True)
                                                ]),
                                            ]),

                                    ], className='save-container'),
                                    html.Div([
                                        html.Div([
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("Max Altitude (km)"),
                                                dbc.Input(
                                                    type = "number", 
                                                    min = 0, 
                                                    max = 10000000000, 
                                                    step=0.0001,
                                                    id = 'max-altitude',
                                                    value=0,
                                                    className = 'styled-numeric-input',
                                                    debounce=True)
                                            ]),
                                        ]),
                                        html.Div([
                                            dbc.FormGroup(
                                                [
                                                    dbc.Label("eccentricity"),
                                                    dbc.Input(
                                                        type = "number", 
                                                        min = 0, 
                                                        max = 1, 
                                                        step=0.0001,
                                                        id = 'eccentricity',
                                                        value=1,
                                                        className = 'styled-numeric-input',
                                                        debounce=True)
                                            ]),
                                        ]),
                                    ], className='save-container'),
                                    
                                    html.Div([
                                            html.P("Z+ initial orientation", className='sc-bwzfXH.eYbLCt orbit-label'),
                                            dcc.Dropdown(
                                                id='z-initial-orient',
                                                className='orbit-dropdown',
                                                options=[
                                                    {'label': 'Sun', 'value': 'sun'}, {'label': 'Earth', 'value': 'Earth'}],
                                                value='rect'
                                            ),
                                        ], className='orbit-container'),
                                    html.Div([
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("Additional Rotation (deg per orbit)"),
                                                dbc.Input(
                                                    type = "number", 
                                                    min = 0, 
                                                    max = 10000000000, 
                                                    step=0.0001,
                                                    id = 'additional-rotation',
                                                    value=0,
                                                    className = 'styled-numeric-input',
                                                    debounce=True)
                                            ]),
                                    ]),
                                    html.Div([
                                        html.P("About which Spacecraft axis?", className='sc-bwzfXH.eYbLCt orbit-label'),
                                        dcc.Dropdown(
                                            id='spacecraft-axis',
                                            className='orbit-dropdown',
                                            options=[
                                                {'label': 'X', 'value': 'X'}, {'label': 'Y', 'value': 'Y'},
                                                {'label': 'Z', 'value': 'Z'}],
                                            value='Z'
                                        ),
                                    ], className='orbit-container'),
                                
                                
                            ], id='complex-orbit-container', className = 'save-container'),
                            html.Hr(),
                            html.Div([
                                html.P("Click for detailed help"),
                                html.Img(src=app.get_asset_url('help.png'), className = 'helpButton', id='orbit-help-button'),
                            ], className='help-button-container'),
                        ], className='tab-container')

                    ], className='custom-tab')
                    #####################################################################################################################
                
                ])
            ], className='pretty_container', id='all-tab-container'),

            # graphs
            html.Div([  # graph layout
                html.Div([  # tabs of graphs
                    dcc.Tabs(id="graph-custom-tabs", children=[
                        dcc.Tab(label='Battery', children=[
                            dcc.Graph(
                                id='battery_graph', className='graph-style', 
                                figure={
                                    'data': [],
                                    'layout': go.Layout(
                                        title='Battery Voltage & SOC',
                                        autosize=True,
                                        legend_orientation='h',
                                        legend=dict(x=0.2, y=-0.05),
                                        margin=dict(l=50, r=50, t=50, b=50),
                                        xaxis=dict(domain=[0.1, 0.9], title='Orbit Time (minutes)', position=0),
                                        yaxis=dict(
                                            title='V', titlefont=dict(
                                                color='rgb(255, 0, 0)'

                                            ),
                                            tickfont=dict(
                                                color='rgb(255, 0, 0)'
                                            )
                                        ),
                                        yaxis2=dict(
                                            title='%',
                                            titlefont=dict(
                                                color='rgb(0, 255, 100)'
                                            ),
                                            tickfont=dict(
                                                color='rgb(0, 255, 100)'
                                            ),
                                            overlaying='y',
                                            side='right'

                                        ),
                                        yaxis3=dict(title="Current (A)",
                                                    titlefont=dict(
                                                        color="rgb(0,0,255)"
                                                    ),
                                                    tickfont=dict(
                                                        color="rgb(0,0,255)"
                                                    ),
                                                    anchor="free",
                                                    overlaying="y",
                                                    side="left",
                                                    position=0.05),
                                        yaxis4=dict(title="Ahr",
                                                    titlefont=dict(
                                                        color="rgb(210,194,49)"
                                                    ),
                                                    tickfont=dict(
                                                        color="rgb(210,194,49)"
                                                    ),
                                                    anchor="free",
                                                    overlaying="y",
                                                    side="right",
                                                    position=0.95)
                                    )
                                }
                            )
                        ]),
                        dcc.Tab(label='Load', children=[
                            dcc.Graph(
                                id='load_graph', className='graph-style', 
                                figure={
                                    'data': [],
                                    'layout': go.Layout(
                                        title='Load Profile',
                                        legend_orientation='h',
                                        legend=dict(x=0.2, y=-0.04),
                                        margin=dict(l=50, r=50, t=50, b=75),
                                        xaxis=dict(domain=[0.1, 0.95], title='Orbit Time (minutes)'),
                                        yaxis=dict(
                                            title='V', titlefont=dict(
                                                color='rgb(255, 0, 0)'

                                            ),
                                            tickfont=dict(
                                                color='rgb(255, 0, 0)'
                                            )
                                        ),
                                        yaxis2=dict(
                                            title='Power (W)',
                                            titlefont=dict(
                                                color='rgb(0, 255, 100)'
                                            ),
                                            tickfont=dict(
                                                color='rgb(0, 255, 100)'
                                            ),
                                            overlaying='y',
                                            side='right',
                                            position=0.975

                                        ),
                                        yaxis3=dict(title="Current (A)",
                                                    titlefont=dict(
                                                        color="rgb(0,0,255)"
                                                    ),
                                                    tickfont=dict(
                                                        color="rgb(0,0,255)"
                                                    ),
                                                    anchor="free",
                                                    overlaying="y",
                                                    side="left",
                                                    position=0.04)
                                    )
                                }
                            )
                        ]),
                        dcc.Tab(label='Solar Array', children=[
                            dcc.Graph(
                                id='solar_graph', className='graph-style',
                                figure={
                                    'data': [],
                                'layout': go.Layout(
                                    title='Solar Array Profile',
                                    legend_orientation='h',
                                    legend=dict(x=0.2, y=-0.04),
                                    margin=dict(l=50, r=75, t=50, b=75),
                                    xaxis=dict(domain=[0.1, 1], title='Orbit Time (minutes)'),
                                    yaxis=dict(
                                        title='V', titlefont=dict(
                                            color='rgb(255, 0, 0)'

                                        ),
                                        tickfont=dict(
                                            color='rgb(255, 0, 0)'
                                        )
                                    ),
                                    yaxis2=dict(
                                        title='Power (W)',
                                        titlefont=dict(
                                            color='rgb(255, 0, 255)'
                                        ),
                                        tickfont=dict(
                                            color='rgb(255, 0, 255)'
                                        ),
                                        overlaying='y',
                                        side='right'

                                    ),
                                    yaxis3=dict(title="Current (A)",
                                                titlefont=dict(
                                                    color="rgb(0,0,255)"
                                                ),
                                                tickfont=dict(
                                                    color="rgb(0,0,255)"
                                                ),
                                                anchor="free",
                                                overlaying="y",
                                                side="left",
                                                position=0.04)
                                )
                                }
                            )
                        ]),
                        dcc.Tab(label='IV Curves', children=[
                            dcc.Graph(
                                id='solarIV_graph',
                                className='graph-style',
                                figure={
                        'data': [],
                        'layout': go.Layout(
                            title='Solar IV',
                            legend_orientation='h',
                            legend=dict(x=0.2, y=-0.08),
                            margin=dict(l=75, r=75, t=50, b=75),
                            xaxis=dict(domain=[0, 1], title=''),
                            yaxis=dict(
                                title='Current (A)', titlefont=dict(
                                    color='rgb(0,0,255)'

                                ),
                                tickfont=dict(
                                    color='rgb(0,0,255)'
                                )),
                            yaxis2=dict(
                                title='Power (W)', titlefont=dict(
                                    color='rgb(255,0,0)'

                                ),
                                tickfont=dict(
                                    color='rgb(255,0,0)'
                                ), overlaying='y',
                                side='right'
                            )
                        )

                    }
                            )
                        ])
                    ], vertical=True),
                ], id='graph-tab-container', className='pretty_container'),

                html.Div([  # system graph
                    dcc.Graph(
                        id='system_graph', className='graph-style',
                        style = {'width': '100%'},
                        figure={'data': [],
        'layout': go.Layout(
            title='Overall System',
            legend_orientation='h',
            legend=dict(x=0.2, y=-0.2),
            margin=dict(l=50, r=50, t=50, b=100),
            autosize=True,
            xaxis=dict(domain=[0.1, 0.90], title='Orbit Time (minutes)', position=0.1),
            yaxis=dict(
                title='V', titlefont=dict(
                    color='rgb(255, 0, 0)'

                ),
                tickfont=dict(
                    color='rgb(255, 0, 0)'
                )
            ),
            yaxis2=dict(
                title='%',
                titlefont=dict(
                    color='rgb(0, 255, 100)'
                ),
                tickfont=dict(
                    color='rgb(0, 255, 100)'
                ),
                overlaying='y',
                side='right'

            ),
            yaxis3=dict(title="Current (A)",
                        titlefont=dict(
                            color="rgb(0,0,255)"
                        ),
                        tickfont=dict(
                            color="rgb(0,0,255)"
                        ),
                        anchor="free",
                        overlaying="y",
                        side="left",
                        position=0.04),
            yaxis4=dict(title="Power (W)", titlefont=dict(
                color="rgb(255,0,255)"
            ),
                        tickfont=dict(
                            color="rgb(255,0,255)"
                        ),
                        anchor="free",
                        overlaying="y",
                        side="right",
                        position=0.98)
        )}
                    ),
                ], id='sys-graph', className='pretty_container'),
            ], className='block-display')

        ], className='flex-display'),

        # modal popouts for each tab section
        ####################################
        # help text will be populated with callbacks
        # general help
        html.Div([
            html.Div([html.Div(children=[
                html.Div([html.Button("X", id='close-general-popup', className='closeButton')], className = 'close-container'),
                html.H6("General Instructions"),
                html.Hr(),
                dcc.Markdown(['''
                ****Make sure to click the Update button after selecting a preset or uploading a file****

                __*Power topology:*__ Allows you to select a DET or PPT topology.

                __*Spinner model:*__ When chosen, you can build a multi-sided spinner spacecraft. Note that this option assumes a polygonal shape and a normal sun angle to the exposed side.
                
                __*Importing:*__ Select from any of the presets or upload your own custom file. Any file type can be uploaded to the custom file select. Each file type corresponds to a tab in the simulation. EOL Factors are only stored in the system files.
                
                '''
                ],className='modal-text'),
            ], className='modal-content'),
                
            ], className='popup-container')
        ], style={"display": 'none'}, className='modal', id='general-help-container'),
        # battery help
        html.Div([
            html.Div([html.Div(children=[
                html.Div([html.Button("X", id='close-battery-popup', className='closeButton')], className = 'close-container'),
                html.H6("Battery Instructions"),
                html.Hr(),
                dcc.Markdown(['''
                __*Initial SOC:*__ Allows you to specify a starting SOC for the simulation. 

                __*Capacity:*__ Specify battery capacity in Amp hours

                __*Cells in Series:*__ Specify number of cells in series for the battery. This simulation assumes that the charge/discharge curves you provide are for 8 cells in series.
                
                __*Max Charging Current/Voltage:*__ Given in Amps/Volts
                
                __*Internal Resistance:*__ Given in Ohms
                
                __*Charging/Discharging curves:*__ Upload battery charging curve data for 8 cells in series
                '''
                ],className='modal-text'),
            ], className='modal-content'),
            ], className='popup-container')
        ], style={"display": 'none'}, className='modal', id='battery-help-container'),
        # load help
        html.Div([
            html.Div([html.Div(children=[
                html.Div([html.Button("X", id='close-load-popup', className='closeButton')], className = 'close-container'),
                html.H6("Load Instructions"),
                html.Hr(),
                dcc.Markdown(['''
                __*Constant load:*__  Allows you to specify one load for the entire duration of the simulation.

                __*Custom load:*__  Upload your own load profile for the length of the simulation. If the given profile is shorter than the load, it will take the last given value for the rest of the simulation.
               
                __*Custom periodic load:*__  Same functionality as custom load. If the given profile is shorter than the load, it will go back to the start of the profile. (Loop until the simulation ends)
                '''
                ],className='modal-text'),
            ], className='modal-content'),
            ], className='popup-container')
        ], style={"display": 'none'}, className='modal', id='load-help-container'),
        # orbit help
        html.Div([
            html.Div([html.Div(children=[
                html.Div([html.Button("X", id='close-orbit-popup', className='closeButton')], className = 'close-container'),
                html.H6("Orbit Instructions"),
                html.Hr(),
                dcc.Markdown(['''
                __*Time Interval:*__ Specify the number of minutes between each time a point is generated. You can input decimal values to specify an interval less than one minute (input might be a little finicky, so use your arrow keys!).
                
                **Make sure this interval is smaller than the interval at which you specify load profile or sun angles in order to make full use of the given data.**

                __*LEO:*__ The simulation starts at the orbit’s noon point (middle of sun time). Changing the start time will change this starting position, i.e. If you had a 90 min orbit with a 40 min eclipse, you can adjust to start at the beginning of an eclipse by setting your start time at 25 mins.
                '''
                ],className='modal-text'),

                html.Img(src=app.get_asset_url('eclipse graphic.png'), width = '350px'),

                dcc.Markdown(['''
                __*L1/L2:*__ The specified eclipse time will occur relative to the given start and end times. It is a one time eclipse that does not occur periodically. 
                The distance factors used are: 
                * L1:(149.6/(148.11+2.5))**2
                * L2:(149.6/(151.1+2.5))**2
                '''
                ],className='modal-text'),
            ], className='modal-content'),
            ], className='popup-container')
        ], style={"display": 'none'}, className='modal', id='orbit-help-container'),
        # SA help
        html.Div([
            html.Div([html.Div(children=[
                html.Div([html.Button("X", id='close-solar-popup', className='closeButton')], className = 'close-container'),
                html.H6("Solar Array Instructions"),
                html.Hr(),
                dcc.Markdown(['''
                __*Num. of Wings:*__ Specify number of wings on spacecraft or sides on a spinning spacecraft

                __*Sun Angles:*__ Specify if you want to use a custom sun angle profile on top of the constant roll and pitch angles. 
                * __*For LEO:*__ Enter sun angles for each degree orbit angle (0 to 360)
                * __*For L1/L2:*__ Enter sun angles for one orbit starting from t=0. This corresponds to t=0 provided as the start time. Note that if you start your simulation at t=25, then the program will choose the sun angle at t=25 for calculation.
                
                __*BOL Factors:*__ These parameters were measured at 28C

                __*EOL Factors:*__ Specify EOL Factors for the mission. These will only be saved in the .system file, and not the individual .solar file. You have the option of enabling them or disabling them for calculations. 
                
                __*Solar Wings:*__ Each row of the table represents one wing. For the spinner model, the roll and pitch angles will not be used for calculation and are grayed out.
                '''
                ],className='modal-text'),
            ], className='modal-content'),
            ], className='popup-container')
        ], style={"display": 'none'}, className='modal', id='solar-help-container'),
        # Export Help
        html.Div([
            html.Div([html.Div(children=[
                html.Div([html.Button("X", id='close-export-popup', className='closeButton')], className = 'close-container'),
                html.H6("Export Instructions"),
                html.Hr(),
                dcc.Markdown(['''
                ****Press the Run button if no export options show up****

                __*Export Options:*__ Select which parts of the setup to capture and export in a config file. 

                __*Export Raw Data:*__ Exports each graph outputted as raw Excel data in different sheets
                '''
                ],className='modal-text'),
            ], className='modal-content'),
            ], className='popup-container')
        ], style={"display": 'none'}, className='modal', id='export-help-container'),
        ###################################################################################################################

    ], id='mainContainer')
