import sys
sys.path.append("/classes/")
from flask import stream_with_context, request
from werkzeug.wrappers import Response
import json

'''
Gathers json string from value query key and converts it to a custom file type and sends it to the user for downloading
'''

def exportToJSON(server):
    @server.route('/exporttojson')
    @stream_with_context
    def exportJSON():
        #Exract json from value query key
        out = request.args.get('value')
        #Convert json to dict to get filename
        outDict = json.loads(out)

        # stream the response as the data is generated
        response = Response(out, mimetype='application/json')
        # add a filename
        response.headers.set("Content-Disposition", "attachment", filename=outDict["fileName"])
        #Send to user for downloading
        return response



