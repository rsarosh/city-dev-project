import requests
from bs4 import BeautifulSoup
import soup_extra_methods as methods

base_url = "http://apprenticareers.org/apply/"

csv = []

r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html5lib')
print('Loaded data from ' + base_url)

class_list = methods.find_all('div', soup, attrs={'class':'vcex-module vcex-icon-box clr vcex-icon-box-two textcenter'})

key_words_os = ['os', 'linux', 'windows', 'macintosh', 'ubuntu', 'arch linux', 'microsoft', 'apple']
key_words_network = ['cloud', 'clouds', 'network', 'networks', 'backend', 'server']
key_words_technician = ['technician', 'technical', 'technicians', 'sysadmin', 'IT']
key_words_developer = ['software', 'programmer', 'developer', 'designer', 'coder', 'code']

for class_item in class_list:
    course = {}
    title = methods.find('div', class_item, attrs={'class':'vcex-icon-box-heading'}).getText()
    description = methods.find('div', class_item, attrs={'class':'vcex-icon-box-content clr'}).getText().strip()

    '''
    TOPIC:
    * If the title mentions an OS (Linux, Windows, Macintosh), then the topic is 'OS'
    * If the title mentions a network term, then the topic is 'Cloud Services'
    * If the title mentions an IT term, then the topic is 'IT'
    * Otherwise, the topic is the first word of the title
    '''
    topic = title.split(" ")[0]
    for key_word in key_words_os:
        if key_word in title.lower():
            topic = 'OS'
    for key_word in key_words_network:
        if key_word in title.lower():
            topic = 'Network Services'
    for key_word in key_words_technician:
        if key_word in title.lower():
            topic = 'IT'
    for key_word in key_words_developer:
        if key_word in title.lower():
            topic = 'Programming'

    course['URL'] = 'http://apprenticareers.org/apply/'
    course['Title'] = title
    course['Topic'] =  topic
    course['SkillLevel'] = 'Advanced'
    course['CourseType'] = 'Job Certification'
    course['MinimumAge'] = 18
    course['MaximumAge'] = -1
    course['Description'] = description
    course['Provider'] = 'Apprenti Careers'
    course['Locations'] = ['8201 164th Ave NE #200, Redmond, WA 98052']

    csv.append(course)

import pandas as pd

df = pd.DataFrame(csv)
df.to_csv('csv\\course_apprenticareers.csv', index=False,encoding='utf-8')

print('Complete')