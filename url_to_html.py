import requests


def url_to_file(url, filename='box_office.html'):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        with open(filename, 'w') as file:
            file.write(html_text)
        file.close()


url = "https://www.boxofficemojo.com/year/world/"

url_to_file(url)
