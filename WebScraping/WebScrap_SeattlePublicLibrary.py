'''

SPL hosts their online calendar through Trumba. Trumba offers unformatted but easily accessible data on their website
    and that is was is used. If this script ever breaks, look for the RSS feed from https://www.spl.org/programs-and-services/learning/technology-skills/technology-skills-calendar
'''

import requests
from bs4 import BeautifulSoup
import soup_extra_methods as methods

base_url = "https://www.trumba.com/events-calendar/wa/seattle/seattle/library/seattle-public-library/seattle-reads/washington-center-for-the-book/story/author/tour/class/talk-time/calendar_of_events__classes";

r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html5lib')

print('Loaded data from ' + base_url)

csv = []

courses = methods.find_all('div', soup, attrs={'class':'vevent'}) # each course is simply a 'vevent' class

title_list = [] # List of all titles to remove repeats (NOTE: repeated titles can still have different locations)
title_key_terms = ['technology', 'computer', 'microsoft'] # key terms to be checked to determine if the class is technology based
title_key_words = ['tech', 'Tech', 'IT'] # these terms are case sensitive and must be unique words seperated by spaces
for course_item in courses:
    title = methods.find('h2', course_item).getText()

    # check if it's a technology course based on key words and terms in the title
    is_technology = False
    for key_term in title_key_terms:
        if key_term.lower() in title.lower():
            is_technology = True
    for key_word in title_key_words:
        if key_word in title.split(' '):
            is_technology = True

    if is_technology:
        if not title.lower() in title_list:
            title_list.append(title.lower())
            course = {}
            course['URL'] = 'https://www.spl.org/programs-and-services/learning/technology-skills/technology-skills-calendar'
            course['Title'] = title
            course['Topic'] = 'Digital Literacy'
            course['SkillLevel'] = 'Beginner'
            # course type is either a class, a lab or an exam
            course_type = 'Class'
            if 'lab' in title.lower().split(' '):
                course_type = 'Lab'
            if 'exam' in title.lower().split(' '):
                course_type = 'Exam'
            course['CourseType'] = course_type
            course['MinimumAge'] = -1
            course['MaximumAge'] = -1
            # remove 'Description:' from the description
            description = methods.format_string(methods.find('span', course_item, attrs={'class':'tcfDescription'}).getText())
            description = description[12:]
            course['Description'] = description
            course['Provider'] = 'Seattle Public Library'
            # remove 'Where:' from the location
            location = methods.find('span', course_item, attrs={'class':'tcfWhere'}).getText()
            location = location[7:][:-1]
            course['Locations'] = [location]
            csv.append(course)
        else:
            # if its a repeated title, check if its a new location and if it is add it to the list
            location = methods.find('span', course_item, attrs={'class':'tcfWhere'}).getText()[7:][:-1]
            for course in csv:
                if  course['Title'] == title:
                    if not location in course['Locations']:
                        course['Locations'].append(location)

# create csv file
import pandas as pd

df = pd.DataFrame(csv)
df.to_csv('csv\\course_seattlepubliclibrary.csv', index=False,encoding='utf-8')

print('Complete')