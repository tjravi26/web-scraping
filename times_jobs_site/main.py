from bs4 import BeautifulSoup

with open('times_jobs_site/times_jobs.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    # Using enumerate gives every job post an index.
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.h3.text.replace(' ', '')
            location = job.span.text.replace(' ', '')
            skills = job.find(
                'span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            # Saving every job post in a text file.
            with open(f'job_posts/post_{index}.text', 'w') as f:
                f.write(f"Comapany: {company_name.strip()}\n")
                f.write(f"Location: {location}\n")
                f.write(f"Skills required: {skills.strip()}\n")
                f.write(f"More Info: {more_info}")
            print(f'File {index} saved.')
