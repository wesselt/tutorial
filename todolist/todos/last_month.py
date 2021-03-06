# Include the `fusioncharts.py` file that contains functions to embed the charts.
from .fusioncharts import FusionCharts

from .models import FeedBack


# The `chart` function is defined to generate Column 2D chart from database.
def chart(request):
    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Monthly Feedback" + request.user.first_name,
        "subCaption": "Harry's SuperMart",
        "xAxisName": "Date",
        "yAxisName": "Mood",
        "numberPrefix": "$",
        "paletteColors": "#0075c2",
        "bgColor": "#ffffff",
        "borderAlpha": "0",
        "canvasBorderAlpha": "0",
        "usePlotGradientColor": "0",
        "plotBorderAlpha": "10",
        "placevaluesInside": "1",
        "rotatevalues": "1",
        "valueFontColor": "#ffffff",
        "showXAxisLine": "1",
        "xAxisLineColor": "#999999",
        "divlineColor": "#999999",
        "divLineIsDashed": "1",
        "showAlternateHGridColor": "0",
        "subcaptionFontBold": "0",
        "subcaptionFontSize": "14"
    }

    # The data for the chart should be in an array where each element of the array is a JSON object
    # having the `label` and `value` as key value pair.

    dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in FeedBack.objects.filter(user=request.user):
        data = {}
        data['label'] = key.date_first.strftime("%Y-%m-%d")
        data['value'] = key.mood_choices
        dataSource['data'].append(data)

        # Create an object for the Column 2D chart using the FusionCharts class constructor
    column2D = FusionCharts("column2D", "ex2", "600", "350", "fietswiel", "json", dataSource)
    return column2D.render()
