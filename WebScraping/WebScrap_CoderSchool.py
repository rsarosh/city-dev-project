import requests
from bs4 import BeautifulSoup
import soup_extra_methods as methods

base_url = "https://www.thecoderschool.com/camps"

csv = []

r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html5lib')

print('Loaded data from ' + base_url)

#Each course is a different 'index-section' div within the 'main-content' div
main_div = methods.find("div", soup, attrs={"class": "main-content"})
classes = methods.find_all("div", main_div, attrs={"class":"index-section"})[1:] #remove first element as it's the menu

for class_item in classes:
    course = {}
    # different attributes of the details are accessed by accessing different 'td's within the table of info
    info = methods.find_all("td",class_item,attrs={"class":"camptd"})
    course['URL'] = base_url + "#" + class_item['data-url-id']
    course['Title'] = methods.find('h1', class_item).getText()
    course['Topic'] = info[1].getText()[7:] # bracket at end simply removes the 'Topic:' from the text
    course['SkillLevel'] = info[3].getText()[13:]
    course['CourseType'] = 'Summer Camp'
    age_range = info[0].getText()[5:]
    if age_range.find("-") != -1: #e.g, 5-10 would be 5 minimum with 10 maximum
        age_range = age_range.split("-")
        course['MinimumAge'] = age_range[0]
        course['MaximumAge'] = age_range[1]
    elif age_range.find("+") != -1: #e.g, 10+ would be 10 minimum with no maximum
        course['MinimumAge'] = age_range[:-1]
        course['MaximumAge'] = -1
    else: #If neither of those conditions are met, then leave it as no age restriction
        course['MinimumAge'] = -1
        course['MaximumAge'] = -1

    desc = ""
    try:
        desc = methods.next_tag(methods.find("h2", class_item)).getText()
    except AttributeError as attr_err:
        desc = ""
    course['Description'] = desc
    course['Provider'] = 'The Coder School'
    course['Locations'] = ['1101 106th Ave NE #15']

    csv.append(course)

import pandas as pd

df = pd.DataFrame(csv)
df.to_csv('csv\\course_coderschool.csv', index=False,encoding='utf-8')

print('Complete')
