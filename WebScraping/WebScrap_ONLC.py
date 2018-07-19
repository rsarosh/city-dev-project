#WARNING: program goes to >1000 different pages, so runtime may be a while
import requests
import re
from bs4 import BeautifulSoup,Tag

base_url = "https://www.onlc.com/"

csv = []

r = requests.get(base_url + 'sched.asp?g=Seattle-Washington-Computer-Training-Classes')
soup = BeautifulSoup(r.text, 'html5lib')


print('LOADED DATA FROM ' + base_url)

main_div = soup.find('form', attrs={'name':'main'})

table = main_div.find('table').find_all('tr')[2:] #Skip first one

urls = []
for row in table:
    url = row.find('a')
    if url:
        if url.has_attr('href'):
            urls.append(url['href'])

#Not a perfect method, but gets about 95% correct which is good for the alotted of time
key_words = [['Software', ['adobe', 'photoshop', 'microsoft office', 'microsoft word', 'excel', 'spreadsheet', 'software', 'creative cloud', 'windows', 'linux'], 0],
             ['Network / Cloud', ['SQL','amazon web service','sysadmin','network', 'cloud', 'backend', 'server', 'ftp', 'maintenance', 'linux', 'troubleshoot', 'backup'], 0],
             ['Programming', ['developer', 'programming', 'coding', 'script', 'development', 'java', 'python', 'c++'], 0],
            ]

num = 0
for url in urls:
    num += 1
    r = requests.get(base_url + url)
    soup = BeautifulSoup(r.text, 'html5lib')

    title = soup.find('title').getText()

    '''
    Look for an 'overview' paragraph and use that: if that doesn't exist, use the whole header
    '''
    desc_div = soup.find('h1').parent
    desc_headers = desc_div.find_all('b')
    desc = ''
    for header in desc_headers:
        if header.getText().strip().lower() == 'overview':
            desc = header
            break
    if desc != '':
        while isinstance(desc, Tag) or desc == '':
            desc = desc.nextSibling
    else:
        desc = desc_div.getText().strip()
    re.sub(r"\s+", " ", desc)

    searcher = desc_div.getText().strip().lower() + title.lower()
    topic = 'Digital Literacy'

    for subject in key_words:
        for key_word in subject[1]:
            if key_word in searcher:
                subject[2] += 1

    most_hits = 0
    for subject in key_words:
        if subject[2] >= most_hits:
            most_hits = subject[2]
            topic = subject[0]

    skill_level = 'Intermediate / Advanced'

    course = {}
    course['URL'] = base_url + url
    course['Title'] = title
    course['Topic'] = topic
    course['SkillLevel'] = skill_level
    course['CourseType'] = 'Class / Web Course'
    course['MinimumAge'] = -1
    course['MaximumAge'] = -1
    course['Description'] = desc
    course['Provider'] = 'ONLC'
    course['Locations'] = ['1700 7th Ave #2100', '14205 SE 36th St #100', '19125 North Creek Pkwy #120']

    print(str(num) + " / " + str(len(urls)))
    csv.append(course)

import pandas as pd

df = pd.DataFrame(csv)
df.to_csv('csv\\course_onlc.csv', index=False,encoding='utf-8')

print("COMPLETED")
