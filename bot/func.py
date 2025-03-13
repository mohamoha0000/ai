import random
import re
import requests
import json
import http.client
from urllib.parse import urlparse
import socket
access_token = 'EAAVye6i2In8BOwpyXE22pJWeZAlvK5bkXzgwgIHBBiIqOmfOlFEPoGuTutHhwZAZAwb996XbiW2RJrMCaY2Nxgd5L1apTMQykfdWRwfNLpyYRIonZCxkZCi9WKe9jAWzDMZAQy5ZAfmhE2qpulFDZAoWJh6X6mrPgzNZBOEuxDy4XNn3V1dT7lwMQgXb7tslnF4OO'
phone_number_id = '378648901991253'
base_url = 'https://graph.facebook.com/v19.0'
def generate_user_agent():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    aa = 'Mozilla/5.0 (Linux; Android 9; Nokia C2 Build/PPR1.180610.011; wv)'
    b = random.randint(6, 12)
    c = 'Android 9; Nokia C2 Build/'
    d = random.choice(letters)
    e = random.randint(1, 999)
    f = random.choice(letters)
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79'
    h = random.randint(73, 100)
    i = 0
    j = random.randint(4200, 4900)
    k = random.randint(40, 150)
    l = 'Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/297.0.0.13.113;]'
    full_agent = f"{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}"
    return full_agent

def hs():
    user_agent = generate_user_agent()

    headers = {
        'User-Agent': user_agent
    }

    response = requests.get('https://www.hespress.com/all', headers=headers)

    if response.status_code != 200:
        return []

    html_text = response.text
    img_regex = r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]+)"'
    matches = re.findall(img_regex, html_text)

    return matches

def sendi(phone_number, image_url, caption):
    base_url = 'https://graph.facebook.com/v19.0'
    phone_number_id = '378648901991253'
    access_token = 'EAAVye6i2In8BOwpyXE22pJWeZAlvK5bkXzgwgIHBBiIqOmfOlFEPoGuTutHhwZAZAwb996XbiW2RJrMCaY2Nxgd5L1apTMQykfdWRwfNLpyYRIonZCxkZCi9WKe9jAWzDMZAQy5ZAfmhE2qpulFDZAoWJh6X6mrPgzNZBOEuxDy4XNn3V1dT7lwMQgXb7tslnF4OO'
    url = f"{base_url}/{phone_number_id}/messages"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "image",
        "image": {
            "link": image_url,
            "caption": caption
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        return 200
    else:
        return response.status_code
def getsize(url,prox):
    socket.setdefaulttimeout(3)
    prox=prox.strip()
    prox=prox.split(":")
    proxy_host = prox[1].split("//")[1]
    proxy_port = prox[-1]
    parsed_url = urlparse(url)
    conn = http.client.HTTPConnection(proxy_host, proxy_port)
    conn.set_tunnel(parsed_url.netloc)
    headers = {
    'User-Agent':generate_user_agent(),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    }
    try:
        conn.request('HEAD', parsed_url.path + '?' + parsed_url.query, headers=headers)
        response = conn.getresponse()
        print(response.status)
    except:
        conn.close()
        return proxy_host, proxy_port
    if response.status ==302:
        new_location = response.getheader('Location')
        print(new_location)
        parsed_new_location = urlparse(new_location)
        conn = http.client.HTTPSConnection(parsed_new_location.netloc)
        conn.request('HEAD', parsed_new_location.path + '?' + parsed_new_location.query, headers=headers)
        response = conn.getresponse()
    print(response.status)
    if response.status == 200:
        file_size_bytes = int(response.getheader('Content-Length', 0))
        conn.close()
        return file_size_bytes / (1024 * 1024),new_location
    else:
        conn.close()
        return None

def sendf2(phone_number,url):
    video_url = url

    url = f"{base_url}/{phone_number_id}/messages"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    payload = {
    "messaging_product": "whatsapp",
    "to": phone_number,
    "type": "document",
    "document": {
        "link": video_url,
        "filename":"bot"
    }
}

    response = requests.post(url, headers=headers, data=json.dumps(payload))
def send_message(phone_number, message):
    url = f"{base_url}/{phone_number_id}/messages"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "text",
        "text": {
            "body": message
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))

