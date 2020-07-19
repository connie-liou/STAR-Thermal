import sys
sys.path.append("/classes/")
from classes.Battery import *
from classes.Solar import *
import time
import plotly.graph_objs as go
'''
Returns blank graphs for when the program initially starts
'''


'''
These functions extract data from battery and solar array to generate the graph data and layouts
'''
def batteryGraph(batt: Battery):

    bV = go.Scatter(
        x=batt.timeList,
        y=batt.batteryVoltageList,
        name='Voltage (V)',
        mode='lines', line=dict(color='rgb(255,0,0)')
    )
    ahrChange = go.Scatter(
        x=batt.timeList,
        y=batt.ahrchangeList,
        name='Ahr Change',
        mode='lines', line=dict(color='rgb(210,194,49)'),
        yaxis='y4'
    )
    SOC = go.Scatter(
        x=batt.timeList,
        y=batt.stateOfCharge,
        name='SOC',
        yaxis='y2',
        mode='lines', line=dict(color='rgb(0, 255, 100)')
    )
    current = go.Scatter(
        x=batt.timeList,
        y=batt.currentList,
        name='Current (A)',
        yaxis='y3',
        mode='lines', line=dict(color='rgb(0,0,255)')
    )

    return {
        'data': [
            bV, SOC, current, ahrChange
        ],
        'layout': go.Layout(
            title='Battery Voltage & SOC',
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


def loadProfileGraph(batt: Battery):

    power = go.Scatter(
        x=batt.timeList,
        y=batt.loadPowerList,
        name='Power (W)',
        yaxis='y2',
        mode='lines', line=dict(color='rgb(0, 255, 100)')
    )
    lc = go.Scatter(
        x=batt.timeList,
        y=batt.loadCurrentList,
        name='Load Current (A)',
        yaxis='y3',
        mode='lines', line=dict(color='rgb(0, 0, 255)')
    )
    lv = go.Scatter(
        x=batt.timeList,
        y=batt.loadVList,
        name='Load Voltage (V)',
        mode='lines', line=dict(color='rgb(255,0,0)')
    )

    return {
        'data': [
            lv, power, lc
        ],
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


def solarOverTime(batt: Battery):

    sP = go.Scatter(
        x=batt.timeList,
        y=batt.solarP,
        name='Power (W)',
        yaxis='y2',
        mode='lines', line=dict(color='rgb(255,0,255)')
    )
    sI = go.Scatter(
        x=batt.timeList,
        y=batt.solarI,
        name='Current (A)',
        yaxis='y3',
        mode='lines', line=dict(color='rgb(0, 0, 255)')
    )
    sV = go.Scatter(
        x=batt.timeList,
        y=batt.solarV,
        name='Voltage (V)',
        mode='lines', line=dict(color='rgb(255,0,0)')
    )
    dataList = []
    wingNumber = 1
    for i in range (len(batt.solarArray.wingList)):
        solarI = go.Scatter(
            x=batt.timeList,
            y=batt.wingListI[i],
            name='Solar Wing ' + str(wingNumber) + ' Current',
            legendgroup=str(wingNumber),
            yaxis='y3',
            mode='lines', line=dict(dash='dash' ,color='rgb(0,0,255)')
        )

        dataList.append(solarI)
        wingNumber = wingNumber + 1
    dataList.append(sV)
    dataList.append(sP)
    dataList.append(sI)
    end = time.time()
    # print("Solar Graph Time = " + str(end - start))
    return {
        'data': dataList,
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


def systemGraph(batt: Battery):
    # Battery Data

    bV = go.Scatter(
        x=batt.timeList,
        y=batt.batteryVoltageList,
        name='Battery Voltage (V)',
        mode='lines', line=dict(color='rgb(255,0,0)')
    )
    SOC = go.Scatter(
        x=batt.timeList,
        y=batt.stateOfCharge,
        name='Battery SOC',
        yaxis='y2',
        mode='lines', line=dict(color='rgb(0, 255, 100)')
    )
    current = go.Scatter(
        x=batt.timeList,
        y=batt.currentList,
        name='Battery Current (A)',
        yaxis='y3',
        mode='lines', line=dict(color='rgb(0,0,255)')
    )


    sP = go.Scatter(
        x=batt.timeList,
        y=batt.solarP,
        name='Solar Array Power (W)',
        yaxis='y4',
        mode='lines', line=dict(dash='dash', color='rgb(255,0,255)')
    )
    sI = go.Scatter(
        x=batt.timeList,
        y=batt.solarI,
        name='Solar Array Current (A)',
        yaxis='y3',
        mode='lines', line=dict(dash='dash', color='rgb(0, 0, 255)')
    )
    sV = go.Scatter(
        x=batt.timeList,
        y=batt.solarV,
        name='Solar Array Voltage (V)',
        mode='lines', line=dict(dash='dash', color='rgb(255,0,0)')
    )



    power = go.Scatter(
        x=batt.timeList,
        y=batt.loadPowerList,
        name='Load Power (W)',
        yaxis='y4',
        mode='lines', line=dict(dash='dot', color='rgb(255, 0, 255)')
    )
    lc = go.Scatter(
        x=batt.timeList,
        y=batt.loadCurrentList,
        name='Load Current (A)',
        yaxis='y3',
        mode='lines', line=dict(dash='dot', color='rgb(0, 0, 255)')
    )
    lv = go.Scatter(
        x=batt.timeList,
        y=batt.loadVList,
        name='Load Voltage (V)',
        mode='lines', line=dict(dash='dot', color='rgb(255,0,0)')
    )

    return {
        'data': [bV, SOC, current, sP, sI, sV, power, lc, lv],
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
        )
    }


def solarIV(solarArray: SolarArray, battery: Battery):
    dataList = []

    maxV = go.Scatter(
        x=[battery.MAX_VOLTAGE_REACHED],
        y=[solarArray.calculateCurrentIVCurve(battery.MAX_VOLTAGE_REACHED)],
        mode="markers+text",
        name="Max Voltage",
        text=["Max Solar Array Voltage"],
        textposition="top center",
        legendgroup='array',
        showlegend=False
    )
    dataList.append(maxV)

    solarAP = go.Scatter(
        x=solarArray.voltageIVList,
        y=solarArray.powerIVList,
        name='Solar Array Power',
        yaxis='y2',
        legendgroup='array',
        mode='lines', line=dict(dash='dash', color='rgb(255,0,0)')
    )
    dataList.append(solarAP)
    solarAI = go.Scatter(
        x=solarArray.voltageIVList,
        y=solarArray.currentIVList,
        name='Solar Array Current',
        legendgroup='array',
        mode='lines', line=dict(dash='dash', color='rgb(0,0,255)')
    )
    dataList.append(solarAI)
    wingNumber = 1
    for wing in solarArray.wingList:
        solarP = go.Scatter(
            x=wing.voltageIVList,
            y=wing.powerIVList,
            name='Solar Wing ' + str(wingNumber) + ' Power',
            yaxis='y2',
            legendgroup=str(wingNumber),
            mode='lines', line=dict(color='rgb(255,0,0)')
        )

        solarI = go.Scatter(
            x=wing.voltageIVList,
            y=wing.currentIVList,
            name='Solar Wing ' + str(wingNumber) + ' Current',
            legendgroup=str(wingNumber),
            mode='lines', line=dict(color='rgb(0,0,255)')
        )
        maxV = go.Scatter(
            x=[battery.MAX_VOLTAGE_REACHED],
            y=[wing.calculateCurrentIVCurve(battery.MAX_VOLTAGE_REACHED)],
            mode="markers+text",
            name="Max Voltage",
            text=["Max Solar Wing " + str(wingNumber) + " Voltage"],
            textposition="top center",
            legendgroup=str(wingNumber),
            showlegend=False
        )
        dataList.append(solarP)
        dataList.append(solarI)
        dataList.append(maxV)
        wingNumber = wingNumber + 1

    return {
        'data': dataList,
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