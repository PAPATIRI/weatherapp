from django.shortcuts import render

# todo api kode : http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=9CBA3349-C777-42CC-BC87-86791526BB68
# Create your views here.
def home(request):
    import json
    import requests

    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=9CBA3349-C777-42CC-BC87-86791526BB68")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "error"

    return render(request, 'home.html', {'api':api})


def about(request):
    return render(request, 'about.html', {})