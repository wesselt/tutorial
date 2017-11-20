# Include the `fusioncharts.py` file that contains functions to embed the charts.
from .fusioncharts import FusionCharts

from .models import FeedBack


# The `chart` function is defined to generate Column 2D chart from database.
def chart(request):
    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Personal mood trend",
        "subCaption": request.user.first_name + " " + request.user.last_name,
        "xAxisName": "Date",
        "yAxisName": "Mood in numbers",
        "numberPrefix": "Mood ",
        "paletteColors": "#0075c2",
        "bgColor": "#ffffff",
        "showBorder": "0",
        "showCanvasBorder": "0",
        "plotBorderAlpha": "10",
        "usePlotGradientColor": "0",
        "plotFillAlpha": "50",
        "showXAxisLine": "1",
        "axisLineAlpha": "25",
        "divLineAlpha": "10",
        "showValues": "1",
        "showAlternateHGridColor": "0",
        "captionFontSize": " 14",
        "subcaptionFontSize": "14",
        "subcaptionFontBold": "0",
        "toolTipColor": "#ffffff",
        "toolTipBorderThickness": "0",
        "toolTipBgColor": "#000000",
        "toolTipBgAlpha": "80",
        "toolTipBorderRadius": "1",
        "toolTipPadding": "0"
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
    column2D = FusionCharts("area2D", "ex2", "600", "350", "fietswiel", "json", dataSource)
    return column2D.render()
