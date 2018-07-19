import requests
from bs4 import BeautifulSoup,Tag
import soup_extra_methods as methods

# this header is required so the site doesn't detect the program as a scraper
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

base_url = "https://ncs.seattleu.edu/programs-courses/digital-technology/courses/"

csv = []

r = requests.get(base_url,headers=headers)
soup = BeautifulSoup(r.text, 'html5lib')

print('Loaded data from ' + base_url)

class_list = methods.find_all('article', soup) # classes are 'articles' in the website

urls = []

for class_item in class_list:
    url = methods.find('a', class_item);
    link = methods.safe_attr_access(url, 'href')

    if link != -1: # only append to urls if the link is real
        urls.append(link)


description_key_words = ['details', 'description']

for url in urls:
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html5lib')
    title = methods.find('title', soup).getText()

    subtitles = methods.find_all('div', soup, attrs={'class':'sub-title'}) # 'subtitle' includes the description / course details
    description_header = 0
    for subtitle in subtitles:
        for key_word in description_key_words:
            if key_word in subtitle.getText().strip().lower(): # find the 'header' for the description
                description_header = subtitle
                break

    description = methods.next_tag(description_header)

    course = {}
    course['URL'] = url
    course['Title'] = title.strip()
    course['Topic'] = 'Digital Culture'
    course['SkillLevel'] = 'Beginner'
    course['CourseType'] = 'Course'
    course['MinimumAge'] = -1
    course['MaximumAge'] = -1
    course['Description'] = description.getText().strip()
    course['Provider'] = 'Seattle University'
    course['Locations'] = ['1215 E Columbia St, Seattle, WA 98122']
    csv.append(course)

import pandas as pd

df = pd.DataFrame(csv)
df.to_csv('csv\\course_seattleuniversity.csv', index=False,encoding='utf-8')

print("Complete")