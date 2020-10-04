import sys
sys.path.append("/model/")
from thermalModel import *
import dash_html_components as html 

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
def thermalLooping(clicks,):
    print('yeah im getting there')