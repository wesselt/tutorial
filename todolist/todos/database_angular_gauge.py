from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from .fusioncharts import FusionCharts


# Loading Data from a Static JSON String
# It is a example to show a Pie 3D chart where data is passed as JSON string format.
# The `chart` method is defined to load chart data from an JSON string.

def chart(request):
    # Create an object for the Line chart using the FusionCharts class constructor
    user = request.user.first_name + " " + request.user.last_name
    latest_mood = request.user.feedback_set.latest('date_first')
    mood = latest_mood.mood_choices / 5 * 100
    angularChart = FusionCharts("angulargauge", "ex1", "300", "200", "chart-1", "json",
                                # The chart data is passed as a string to the `dataSource` parameter.
                                """{
                                    "chart": {
                                        "caption": "Mood of """ + user + """",
                                        "lowerlimit": "0",
                                        "upperlimit": "100",
                                        "lowerlimitdisplay": "Bad",
                                        "upperlimitdisplay": "Good",
                                        "palette": "1",
                                        "numbersuffix": "%",
                                        "tickvaluedistance": "10",
                                        "showvalue": "0",
                                        "gaugeinnerradius": "0",
                                        "bgcolor": "FFFFFF",
                                        "pivotfillcolor": "333333",
                                        "pivotradius": "8",
                                        "pivotfillmix": "333333, 333333",
                                        "pivotfilltype": "radial",
                                        "pivotfillratio": "0,100",
                                        "showtickvalues": "1",
                                        "showborder": "0"
                                    },
                                    "colorrange": {
                                        "color": [
                                            {
                                                "minvalue": "0",
                                                "maxvalue": "40",
                                                "code": "e44a00"
                                            },
                                            {
                                                "minvalue": "40",
                                                "maxvalue": "80",
                                                "code": "f8bd19"
                                            },
                                            {
                                                "minvalue": "80",
                                                "maxvalue": "100",
                                                "code": "6baa01"
                                            }
                                        ]
                                    },
                                    "dials": {
                                        "dial": [
                                            {
                                                "value": " """ + str(mood) + """",
                                                "rearextension": "15",
                                                "radius": "100",
                                                "bgcolor": "333333",
                                                "bordercolor": "333333",
                                                "basewidth": "8"
                                            }
                                        ]
                                    }
                                }""")

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return angularChart.render()
