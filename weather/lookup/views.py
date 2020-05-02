from django.shortcuts import render

# todo api kode : http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=9CBA3349-C777-42CC-BC87-86791526BB68
# Create your views here.


def home(request):
    import json
    import requests

    api_request = requests.get(
        "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=9CBA3349-C777-42CC-BC87-86791526BB68")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "error"

    if api[0]['Category']['Name'] == "Good":
        category_description = "( 0 - 50 ) kualitas udara baik dan polusi udara yang ada pada tempat di atas hanya sedikit atau tidak beresiko"
        category_color = "good"
    elif api[0]['Category']['Name'] == 'Moderate':
        category_description = '( 51 - 100 ) kualitas udara masih bisa diterima, untuk beberapa orang yang tidak terbiasa atau sensitif terhadap polusi udara mungkin akan menyebabkan gejala kesehatan'
        category_color = 'moderate'
    elif api[0]['Category']['Name'] == 'Unhealthy for Sensitive Groups':
        category_description = '( 101 - 150 )meski secara umum aktifitas umum tidak terganggu dengan keadaan udara ini tapi untuk orang tua, penderita penyakit paru-paru , dan anak-anak memiliki resiko buruk yang tinggi dari dampak udara'
        category_color = 'sensitive'
    elif api[0]['Category']['Name'] == 'Unhealthy':
        category_description = '( 151 - 200 ) setiap orang mungkin kesehatannya sudah terganggu dan orang yang sensitif terhadap udara kotor mungkin akan mendapat efek yang lebig serius'
        category_color = 'unhealthy'
    elif api[0]['Category']['Name'] == 'Very Unhealthy':
        category_description = '( 201 - 300 )bahaya pada kesehatan, semua orang akan terkena penyakit yang lebih serius'
        category_color = 'veryunhealthy'
    elif api[0]['Category']['Name'] == 'Hazardous':
        category_description = '( 301 - 500 )peringatan pada kondisi darurat kesehatan, semua penduduk pasti terkena dampaknya yang sangat parah'
        category_color = 'hazardous'

    return render(request, 'home.html', {'api': api,
                                         'category_description': category_description,
                                         'category_color': category_color})


def about(request):
    return render(request, 'about.html', {})
