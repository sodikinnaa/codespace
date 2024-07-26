import requests
import random


def getData(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        data = data["payload"]["data"]
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the data: {e}")
        return None


import json


def dd(variable):
    print(json.dumps(variable, indent=4, ensure_ascii=False))


def postData(url, data):
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(
            url, headers=headers, verify=False, data=json.dumps(data)
        )
        response.raise_for_status()  # Check if the request was successful
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error posting the data: {e}")
        return None


def putData(url, data):
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.put(
            url, headers=headers, verify=False, data=json.dumps(data)
        )
        response.raise_for_status()  # Check if the request was successful
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error posting the data: {e}")
        return None


def send_data_to_endpoint(data):
    endpoint_url = "https://media.datadebasa.com/api/v1.0/dosen/"  # URL endpoint untuk update professor
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.put(
            endpoint_url + f"/{data['id_sitasi_dosen']}",
            json=data,
            headers=headers,
            verify=False,
        )
        if response.status_code == 200:
            print("Data berhasil dikirim ke endpoint.")
        else:
            print("Gagal mengirim data. Status code:", response.status_code)
    except Exception as e:
        print("Error saat mengirim data ke endpoint:", e)


def send_data_array(data):
    # dd(data)
    # for dosen in data['dosen']:
    #     dd(dosen['id_sitasi_dosen'])
    endpoint_url = "https://media.datadebasa.com/api/v1.0/Arrdosen"  # URL endpoint untuk update professor
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.put(endpoint_url, json=data, headers=headers, verify=False)
        if response.status_code == 200:
            response.raise_for_status()  # Check if the request was successful
            datas = response.json()
            # dd(datas)
            print("Data berhasil dikirim ke endpoint. dengan data", datas)
        else:
            print("Gagal mengirim data. Status code:", response.status_code)
            print("Response content:", response.content.decode())
    except Exception as e:
        print("Error saat mengirim data ke endpoint:", e)

    return data


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


# update data by array
def fake_autor(data, hasil):
    data = {
        "dosen": [
            {
                "id_sitasi_dosen": "meong.ac.id-002",
                "nama_dosen": "Rizki Yuliandra, M.Pd",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=1BSEYXIAAAAJ",
                "email_verified": "Verified email at meong.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia",
                "total_sitasi": "9301",
                "id_sitasi_kampus": "meong.ac.id",
            },
            {
                "id_sitasi_dosen": "meong.ac.id-003",
                "nama_dosen": "Rachmi Marsheilla Aguss",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=aZnAoQQAAAAJ",
                "email_verified": "Verified email at meong.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia",
                "total_sitasi": "9279",
                "id_sitasi_kampus": "meong.ac.id",
            },
            {
                "id_sitasi_dosen": "meong.ac.id-004",
                "nama_dosen": "Arief Budiman",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=OVSt6TkAAAAJ",
                "email_verified": "Verified email at meong.ac.id",
                "afiliations": "Assistant Professor of Computer Science at Universitas Teknokrat Indonesia",
                "total_sitasi": "9113",
                "id_sitasi_kampus": "meong.ac.id",
            },
            {
                "id_sitasi_dosen": "meong.ac.id-005",
                "nama_dosen": "Aditya Gumantan",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=EcHDu5wAAAAJ",
                "email_verified": "Verified email at meong.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia",
                "total_sitasi": "9027",
                "id_sitasi_kampus": "meong.ac.id",
            },
            {
                "id_sitasi_dosen": "meong.ac.id-006",
                "nama_dosen": "Rohmat Indra Borman",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=MLf7eZQAAAAJ",
                "email_verified": "Verified email at meong.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia",
                "total_sitasi": "8984",
                "id_sitasi_kampus": "meong.ac.id",
            },
            {
                "id_sitasi_dosen": "meong.ac.id-007",
                "nama_dosen": "Adi Sucipto, MT.",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=WXCZkqwAAAAJ",
                "email_verified": "Verified email at meong.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia (UTI)",
                "total_sitasi": "8891",
                "id_sitasi_kampus": "meong.ac.id",
            },
            {
                "id_sitasi_dosen": "meong.ac.id-008",
                "nama_dosen": "Berlinda Mandasari (Scopus ID: 58092736700)",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=-m67dqUAAAAJ",
                "email_verified": "Verified email at meong.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia",
                "total_sitasi": "8783",
                "id_sitasi_kampus": "meong.ac.id",
            },
            {
                "id_sitasi_dosen": "meong.ac.id-009",
                "nama_dosen": "Neneng",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=SyQPXdUAAAAJ",
                "email_verified": "Verified email at meong.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia",
                "total_sitasi": "8745",
                "id_sitasi_kampus": "meong.ac.id",
            },
            {
                "id_sitasi_dosen": "meong.ac.id-010",
                "nama_dosen": "Eko Bagus Fahrizqi",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=yFIIstgAAAAJ",
                "email_verified": "Verified email at meong.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia",
                "total_sitasi": "8638",
                "id_sitasi_kampus": "meong.ac.id",
            },
            {
                "id_sitasi_dosen": "meong.ac.id-011",
                "nama_dosen": "Styawati, ST, M.Cs.",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=XtLzsRYAAAAJ",
                "email_verified": "Verified email at meong.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia",
                "total_sitasi": "8371",
                "id_sitasi_kampus": "meong.ac.id",
            },
            {
                "id_sitasi_dosen": "meong.ac.id-012",
                "nama_dosen": "Putri Sukma Dewi",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=v2J6ecoAAAAJ",
                "email_verified": "Verified email at meong.ac.id",
                "afiliations": "Dosen pendidikan matematika, Universitas Teknokrat Indonesia",
                "total_sitasi": "8206",
                "id_sitasi_kampus": "meong.ac.id",
            },
            {
                "id_sitasi_dosen": "meong.ac.id-013",
                "nama_dosen": "Ryan Randy Suryono",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=9EkYs-gAAAAJ",
                "email_verified": "Verified email at meong.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia",
                "total_sitasi": "8120",
                "id_sitasi_kampus": "meong.ac.id",
            },
            {
                "id_sitasi_dosen": "meong.ac.id-014",
                "nama_dosen": "Agus Wantoro",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=MaJqcIAAAAAJ",
                "email_verified": "Verified email at meong.ac.id",
                "afiliations": "UNIVERSITAS TEKNOKRAT INDONESIA",
                "total_sitasi": "8094",
                "id_sitasi_kampus": "meong.ac.id",
            },
            {
                "id_sitasi_dosen": "meong.ac.id-015",
                "nama_dosen": "Rakhmat Dedi Gunawan",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=s29ExogAAAAJ",
                "email_verified": "Verified email at meong.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia",
                "total_sitasi": "8093",
                "id_sitasi_kampus": "meong.ac.id",
            },
        ]
    }
    send_data_array(data)

    enp = f"/detuniv/{hasil}"
    return redirect(enp)
