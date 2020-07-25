from dash.dependencies import Input, Output, State

def popupCallbacks(app):
    #popup callbakcs#######################################################################
    @app.callback(
        [Output('general-help-container', 'style')],
        [Input('close-general-popup','n_clicks'),Input('general-help-button','n_clicks')]
    )
    def open_popup(close, openClicks):
        if(close is None):
            close = 0
        if (openClicks is None):
            openClicks = 0

        if(openClicks > close):
            return[{"display":'block'}]
        else:
            return[{'display':'block',"visibility":'hidden'}]

    @app.callback(
        [Output('battery-help-container', 'style')],
        [Input('close-battery-popup','n_clicks'),Input('battery-help-button','n_clicks')]
    )
    def open_popup(close, openClicks):
        if(close is None):
            close = 0
        if (openClicks is None):
            openClicks = 0

        if(openClicks > close):
            return[{"display":'block'}]
        else:
            return[{'display':'block',"visibility":'hidden'}]

    @app.callback(
        [Output('load-help-container', 'style')],
        [Input('close-load-popup','n_clicks'),Input('load-help-button','n_clicks')]
    )
    def open_popup(close, openClicks):
        if(close is None):
            close = 0
        if (openClicks is None):
            openClicks = 0

        if(openClicks > close):
            return[{"display":'block'}]
        else:
            return[{'display':'block',"visibility":'hidden'}]

    @app.callback(
        [Output('orbit-help-container', 'style')],
        [Input('close-orbit-popup','n_clicks'),Input('orbit-help-button','n_clicks')]
    )
    def open_popup(close, openClicks):
        if(close is None):
            close = 0
        if (openClicks is None):
            openClicks = 0

        if(openClicks > close):
            return[{"display":'block'}]
        else:
            return[{'display':'block',"visibility":'hidden'}]

    @app.callback(
        [Output('solar-help-container', 'style')],
        [Input('close-solar-popup','n_clicks'),Input('solar-help-button','n_clicks')]
    )
    def open_popup(close, openClicks):
            if(close is None):
                close = 0
            if (openClicks is None):
                openClicks = 0

            if(openClicks > close):
                return[{"display":'block'}]
            else:
                return[{'display':'block',"visibility":'hidden'}]
    
    @app.callback(
        [Output('export-help-container', 'style')],
        [Input('close-export-popup','n_clicks'),Input('export-help-button','n_clicks')]
    )
    def open_popup(close, openClicks):
        if(close is None):
            close = 0
        if (openClicks is None):
            openClicks = 0

        if(openClicks > close):
            return[{"display":'block'}]
        else:
            return[{'display':'block',"visibility":'hidden'}]

