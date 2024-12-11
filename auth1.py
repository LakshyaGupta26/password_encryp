import requests

def get_ip():
    ip_data = requests.get('https://api.ipify.org?format=json').json()
    return ip_data["ip"]
