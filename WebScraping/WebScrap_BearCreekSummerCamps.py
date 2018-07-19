import requests
import re
from bs4 import BeautifulSoup,Tag
import warnings
import soup_extra_methods as methods

base_url = "https://www.tbcs.org/page.cfm?p=5384"

csv = []

r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html5lib')
print('Loaded data from ' + base_url)

#Find the header that refers to technology camps by using a key word search on all headers
main_div = methods.find('div', soup, attrs={'id':'eventRegSessionDetails'})
headers = main_div.find_all(re.compile('^h[1-6]$'), recursive=False) # any header will be included in the search, however it must be on the top-level of the div

key_word_technology = ['tech', 'technology', 'science', 'stem']

tech_header = 0
for header in headers:
    for key_word in key_word_technology:
        if key_word in header.getText().strip().lower():
            tech_header = header
if tech_header == 0:
    warnings.warn("No technology header found")

class_div = methods.next_tag(tech_header, tag_name='div') #the next div after the tech header contains the courses

class_list = methods.surface_search(class_div) # each 'div' in the class div is a course
class_names = class_div.find_all(re.compile('^h[1-6]$'), recursive=False) # all headers are different course names

if len(class_list) != len(class_names):
    warnings.warn("Different number of classes and titles found!")
else:
    for class_desc,class_title in zip(class_list,class_names):
        title = class_title.getText()

        # find the age range by working around the... 'interesting' formatting of it
        ages = []
        age_range = title[title.find("(")+1:title.find(")")]
        age_range = age_range.split("-")
        is_grade = False
        for age in age_range:
            age_num = re.findall(r'\d+', age)
            if len(age_num) == 0:
                age_num = 0
            else:
                age_num = int(age_num[0])
            age = age.lower()
            if age.find("grade") != -1 or (age.find("age") == -1 and is_grade):
                is_grade = True
                age_num += 5
            ages.append(age_num)

        # location
        location = methods.find('div', class_desc, attrs={'class':'location'}).getText().strip()

        # description: some are very long, so i cropped it to first paragraph for each (ideally it would range from 1-3)
        description = methods.find('div', class_desc, attrs={'class': 'description'}).getText().strip()
        description_paragraphs = description.split('\n')
        description = description_paragraphs[0]

        course = {}
        course['URL'] = 'https://www.tbcs.org/community/summer-camp'
        course['Title'] = title
        course['Topic'] = 'Science & Technology'
        course['SkillLevel'] = 'Beginner'
        course['CourseType'] = 'Summer Camp'
        course['MinimumAge'] = ages[0]
        course['MaximumAge'] = ages[1]
        course['Description'] = description
        course['Provider'] = 'Bear Creek Summer Camps'
        course['Locations'] = [location]
        csv.append(course)

import pandas as pd

df = pd.DataFrame(csv)
df.to_csv('csv\\course_breakcreeksummercamps.csv', index=False,encoding='utf-8')

print("Complete")