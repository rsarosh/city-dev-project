from selenium import webdriver
from bs4 import BeautifulSoup,Tag
import soup_extra_methods as methods

base_url = "http://www.kalacademy.org/home/Calendar"
csv = []

browser = webdriver.Chrome()
browser.get(base_url)
innerHTML = browser.execute_script("return document.body.innerHTML")

soup = BeautifulSoup(innerHTML, 'html5lib')

print('Loaded data from ' + base_url)

# the rows of the main table of all classes
table = methods.find('table', soup, attrs={'class':'calendar__table'}).find("tbody")
rows = table.find_all('tr', recursive=False)[1:][:-1]

row_num = 0 # used to determine difficulty of course (farther along rows, more advanced course)
for row in rows:
    row_num += 1

    sections = row.find_all('td', recursive=False) #sections[0] is topic, sections[1] is subtable w classes
    sub_rows = methods.find_all('tr', sections[1])

    for sub_row in sub_rows:
        course = {}
        title = methods.find('p', methods.find('td', sub_row))
        topic = sections[0]

        skill_level = 'Intermediate'
        if row_num > len(rows)/2:
            skill_level = 'Advanced'

        course['URL'] = 'http://www.kalacademy.org/home/Calendar'
        course['Title'] = title.getText().strip()
        course['Topic'] = topic.getText().strip()
        course['SkillLevel'] = skill_level
        course['CourseType'] = 'Course'
        course['MinimumAge'] = -1
        course['MaximumAge'] = -1
        course['Description'] = ""
        course['Provider'] = 'Kal Academy'
        course['Locations'] = ['2757 152nd Ave NE, Redmond, WA']
        csv.append(course)

import pandas as pd

df = pd.DataFrame(csv)
df.to_csv('csv\\course_kalacademy.csv', index=False,encoding='utf-8')

print('Complete')