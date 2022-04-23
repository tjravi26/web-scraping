from turtle import home
from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())  # prints the html data in a readable format.
    tags = soup.find('p')  # finds only the first value.
    # print(tags)
    courses_html_tags = soup.find_all('p')  # finds all the values.
    # Can filter using class.
    # Must use _ after class as 'class' is a built-in method of python.
    course_cards = soup.find_all('h4', class_='card-title')
    # Can even filter while printing.
    for course in course_cards:
        print(course.text)
