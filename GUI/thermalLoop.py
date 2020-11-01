import sys
sys.path.append("/model/")
from thermalModel import *
import dash_html_components as html 
from dash.exceptions import PreventUpdate

from model.components.nodeSet import NodeSet
from model.components.orbit import Orbit
from model.components.orbitalBody import OrbitalBody
from model.components.orientation import Orientation
from model.components.solarPosition import SolarPosition
from model.components.spacecraftConfiguration import SpacecraftConfiguration
from model.components.timingConfiguration import TimingConfiguration

def thermalLoop(app):
    @app.callback(
        [Output('thermal-graph', 'figure')],
        [Input('run_button', 'n_clicks'),
        Input('num-nodes','value'),
        Input('node-table','data'),
        Input('node-table','columns'),
        Input('radiation-table','data'),
        Input('radiation-table','columns'),
        Input('conductance-table','data'),
        Input('conductance-table','columns'),
        Input('use-simple-orbit','value'),
        Input('orbit-type','value'),
        Input('start-time','value'),
        Input('end-time','value'),
        Input('timestep','value'),
        Input('period','value'),
        Input('eclipse-length','value'),
        Input('eclipse-start','value'),
        Input('eclipse-end','value'), #complex orbit
        Input('start-time-complex','value'),
        Input('end-time-complex','value'),
        Input('timestep-complex','value'),
        Input('spacecraft-config','value'),
        Input('inclination','value'),
        Input('right-ascension','value'),
        Input('periapsis','value'),
        Input('max-altitude','value'),
        Input('eccentricity','value'),
        Input('z-initial-orient','value'),
        Input('spacecraft-axis','value'),
        Input('additional-rotation','value'),
        Input('orbit-body-radius','value'),
        Input('grav-param','value'),
        Input('blackbody-temp','value'),
        Input('orbiting-albedo','value'),
        Input('solar-const-atm','value'),
        Input('right-ascension-sun','value'),
        Input('declination-sun','value')]
    )
def thermalLooping(clicks, num-nodes, node-table-rows, node-table-cols, radiation-table-rows, radiation-table-cols, conductance-table-rows,
         conductance-table-cols, use-simple-orbit, orbit-type, start-time, end-time, timestep, period, eclipse-length, eclipse-start, 
         eclipse-end, start-time-complex, end-time-complex, timestep-complex, spacecraft-config, inclination, right-ascension, periapsis, 
         max-altitude, eccentricity, z-initial-orient, spacecraft-axis, additional-rotation, orbit-body-radius, grav-param, blackbody-temp,
         orbiting-albedo, solar-const-atm, right-ascension-sun, declination-sun):
    print('yeah im getting there')

    #TODO: Create all object properties reading in GUI values
    # Create Thermal Model object, output nodeTemperatures array
    # Graph array in GUI

    thermalModel = ThermalModel()
    raise PreventUpdate