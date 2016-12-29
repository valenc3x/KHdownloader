import urllib.request
from bs4 import BeautifulSoup


def get_html_from_url(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    return html


def get_mp3_links(site_url):
    html = get_html_from_url(site_url)
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.h2.string)
    all_a = soup.find_all('a')
    all_mp3_url = []
    for a in all_a:
        if '.mp3' in a['href'] and a.string == 'Download':
            url_struct = a['href'].split('/')
            file_name = "%s/%s" % (url_struct[-2], url_struct[-1])
            html = get_html_from_url(a['href'])
            soup = BeautifulSoup(html, 'html.parser')
            file_url = soup.audio['src']
            all_mp3_url.append([file_url, file_name])
    return all_mp3_url

