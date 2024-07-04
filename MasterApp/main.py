import requests

def get_html_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

url = "https://trends.google.com/trends/trendingsearches/daily?geo=ID&hl=en-US"
html_content = get_html_from_url(url)

if html_content:
    with open("trending_searches.html", "w", encoding="utf-8") as file:
        file.write(html_content)
