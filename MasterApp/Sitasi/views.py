from django.shortcuts import render, redirect
from django.http import HttpResponse
from .helpers.global_helpers import *
import pandas as pd
import re

from parsel import Selector


# Create your views here.
def daftaruniv(request):
    endp = "https://media.datadebasa.com/api/v1.0/universitas?max=10000"
    data = getData(endp)
    return render(request, "daftar_univ.html", {"content": data})


def detuniv(request, prefix):
    endp = f"https://media.datadebasa.com/api/v1.0/universitas/{prefix}?max=1000"
    endpdosen = f"https://media.datadebasa.com/api/v1.0/dosen/{prefix}?max=1000"
    data_univ = getData(endp)
    data_dosen = getData(endpdosen)
    data = {"data_univ": data_univ[0], "data_dosen": data_dosen}
    # print(data_univ)

    return render(request, "detail_univ.html", {"content": data})


def postuniv(request):
    nama_kampus = request.GET.get("nama_kampus")
    url_kampus = request.GET.get("url_kampus")

    # Lakukan sesuatu dengan data yang diambil, misalnya menyimpannya ke database atau memprosesnya lebih lanjut
    response = f"Nama Kampus: {nama_kampus}, URL Kampus: {url_kampus}"
    endp = f"https://media.datadebasa.com//api/v1.0/universitas/{url_kampus}"
    is_data = getData(endp)
    if is_data:
        return HttpResponse('data Sudah di tabahkan <br> <a href="/adduniv">Back</a>')
    data = {
        "id_sitasi_kampus": url_kampus,
        "nama_kampus": nama_kampus,
        "url_kampus": url_kampus,
        "total_sitasi": 0,
    }
    endpoint = "https://media.datadebasa.com/api/v1.0/universitas"
    is_save = postData(endpoint, data)
    if is_save:
        return HttpResponse(
            'Data Universitas Berhasil di tambahkan <br> <a href="/">Back</a>'
        )
    return HttpResponse(f"post data {response}")


def editUniv(request, prefix):
    endp = f"https://media.datadebasa.com//api/v1.0/universitas/{prefix}"
    data = getData(endp)
    if data:
        data = data[0]
        return render(request, "edit_univ.html", {"content": data})
    else:
        return HttpResponse('data tidak ditemukan <br> <a href="/">Back</a>')


def updateUniv(request, prefix):
    nama_kampus = request.GET.get("nama_kampus")
    url_kampus = request.GET.get("url_kampus")

    # Lakukan sesuatu dengan data yang diambil, misalnya menyimpannya ke database atau memprosesnya lebih lanjut
    response = f"Nama Kampus: {nama_kampus}, URL Kampus: {url_kampus}"
    endp = f"https://media.datadebasa.com//api/v1.0/universitas/{prefix}"
    is_data = getData(endp)
    if not is_data:
        return HttpResponse(
            'data tidak ditemukan <br> <a href="/edit/{{ url_kampus }}">Back</a>'
        )

    data = {
        "id_sitasi_kampus": url_kampus,
        "nama_kampus": nama_kampus,
        "url_kampus": url_kampus,
        "total_sitasi": 0,
    }

    endpoint = f"https://media.datadebasa.com/api/v1.0/universitas/{prefix}"
    is_update = putData(endpoint, data)
    if is_update:
        return HttpResponse(
            'Data Universitas Berhasil di Update <br> <a href="/">Back</a>'
        )
    return HttpResponse(f"update data {response}")


def addUniv(request):
    return render(request, "add_univ.html")


def deleteUniv(request, prefix):
    endp = f"https://media.datadebasa.com/api/v1.0/universitas/{prefix}"

    try:
        response = requests.delete(endp)
        response.raise_for_status()  # Check if the request was successful
        return HttpResponse(
            'Data Universitas Berhasil di Update <br> <a href="/">Back</a>'
        )
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"Error deleting the data: {e} <br> <a href='/'>Back</a>")


