import requests
from bs4 import BeautifulSoup
import soup_extra_methods as methods

base_url = "http://www.seattle.gov/iandraffairs/RTW"

csv = []

r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html5lib')

print('Loaded data from ' + base_url)

class_options = methods.find_all('h2', methods.find('main', soup)) # potential classes are h2 headers within the main div

for option in class_options:
    course = {}
    name = option.getText()
    if name[:16] == "Ready to Work - ": # each class begins with 'Ready to Work'
        course['URL'] = base_url
        course['Title'] = 'Ready to Work: ' + name[16:]
        course['Topic'] = 'Digital Literacy'
        course['SkillLevel'] = 'Beginner'
        course['CourseType'] = 'Class'
        course['MinimumAge'] = -1
        course['MaximumAge'] = -1
        course['Description'] = 'Ready to Work (RTW) was designed for residents who face barriers to learning English and gaining employment. The program combines English as a Second Language (ESL) classes (1-3) with computer literacy instruction and case management to help immigrants gain job readiness skills and take steps toward economic self-sufficiency. Participants in the program have moved on to full-time jobs and/or advanced English-language level classes.'
        course['Provider'] = 'Seattle Gov'
        loc_unformatted = methods.next_tag(option, tag_name='p', len=2).find_all('a')
        locations = []
        for location in loc_unformatted:
            locations.append(location.getText())
        course['Locations'] = locations
        csv.append(course)

import pandas as pd

df = pd.DataFrame(csv)
df.to_csv('csv\\course_seattleRTW.csv', index=False,encoding='utf-8')

print('Complete')