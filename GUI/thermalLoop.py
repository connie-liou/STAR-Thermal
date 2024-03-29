import sys

from pandas.tests.test_downstream import df

sys.path.append("/model/")
from dash.dependencies import *
import plotly.express as px
import dash_core_components as dcc

import pandas as pd


def thermalLoop(app):
    @app.callback(
        Output('thermal-graph', 'figure'),
        [Input('run_button', 'n_clicks'),
         Input('num-nodes', 'value'),
         Input('node-table', 'data'),
         Input('node-table', 'columns'),
         Input('radiation-table', 'data'),
         Input('radiation-table', 'columns'),
         Input('conductance-table', 'data'),
         Input('conductance-table', 'columns'),
         Input('use-simple-orbit', 'value'),
         Input('orbit-type', 'value'),
         Input('start-time', 'value'),
         Input('end-time', 'value'),
         Input('timestep', 'value'),
         Input('period', 'value'),
         Input('eclipse-length', 'value'),
         Input('eclipse-start', 'value'),
         Input('eclipse-end', 'value'),  # complex orbit
         Input('start-time-complex', 'value'),
         Input('end-time-complex', 'value'),
         Input('timestep-complex', 'value'),
         Input('spacecraft-config', 'value'),
         Input('inclination', 'value'),
         Input('right-ascension', 'value'),
         Input('periapsis', 'value'),
         Input('max-altitude', 'value'),
         Input('eccentricity', 'value'),
         Input('z-initial-orient', 'value'),
         Input('spacecraft-axis', 'value'),
         Input('additional-rotation', 'value'),
         Input('orbit-body-radius', 'value'),
         Input('grav-param', 'value'),
         Input('blackbody-temp', 'value'),
         Input('orbiting-albedo', 'value'),
         Input('solar-const-atm', 'value'),
         Input('right-ascension-sun', 'value'),
         Input('declination-sun', 'value')]
    )
    def thermalLooping(clicks, num_nodes, node_table_rows, node_table_cols, radiation_table_rows, radiation_table_cols,
                       conductance_table_rows,
                       conductance_table_cols, use_simple_orbit, orbit_type, start_time, end_time, timestep, period,
                       eclipse_length, eclipse_start,
                       eclipse_end, start_time_complex, end_time_complex, timestep_complex, spacecraft_config,
                       inclination, right_ascension, periapsis,
                       max_altitude, eccentricity, z_initial_orient, spacecraft_axis, additional_rotation,
                       orbit_body_radius, grav_param, blackbody_temp,
                       orbiting_albedo, solar_const_atm, right_ascension_sun, declination_sun):
        print('In thermalLoop')
        df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')

        available_indicators = df['Indicator Name'].unique()

        fig = px.scatter(df, x="Year", y="Value")

        fig.update_layout(transition_duration=500)

        return fig

        # # TODO: Using user input values
        # # Create Thermal Model object, output nodeTemperatures array
        # # Graph array in GUI
        #
        # solarPosition = SolarPosition(right_ascension, declination_sun)
        # orbit = Orbit(inclination,rightAscensionOfAscendingNode,argumentOfPeriapsis,maxAltitude,eccentricity,EARTH_ORBITAL_BODY)
        # timingconfiguration = TimingConfiguration(endtime,timestep)
        # thermalModel = ThermalModel()
        # raise PreventUpdate
