import requests
from django.http import JsonResponse


def convert_currency(request):
    amount = float(request.GET.get('amount', 0))

    # Realiza la lógica de la conversión utilizando la API de la carpeta "usd-clp-api-master"
    # Puedes importar los módulos necesarios y utilizar las funciones proporcionadas por la API

    # Ejemplo de respuesta JSON con los resultados
    result = {
        'amount': amount,
        'converted_amount': converted_amount,
        'currency': currency,
    }

    return JsonResponse(result)
