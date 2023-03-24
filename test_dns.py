import socket
import requests
import json

domains = []

def verifica_dns(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return None

def verifica_status(url):
    try:
        res = requests.get(url, timeout=5)
        return res.status_code
    except requests.exceptions.RequestException:
        return None

results = []

for domain in domains:
    result = {'domain': domain}
    ip = verifica_dns(domain)

    if ip:
        result['ip'] = ip
        url = f'http://{domain}'
        status_code = verifica_status(url)

        if status_code:
            result['url'] = url
            result['status_code'] = status_code
        else:
            result['erro'] = f'nao foi possivel se conectar ao link {url}'
    else:
        result['erro'] = 'link nao esta resolvendo'

    results.append(result)
    
with open('logs.json', 'w') as f:
    json.dump(results, f, indent=2)
