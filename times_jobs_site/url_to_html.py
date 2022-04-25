import requests


def url_to_file(url, filename='times_jobs_site/times_jobs.html'):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        with open(filename, 'w') as file:
            file.write(html_text)
        file.close()


url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="

url_to_file(url)
