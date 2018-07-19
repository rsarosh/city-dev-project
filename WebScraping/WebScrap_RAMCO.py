import requests
import re
from bs4 import BeautifulSoup
import soup_extra_methods as methods

base_url = "https://www.ramco-training.com/pages/"

csv = []

r = requests.get(base_url + 'programming.htm')
soup = BeautifulSoup(r.text, 'html5lib')

print('Loaded data from ' + base_url)

menu_bar = methods.find_all('li', methods.find('ul', soup, attrs={'id':'MenuBar1'}))[1:]

urls = []
topics = []
for course in menu_bar:
    link = methods.find('a', course)
    url = methods.safe_attr_access(link, 'href')
    if url != -1:
        urls.append(url)
        topics.append(link.getText())

for url,topic in zip(urls,topics):
    r = requests.get(base_url + url)
    soup = BeautifulSoup(r.text, 'html5lib')

    url_title = methods.find('title', soup).getText().strip().lower()

    if not 'live online' in url_title:
        tables = methods.find_all('table', soup) # the correct table can be found if one of the rows has a cell saying 'course outline'
        class_titles = []
        for table in tables:
            table_rows = methods.find_all('tr', table)
            if len(table_rows) > 0:
                table_rows = table_rows[1:]

            for row in table_rows:
                table_columns = methods.find_all('td', row)
                if 'course outline' in row.getText().strip().lower() and len(table_columns) > 1:
                    title = table_columns[0].getText()
                    class_titles.append(methods.format_string(title))

        desc = ''
        location_options = methods.find_all(re.compile('^h[1-6]$'), soup)
        location = ''
        for option in location_options:
            txt = option.getText().strip()
            string_loc = txt.lower().find('training center')
            if string_loc != -1:
                location = txt[string_loc:]
                location = location.split(":")[1][1:]

                # find the description as the first non-empty paragraph under the location header
                desc = methods.next_tag(option, tag_name='p', err_handle='ignore')
                num = 0
                while desc != -1 and not re.search('[a-zA-Z]+',desc.getText()):
                    desc = methods.next_tag(desc, tag_name='p', err_handle='ignore')
                if desc != -1:
                    desc  = methods.format_string(desc.getText())
                else:
                    desc = ''

        for class_title in class_titles:
            course_type = 'Course'
            if 'online' in class_title.lower():
                course_type = 'Online Course'
            course = {}
            course['URL'] = base_url + url
            course['Title'] = class_title
            course['Topic'] = topic
            course['SkillLevel'] = 'Beginner'
            course['CourseType'] = course_type
            course['MinimumAge'] = -1
            course['MaximumAge'] = -1
            course['Description'] = desc
            course['Provider'] = 'RAMCO Training'
            course['Locations'] = [location]
            csv.append(course)

import pandas as pd

df = pd.DataFrame(csv)
df.to_csv('csv\\course_ramco.csv', index=False,encoding='utf-8')

print('Complete')