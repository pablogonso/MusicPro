import json
from math import ceil

import requests
from django.http import JsonResponse

URL = 'https://v6.exchangerate-api.com/v6/534569873736672ef33d04ea/latest/USD'


def usd_to_clp(usd):
    response = requests.get(URL)
    return usd * json.loads(response.content)['conversion_rates']['CLP']


def dollar(request, usd=1):
    clp = usd_to_clp(usd)
    data = {
        'clp': ceil(clp),
    }
    if 'display' in request.GET:
        data['display'] = '${:,.0f}'.format(clp)
    return JsonResponse(data)
