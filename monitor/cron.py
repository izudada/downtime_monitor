import requests
from .models import WebLog, Website


def get_web_status():
    all_websites = Website.objects.all()
    for website in all_websites:
        response = requests.get(website.url)
        if response.status_code != 200 and website.state == False:
            pass