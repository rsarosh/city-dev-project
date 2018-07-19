'''
Program goes through 3 different websites - do not quit until 'COMPLETE' bar is shown
'''

MAIN_DIV_ID = 'catalog-results' # "main" div that contains all the courses
DIVIDER_CLASS = 'date-divider clearfix' # divs that seperate courses
TITLE_AND_DESCRIPTION_CLASS = 'item-details' # divs that contain the title and description paragraphs
COURSE_TITLE_CLASS = 'medium item-title' # paragraph that displays the course title
COURSE_DATE_INFO_CLASS = 'date-topic-container' # divs that contain the information on the date and type of course

LOCATION_DIV_CLASS = 'location-style' # div that contains all of the location information
ADDRESS_SPAN_CLASS = 'campus-address' # specific span within location div that contains the address

from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import soup_extra_methods as methods
import warnings

base_url = "https://generalassemb.ly/education?where=seattle&topic="

csv = []


topic_pages = [6, 8, 4] # to filter by topic, each one has a unique link id. 6 for Coding, 8 for Data, and 4 for Design
topic_names = ['Coding', 'Data', 'Design']

previous_class_list = [] # there are repeat classes on the website, so if the title already exists don't add it

for topic_num,topic_name in zip(topic_pages,topic_names):
    browser = webdriver.Chrome()
    browser.get(base_url + str(topic_num))
    innerHTML = browser.execute_script("return document.body.innerHTML")

    soup = BeautifulSoup(innerHTML, 'html5lib')

    print('Loaded data from ' + base_url + str(topic_num))

    #Classes are all inside of div with ID 'catalog-results'
    main_div = methods.find('div', soup, attrs={'id':MAIN_DIV_ID})

    class_listing = methods.surface_search(main_div)

    if(len(class_listing) < 2):
        warnings.warn('Classes not found on page '+base_url+str(topic_num))

    num = 0
    for class_item in class_listing:
        num += 1
        if methods.safe_attr_access(class_item, 'class') == -1: # if the div is not a divider
            url = methods.safe_attr_access(methods.find('a', class_item), 'href') # find the link within the div and go to it
            if url == -1:
                warnings.warn('Link not found for course '+str(class_item))
            else:
                # find the title and the description of the course
                title_and_description = methods.find('div', class_item, attrs={'class': TITLE_AND_DESCRIPTION_CLASS});
                title = methods.find('p', title_and_description, attrs={'class': COURSE_TITLE_CLASS});
                description = methods.next_tag(title)

                if not title.getText().lower() in previous_class_list: # only create a new course if the title is new
                    # if the text 'course' is found within the div that contains the dates, then it is a course rather than seminar
                    course_type = 'Seminar / Event'
                    course_type_container = methods.find('div', class_item, attrs={'class': COURSE_DATE_INFO_CLASS}).getText()
                    if 'course' in course_type_container.strip().lower():
                        course_type = 'Course'

                    locations = ['Unknown'] # if no location info is found, write 'unknown' for it

                    if course_type != 'Course': # inconsistent and difficult to find location of courses, so only non=courses get location info
                        r2 = requests.get(url)
                        soup2 = BeautifulSoup(r2.text, 'html5lib')
                        loc_div = soup2.find('div', attrs={'class': LOCATION_DIV_CLASS})
                        if loc_div:
                            location = methods.find('span', loc_div, attrs={'class': ADDRESS_SPAN_CLASS}).getText()
                            locations[0] = location
                        else: # if there's no location class, that means the course is online
                            locations[0] = 'Online'

                    # record all of the information
                    course = {}
                    course['URL'] = url
                    course['Title'] = title.getText().strip()
                    course['Topic'] = topic_name
                    course['SkillLevel'] = 'Intermediate'
                    course['CourseType'] = course_type
                    course['MinimumAge'] = -1 # no age information found
                    course['MaximumAge'] = -1
                    course['Description'] = description.getText().strip()
                    course['Provider'] = 'General Assembly'
                    course['Locations'] = locations

                    csv.append(course)
                    previous_class_list.append(title.getText().strip().lower())
        print(str(num) + " / " + str(len(class_listing)))
    browser.close()
# create csv file
print("Finished scraping...")

import pandas as pd

df = pd.DataFrame(csv)
df.to_csv('csv\\course_generalassembly.csv', index=False,encoding='utf-8')

print('Complete')