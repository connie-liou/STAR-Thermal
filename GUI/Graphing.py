import sys
sys.path.append("/model/")
from thermalModel import *
import time
import plotly.graph_objs as go
'''
Returns blank graphs for when the program initially starts
'''


'''
These functions extract data from battery and solar array to generate the graph data and layouts
'''
def batteryGraph(thermalModel):

    tempData = go.Scatter(
        x=     ,
        y=     ,
        name='temperature',
        mode='lines', line=dict(color='rgb(255,0,0)')
    )
    return {
        'data': [tempData],
        'layout': go.Layout(
            title='Temperature',
            legend_orientation='h',
            autosize=True,
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
            )
    }
