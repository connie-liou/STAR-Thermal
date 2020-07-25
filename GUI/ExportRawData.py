import sys
sys.path.append("/classes/") 
import pandas as pd
from flask import stream_with_context, request
from werkzeug.wrappers import Response
import json
from io import BytesIO

'''
When the user goes to /exportrawdata the function will extract the value query key and generate an excel file containing all raw data in columns
'''
def exportRawData(server):
    @server.route('/exportrawdata')
    @stream_with_context
    def exportRawData():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        #Extract json from value query key
        excelDict = json.loads(request.args.get('value'))
        #Convert json into pandas dataframes and then convert them to excel sheets
        pd.read_json(excelDict['battery']).to_excel(writer, sheet_name='Battery')
        pd.read_json(excelDict['load']).to_excel(writer, sheet_name='Load')
        pd.read_json(excelDict['solar']).to_excel(writer, sheet_name='Solar')

        for s in excelDict:
            if "IV" in s:
                pd.read_json(excelDict[s]).to_excel(writer, sheet_name=s)
        #Build excel file
        writer.save()
        output.seek(0)

        # stream the response as the data is generated
        response = Response(output.read(), mimetype='application/xlsx')
        # add a filename
        response.headers.set("Content-Disposition", "attachment", filename="raw_data.xlsx")
        #send to user for downloading
        return response

def generateJSON(batt, array):
    # Export Battery to excel
    raw_data_Battery = {
        "Time": batt.timeList,
        "Voltage": batt.batteryVoltageList,
        "Current": batt.currentList,
        "SOC": batt.stateOfCharge
    }

    # Export Load to excel
    raw_data_Load = {
        "Time": batt.timeList,
        "Power": batt.loadPowerList,
        "Voltage": batt.loadVList,
        "Current": batt.loadCurrentList
    }

    # Solar Array
    raw_data_SolarArray = {
        "Time": batt.timeList,
        "Array Power": batt.solarP,
        "Array Voltage": batt.solarV,
        "Array Current": batt.solarI
    }

    raw_data_SolarArrayIV = {
        "Voltage": array.voltageIVList,
        "Array Power": array.powerIVList,
        "Array Current": array.currentIVList
    }
    rawData = {}
    rawData['Array IV'] = pd.DataFrame(data=raw_data_SolarArrayIV).to_json()
    wingIV = {}
    for x in range(len(array.wingList)):
        index = "Wing " + str(x + 1)
        raw_data_SolarArray[index + " Current"] = batt.wingListI[x]

        wingIV[index + " Voltage"] = array.wingList[
            x].voltageIVList
        wingIV[index + " Power"] = array.wingList[
            x].powerIVList
        wingIV[index + " Current"] = array.wingList[
            x].currentIVList

        rawData[index + ' IV'] = pd.DataFrame(data=wingIV).to_json()
        wingIV = {}

    rawData['battery'] = pd.DataFrame(data=raw_data_Battery).to_json()
    rawData['solar'] = pd.DataFrame(data=raw_data_SolarArray).to_json()
    rawData['load'] = pd.DataFrame(data=raw_data_Load).to_json()

    return rawData