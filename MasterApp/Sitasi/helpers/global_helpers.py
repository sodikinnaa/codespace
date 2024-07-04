import requests
import random
def getData(url):    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        data = data['payload']['data']
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the data: {e}")
        return None

import json

def dd(variable):
    print(json.dumps(variable, indent=4, ensure_ascii=False))

def postData(url, data):
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Check if the request was successful
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error posting the data: {e}")
        return None
    
def putData(url, data):
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.put(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Check if the request was successful
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error posting the data: {e}")
        return None

def send_data_to_endpoint(data):
    endpoint_url = "https://media.datadebasa.com/api/v1.0/dosen/"  # URL endpoint untuk update professor
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.put(endpoint_url + f"/{data['id_sitasi_dosen']}", json=data, headers=headers)
        if response.status_code == 200:
            print("Data berhasil dikirim ke endpoint.")
        else:
            print("Gagal mengirim data. Status code:", response.status_code)
    except Exception as e:
        print("Error saat mengirim data ke endpoint:", e)
        
        
        
def get_fake_user_agent():
    fake_user_agents = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Windows; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
        "Mozilla/5.0 (Windows NT 10.0; Windows; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Windows; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36",
        # Tambahkan user agent lainnya jika diperlukan:
    ]
    return random.choice(fake_user_agents)