def fake_autor(request, hasil):
    data = {
        "dosen": [
            {
                "id_sitasi_dosen": "teknokrat.ac.id-002",
                "nama_dosen": "Rizki Yuliandra, M.Pd",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=1BSEYXIAAAAJ",
                "email_verified": "Verified email at teknokrat.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia",
                "total_sitasi": "9301",
                "id_sitasi_kampus": "teknokrat.ac.id",
            },
            {
                "id_sitasi_dosen": "teknokrat.ac.id-003",
                "nama_dosen": "Rachmi Marsheilla Aguss",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=aZnAoQQAAAAJ",
                "email_verified": "Verified email at teknokrat.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia",
                "total_sitasi": "9279",
                "id_sitasi_kampus": "teknokrat.ac.id",
            },
            {
                "id_sitasi_dosen": "teknokrat.ac.id-004",
                "nama_dosen": "Arief Budiman",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=OVSt6TkAAAAJ",
                "email_verified": "Verified email at teknokrat.ac.id",
                "afiliations": "Assistant Professor of Computer Science at Universitas Teknokrat Indonesia",
                "total_sitasi": "9113",
                "id_sitasi_kampus": "teknokrat.ac.id",
            },
            {
                "id_sitasi_dosen": "teknokrat.ac.id-005",
                "nama_dosen": "Aditya Gumantan",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=EcHDu5wAAAAJ",
                "email_verified": "Verified email at teknokrat.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia",
                "total_sitasi": "9027",
                "id_sitasi_kampus": "teknokrat.ac.id",
            },
            {
                "id_sitasi_dosen": "teknokrat.ac.id-006",
                "nama_dosen": "Rohmat Indra Borman",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=MLf7eZQAAAAJ",
                "email_verified": "Verified email at teknokrat.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia",
                "total_sitasi": "8984",
                "id_sitasi_kampus": "teknokrat.ac.id",
            },
            {
                "id_sitasi_dosen": "teknokrat.ac.id-007",
                "nama_dosen": "Adi Sucipto, MT.",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=WXCZkqwAAAAJ",
                "email_verified": "Verified email at teknokrat.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia (UTI)",
                "total_sitasi": "8891",
                "id_sitasi_kampus": "teknokrat.ac.id",
            },
            {
                "id_sitasi_dosen": "teknokrat.ac.id-008",
                "nama_dosen": "Berlinda Mandasari (Scopus ID: 58092736700)",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=-m67dqUAAAAJ",
                "email_verified": "Verified email at teknokrat.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia",
                "total_sitasi": "8783",
                "id_sitasi_kampus": "teknokrat.ac.id",
            },
            {
                "id_sitasi_dosen": "teknokrat.ac.id-009",
                "nama_dosen": "Neneng",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=SyQPXdUAAAAJ",
                "email_verified": "Verified email at teknokrat.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia",
                "total_sitasi": "8745",
                "id_sitasi_kampus": "teknokrat.ac.id",
            },
            {
                "id_sitasi_dosen": "teknokrat.ac.id-010",
                "nama_dosen": "Eko Bagus Fahrizqi",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=yFIIstgAAAAJ",
                "email_verified": "Verified email at teknokrat.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia",
                "total_sitasi": "8638",
                "id_sitasi_kampus": "teknokrat.ac.id",
            },
            {
                "id_sitasi_dosen": "teknokrat.ac.id-011",
                "nama_dosen": "Styawati, ST, M.Cs.",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=XtLzsRYAAAAJ",
                "email_verified": "Verified email at teknokrat.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia",
                "total_sitasi": "8371",
                "id_sitasi_kampus": "teknokrat.ac.id",
            },
            {
                "id_sitasi_dosen": "teknokrat.ac.id-012",
                "nama_dosen": "Putri Sukma Dewi",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=v2J6ecoAAAAJ",
                "email_verified": "Verified email at teknokrat.ac.id",
                "afiliations": "Dosen pendidikan matematika, Universitas Teknokrat Indonesia",
                "total_sitasi": "8206",
                "id_sitasi_kampus": "teknokrat.ac.id",
            },
            {
                "id_sitasi_dosen": "teknokrat.ac.id-013",
                "nama_dosen": "Ryan Randy Suryono",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=9EkYs-gAAAAJ",
                "email_verified": "Verified email at teknokrat.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia",
                "total_sitasi": "8120",
                "id_sitasi_kampus": "teknokrat.ac.id",
            },
            {
                "id_sitasi_dosen": "teknokrat.ac.id-014",
                "nama_dosen": "Agus Wantoro",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=MaJqcIAAAAAJ",
                "email_verified": "Verified email at teknokrat.ac.id",
                "afiliations": "UNIVERSITAS TEKNOKRAT INDONESIA",
                "total_sitasi": "8094",
                "id_sitasi_kampus": "teknokrat.ac.id",
            },
            {
                "id_sitasi_dosen": "teknokrat.ac.id-015",
                "nama_dosen": "Rakhmat Dedi Gunawan",
                "url_dosen": "https://scholar.google.com/citations?hl=en&user=s29ExogAAAAJ",
                "email_verified": "Verified email at teknokrat.ac.id",
                "afiliations": "Universitas Teknokrat Indonesia",
                "total_sitasi": "8093",
                "id_sitasi_kampus": "teknokrat.ac.id",
            },
        ]
    }
    send_data_array(data)

    enp = f"/detuniv/{hasil}"
    return redirect(enp)


