from rest_framework.decorators import api_view
import requests
import json, time
from .models import Request

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@api_view()
def api(request):
    headers = {
        'Content-Type': 'application/json'
    }
    url = "https://sandbox.plaid.com/institutions/get"
    payload = {
        "client_id": "6211eba26ab5e2001a0f6efd",
        "secret": "617edd2eb4bce4e23235c6b4c78e47",
        "count": 2,
        "offset": 5,
        "country_codes": ["us"]
    }

    start_time = time.time() 
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    execution_time = int((time.time() - start_time)*1000)    

    request_log = Request(
        endpoint = request.get_full_path(),
        response_code = response.status_code,
        method = request.method,
        remote_address = get_client_ip(request),
        exec_time = execution_time,
        response = json.loads(response.content),
        request = str(request.body),
    )
    request_log.save() 
    return response