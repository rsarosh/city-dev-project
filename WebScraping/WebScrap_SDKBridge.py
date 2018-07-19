import requests
from bs4 import BeautifulSoup,Tag
import soup_extra_methods as methods

# the Udemy page blocks the request unless these headers are inputted
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

base_url = "http://sdkbridge.com/online-courses/"

csv = []

r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html5lib')

print('Loaded data from ' + base_url)

links = soup.find("main").find_all("a")
for link in links:
    url = link['href']
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html5lib')

    title = methods.find('h1', soup, attrs={'class':'clp-lead__title'}).getText().strip()

    skill_level = 'Advanced'
    requirements = " | ".join([tag.getText() for tag in methods.find_all('li', soup, attrs={'class':'requirements__item'})])
    target_audience = " | ".join([tag.getText() for tag in methods.find_all('ul', soup, attrs={'class':'audience__list'})])

    #Description starts after the last 'strong' after the description header, and ends after the first strong after that
    description_paragraphs = []
    curr = methods.find('div', soup, attrs={'class':'description__title'})
    started = False
    ended = False
    while started is False or ended is False:
        curr = curr.nextSibling
        if isinstance(curr, Tag):
            if curr.find('strong') or curr.name is not 'p':
                if started:
                    ended = True
            elif not started:
                started = True
            if started and not ended:
                description_paragraphs.append(curr.getText())

    description = "\n".join(description_paragraphs).strip()

    '''
    Skill level factors (order from lowest to highest priority):
     * If 3 or more requirements, then it's advanced
     * If title, description or target audience includes "no programming experience", then it's intermediate
     * If requirements mention experience, then it's advanced

    By default, it's advanced
    '''
    key_phrase = ['no programming', 'no experience', 'programming not required', 'programming not requirement', 'no coding', 'no code', 'coding not required', 'coding not requirement']
    full_text_search = description.lower().strip() + title.lower().strip() + requirements.lower().strip() + target_audience.lower().strip()
    if len(requirements) >= 3:
        skill_level = 'Advanced'

    for phrase in key_phrase:
        if full_text_search.find(phrase) != -1:
            skill_level = 'Intermediate'

    if 'experience' in requirements.lower() and 'no experience' not in requirements.lower() and 'experience not' not in requirements.lower():
        skill_level = 'Advanced'

    course = {}
    course['URL'] = url
    course['Title'] = title
    course['Topic'] = 'Digital Literacy'
    course['SkillLevel'] = skill_level
    course['CourseType'] = 'Online Course'
    course['MinimumAge'] = -1
    course['MaximumAge'] = -1
    course['Description'] = description
    course['Provider'] = 'SDK Bridge'
    course['Locations'] = []

    csv.append(course)

import pandas as pd

df = pd.DataFrame(csv)
df.to_csv('csv\\course_sdkbridge.csv', index=False,encoding='utf-8')

print('Complete')