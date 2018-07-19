from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import soup_extra_methods as methods
import warnings

base_url = "https://www.nhseattle.com/resources/free-webinars"
csv = []

browser = webdriver.Chrome()
browser.get(base_url)

pages = []

#Access the different pages using Selenium, and load each one as a seperate page to parse
scraping = True
num = 0
while scraping:
    num += 1
    html = browser.execute_script("return document.body.innerHTML")
    pages.append(html)
    try:
        button = browser.find_element_by_link_text("Next")
    except NoSuchElementException:
        scraping = False # break out of loop if its the last page
    else:
        button.click()
    if num > 15: # if there are more than 15 pages, assume something is wrong
        warnings.warn('While loop broken: '+num+" pages found")
print("Loaded data from "+base_url)

key_words = ["digital", "computer", "technolog", "linkedin", "linked-in"]

#Now parse the pages in beautiful soup and record the courses into the CSV
for page in pages:
    soup = BeautifulSoup(page, 'html5lib')
    courses = methods.find_all('div', soup, attrs={'class':'panel panel-default'})

    for course in courses:
        title = methods.find('p', course, attrs={"class":"blue-inverse"})
        # go down from the title until the paragraph saying 'presenter', and then the paragraph after that is the description
        description = title
        for num in range(8):
            description = description.nextSibling
        title = title.getText()
        description = description.getText()

        # for some reason classes were repeating and I couldn't figure out why, so I just set up a simple check to make sure the title is not already in the CSV
        title_already_exists = False
        for dict in csv:
            if dict['Title'].strip().lower() == title.strip().lower():
                title_already_exists = True

        if not title_already_exists:
            is_tech = False

            # if a phrase from the key_words is included in the title, then set it as tech
            word_list = title.lower().strip()
            for word in key_words:
                if word in word_list:
                    is_tech = True

            # checks for the individual word 'IT" (this section is seperate because IT is case-sensitive, must be a unique word, and also includes the description)
            title_individual_words = title.split(" ") + description.split(" ")
            if 'IT' in title_individual_words:
                is_tech = True

            if is_tech is True:
                dictionary = {}
                dictionary['URL'] = base_url
                dictionary['Title'] = title
                dictionary['Topic'] = 'Digital Literacy'
                dictionary['SkillLevel'] = 'Beginner'
                dictionary['CourseType'] = 'Online Seminar'
                dictionary['MinimumAge'] = -1
                dictionary['MaximumAge'] = -1
                dictionary['Description'] = description
                dictionary['Provider'] = 'NHSeattle'
                dictionary['Locations'] = []

                csv.append(dictionary)

import pandas as pd

df = pd.DataFrame(csv)
df.to_csv('csv\\course_nhswebinar.csv', index=False,encoding='utf-8')

print('Complete')