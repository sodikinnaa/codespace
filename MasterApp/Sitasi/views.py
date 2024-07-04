from django.shortcuts import render, redirect
from django.http import HttpResponse
from .helpers.global_helpers import *
import pandas as pd
import re

from parsel import Selector
# Create your views here.
def daftaruniv(request):
    endp = "https://media.datadebasa.com/api/v1.0/universitas"
    data = getData(endp)
    return render(request, 'daftar_univ.html', {'content': data})

def detuniv(request, prefix):
    endp = f"https://media.datadebasa.com/api/v1.0/universitas/{prefix}?max=1000"
    endpdosen = f"https://media.datadebasa.com/api/v1.0/dosen/{prefix}?max=1000"
    data_univ = getData(endp)
    data_dosen = getData(endpdosen)
    data ={
        'data_univ':data_univ[0],
        'data_dosen' : data_dosen
    }
    print(data_univ)
    
    return render(request, 'detail_univ.html', {'content': data})

def postuniv(request):
    nama_kampus = request.GET.get('nama_kampus')
    url_kampus = request.GET.get('url_kampus')
    
    # Lakukan sesuatu dengan data yang diambil, misalnya menyimpannya ke database atau memprosesnya lebih lanjut
    response = f"Nama Kampus: {nama_kampus}, URL Kampus: {url_kampus}"
    endp = f"https://media.datadebasa.com//api/v1.0/universitas/{url_kampus}"
    is_data = getData(endp)
    if is_data:
        return HttpResponse('data Sudah di tabahkan <br> <a href="/adduniv">Back</a>')
    data = {
        'id_sitasi_kampus':url_kampus,
        'nama_kampus':nama_kampus,
        'url_kampus':url_kampus,
        'total_sitasi':0
    }    
    endpoint = "https://media.datadebasa.com/api/v1.0/universitas"
    is_save = postData(endpoint, data)
    if(is_save):
        return HttpResponse('data bserhasil di kirimkan  <br> <a href="/">Back</a>')
    return HttpResponse(f"post data {response}")

def editUniv(request, prefix):
    endp = f"https://media.datadebasa.com//api/v1.0/universitas/{prefix}"
    
    data = getData(endp)
    if data:
        data = data[0]
        dd(data)
        return render(request, 'edit_univ.html', {'content': data})
    else:
        return HttpResponse('data tidak ditemukan <br> <a href="/">Back</a>')

def updateUniv(request):
    nama_kampus = request.GET.get('nama_kampus')
    url_kampus = request.GET.get('url_kampus')
    
    # Lakukan sesuatu dengan data yang diambil, misalnya menyimpannya ke database atau memprosesnya lebih lanjut
    response = f"Nama Kampus: {nama_kampus}, URL Kampus: {url_kampus}"
    endp = f"https://media.datadebasa.com//api/v1.0/universitas/{url_kampus}"
    is_data = getData(endp)
    if not is_data:
        return HttpResponse('data tidak ditemukan <br> <a href="/edit/{{ url_kampus }}">Back</a>')
    
    data = {
        'id_sitasi_kampus': url_kampus,
        'nama_kampus': nama_kampus,
        'url_kampus': url_kampus,
        'total_sitasi': is_data[0]['total_sitasi']
    }
    
    endpoint = f"https://media.datadebasa.com/api/v1.0/universitas/{url_kampus}"
    is_update = putData(endpoint, data)
    if is_update:
        return HttpResponse('data berhasil diupdate <br> <a href="/">Back</a>')
    return HttpResponse(f"update data {response}")
    return HttpResponse('update data')
def addUniv(request):
    return render(request, 'add_univ.html')

def deleteUniv(request, prefix):
    endp = f"https://media.datadebasa.com/api/v1.0/universitas/{prefix}"
    
    try:
        response = requests.delete(endp)
        response.raise_for_status()  # Check if the request was successful
        return HttpResponse('data berhasil dihapus <br> <a href="/">Back</a>')
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"Error deleting the data: {e} <br> <a href='/'>Back</a>")

    return HttpResponse('scrape author')
def scrape_all_authors(request, hasil):    
    params = {
        'view_op': 'search_authors',  # author results
        'mauthors': hasil,  # search query
        'astart': 20  # page number
    }

    headers = {
        "User-Agent": get_fake_user_agent()
    }

    data = []
    param = 0
    max = 32
    increment = 1
    while True:
        try:
            html = requests.get('https://scholar.google.com/citations', params=params, headers=headers, timeout=30)
            soup = Selector(text=html.text)
            for author in soup.css('.gs_ai_chpr'):
                name = author.css('.gs_ai_name').xpath('normalize-space()').get()
                link = f'https://scholar.google.com{author.css(".gs_ai_name a::attr(href)").get()}'
                affiliations = author.css('.gs_ai_aff').xpath('normalize-space()').get()
                email = author.css('.gs_ai_eml').xpath('normalize-space()').get()
                try:
                    cited_by = re.search(r'\d+', author.css('.gs_ai_cby::text').get()).group()  # Cited by 17143 -> 17143
                except:
                    cited_by = None
                if 2 <= param <= max:
                    id_s = str(increment).zfill(3)
                    id_sitasi = hasil + '-' + id_s
                    data.append({
                        'id_sitasi_dosen': id_sitasi,
                        'nama_dosen': name,
                        'url_dosen': link,
                        'total_sitasi': affiliations,
                        'email_verified':email,
                        'total_sitasi': cited_by,
                        'id_sitasi_kampus': hasil
                    })

                    data_author = {
                        'id_sitasi_dosen': id_sitasi,
                        'nama_dosen': name,
                        'url_dosen': link,
                        'email_verified':email,
                        'total_sitasi': affiliations,
                        'total_sitasi': cited_by,
                        'id_sitasi_kampus': hasil
                    }
                    increment += 1
                    print(id_sitasi)
                    send_data_to_endpoint(data_author)
                    # send_data(id_sitasi, data_author)

            if soup.css('.gsc_pgn button.gs_btnPR::attr(onclick)').get() and param <= 33:
                params['after_author'] = re.search(r'after_author\\x3d(.*)\\x26',
                                                    str(soup.css('.gsc_pgn button.gs_btnPR::attr(onclick)').get())).group(1)
                params['astart'] += 10
            else:
                break
            if 2 <= param <= max:
                print(json.dumps(data, indent=2, ensure_ascii=False))
                
                df = pd.read_json(json.dumps(data, indent=2, ensure_ascii=False))
                # df.to_csv(hasil + '_Juli.csv', sep=';', encoding='utf-8', index=False)
                total_cited_by = df['total_sitasi'].sum()
                print("Total sum dari 'cited_by':", total_cited_by)
            param += 1
            print(param)
        except Exception as e:
            print("An error occurred:", e)
    endp = f"detuniv/{hasil}"
    return redirect(endp)
        