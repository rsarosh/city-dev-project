'''
The topic is not included as there was no good way of categorizing them

The scraper uses selenium and XPath to click two buttons, allowing it to access the proper course info. If this XPath changes, the
program will need to be update accordingly
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup
import soup_extra_methods as methods
import warnings
import re

base_url = "https://class.seattle.gov/parks/Activities/ActivitiesAdvSearch.asp"

browser = webdriver.Chrome()
browser.get(base_url)

def wait_until_loaded(id):
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, id)))
    if not element:
        warnings.warn('Element '+id+' not found while loading page')

# click on the 'Academic Preparedness' category
link = browser.find_element_by_xpath('//*[@id="browser"]/li[1]/span/a')
link.click()

# wait for the link to fully be opened
wait_until_loaded('activity-1-342')

# open the 'Computer Training' subcategory
link = browser.find_element_by_xpath('//*[@id="activity-1-342"]/span[1]/a')
link.click()

# wait again...
wait_until_loaded('activity-course-row')

# NOW begin scraping

innerHTML = browser.execute_script('return document.body.innerHTML')

soup = BeautifulSoup(innerHTML, 'html5lib')

print('Loaded data from ' + base_url)

csv = []

course_div = methods.find('div', methods.find('div', soup, attrs={'id':'activity-1-342'}), attrs={'id':'activity-detail-table'})
courses = methods.find_all('tr', course_div, attrs={'id':'activity-course-row'})

for course_item in courses:
    # The title is the first div within the 'Course' tr, and the description is included in the 'title' attribute of the same tag
    title_and_desc = methods.find('div', methods.find('td', course_item, attrs={'headers':'Course'}))
    title = title_and_desc.getText()
    desc = methods.safe_attr_access(title_and_desc, 'title')

    # The age is included within the title, so simple text formatting will isolate it
    age = title[title.find('(')+1:title.find(')')]
    age = age.split('-')
    age = [re.findall(r'\d+',num) for num in age]

    # Sometimes the description includes the instructor/location, so crop that out if so
    desc = desc[:desc.lower().find('instructor:')]

    # The location is found through the 'Complex' header, and then formatted
    location = methods.find('td', course_item, attrs={'headers':'Complex'})
    location = ''.join(methods.find('br', location).next_siblings)
    location = location.strip()

    course = {}
    course['URL'] = 'https://class.seattle.gov/parks/Activities/ActivitiesAdvSearch.asp'
    course['Title'] = title[:title.find('(')].strip()
    course['Topic'] = '' # INCOMPLETE
    course['SkillLevel'] = 'Beginner'
    course['CourseType'] = 'Course'
    course['MinimumAge'] = age[0]
    course['MaximumAge'] = age[1]
    course['Description'] = desc.strip()
    course['Provider'] = 'Seattle Parks and Recreation'
    course['Locations'] = [location]
    csv.append(course)

# create csv file
import pandas as pd

df = pd.DataFrame(csv)
df.to_csv('csv\\course_rectech.csv', index=False,encoding='utf-8')

print('Complete')