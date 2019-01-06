import requests
from django.conf import settings


def get_api_data(year=None):
    api_url = "https://apis.sktelecom.com/v1/eventday/days?type=h&year="

    if year:
        api_url += str(year)

    headers = {
        'Content-Type': 'application/json',
        "TDCProjectKey": settings.SKT_API_KEY,
    }

    res = requests.get(api_url, headers=headers)

    data = res.json()

    return data