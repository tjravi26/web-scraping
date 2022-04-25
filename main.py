from turtle import home
from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())  # prints the html data in a readable format.

    tags = soup.find('p')  # finds only the first value.
    # print(tags)

    courses_html_tags = soup.find_all('p')  # finds all the values.
    for course in courses_html_tags:
        print(course.text)

    # Can filter using class.
    # Must use _ after class as 'class' is a built-in method of python.
    course_cards = soup.find_all('div', class_='card-body')

    # Can even filter while printing.
    for course in course_cards:
        print(
            f"The course: {course.h4.text} costs: {course.a.text.split()[-1]}")