def scrape_all_authors(request, hasil):
    params = {
        "view_op": "search_authors",  # author results
        "mauthors": hasil,  # search query
        "astart": 20,  # page number
    }
    headers = {"User-Agent": get_fake_user_agent()}

    data = []
    param = 0
    max = 32
    increment = 1
    while True:
        try:
            html = requests.get(
                "https://scholar.google.com/citations",
                params=params,
                headers=headers,
                timeout=30,
            )
            soup = Selector(text=html.text)
            for author in soup.css(".gs_ai_chpr"):
                name = author.css(".gs_ai_name").xpath("normalize-space()").get()
                link = f'https://scholar.google.com{author.css(".gs_ai_name a::attr(href)").get()}'
                affiliations = author.css(".gs_ai_aff").xpath("normalize-space()").get()
                email = author.css(".gs_ai_eml").xpath("normalize-space()").get()
                try:
                    cited_by = re.search(
                        r"\d+", author.css(".gs_ai_cby::text").get()
                    ).group()  # Cited by 17143 -> 17143
                except:
                    cited_by = None
                if 2 <= param <= max:
                    id_s = str(increment).zfill(3)
                    id_sitasi = hasil + "-" + id_s

                    data_author = {
                        "id_sitasi_dosen": id_sitasi,
                        "nama_dosen": name,
                        "url_dosen": link,
                        "email_verified": email,
                        "total_sitasi": affiliations,
                        "total_sitasi": cited_by,
                        "id_sitasi_kampus": hasil,
                    }
                    data.append(data_author)
                    increment += 1
                    print(id_sitasi)

            if (
                soup.css(".gsc_pgn button.gs_btnPR::attr(onclick)").get()
                and param <= max
            ):
                params["after_author"] = re.search(
                    r"after_author\\x3d(.*)\\x26",
                    str(soup.css(".gsc_pgn button.gs_btnPR::attr(onclick)").get()),
                ).group(1)
                params["astart"] += 10
            else:
                break

            param += 1
            print(param)
        except Exception as e:
            print("An error occurred:", e)
    dosen = {"dosen": data}
    send_data_array(dosen)
    endp = f"/detuniv/{hasil}"
    return HttpResponse(
        f'Data Berhasil di Singkronisasi <br> <a href="/detuniv/{hasil}">Back</a>'
    )
