import requests
from parsel import Selector
import pandas as pd
import random
import re
import json

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

def scrape_all_authors():
    hasil = input("Masukkan nama file: ")
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
                if 2 <= param <= 32:
                    data.append({
                        'id_sitasi_dosen': f'{hasil}-{increment}',
                        'nama_dosen': name,
                        'url_dosen': link,
                        'total_sitasi': affiliations,
                        'email_verified': email,
                        'total_sitasi': cited_by,
                        'id_sitasi_kampus': hasil
                    })
                    increment += 1
            if soup.css('.gsc_pgn button.gs_btnPR::attr(onclick)').get() and param <= 33:
                params['after_author'] = re.search(r'after_author\\x3d(.*)\\x26',
                                                    str(soup.css('.gsc_pgn button.gs_btnPR::attr(onclick)').get())).group(1)
                params['astart'] += 10
            else:
                break
            if 2 <= param <= 32:
                print(json.dumps(data, indent=2, ensure_ascii=False))
                df = pd.read_json(json.dumps(data, indent=2, ensure_ascii=False))
                df.to_csv(hasil + '_Juli.csv', sep=';', encoding='utf-8', index=False)
                total_cited_by = df['total_sitasi'].sum()
                print("Total sum dari 'cited_by':", total_cited_by)
            param += 1
            print(param)
        except Exception as e:
            print("An error occurred:", e)

scrape_all_authors()
