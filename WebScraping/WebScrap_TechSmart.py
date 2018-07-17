import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def getSkillLevel(prerequisites):
    if 'No prior coding experience' in prerequisites:
        return 'Beginner'
    else:
        return 'Advanced'

if __name__ == "__main__":
    print('Program running...')
    base_url = 'http://www.techsmartkids.com/teachers/'
    csv = []

    driver = webdriver.Chrome()
    driver.get(base_url)
    innerHTML = driver.execute_script("return document.body.innerHTML")
    soup = BeautifulSoup(innerHTML, "html5lib")
    #print(soup)

    #targeting the section where all the courses are at.
    bootcamp_selection = soup.find('div',attrs={'class':'col-xs-12 ts-card'})
    #print(bootcamp_selection)

    driver.close()
    
    unordered_list = bootcamp_selection.find('ul')
    courses = unordered_list.find_all('li')
    print(courses)
    course_urls = []
    for info in courses:
        #want to skip first index since it's unnessary.
        if courses[0] != info:
            url = base_url + '#' + info['data-ts-id']
            course_urls.append(url)




    csv = []
    #Course_info: URL, Title, Topic, SkillLevel, CourseType, MinimumAge, MaximumAge, Description, Provider, Location
    for url in course_urls:
        #url = course_urls[0]
        course_info = {}

        driver = webdriver.Chrome()
        driver.get(url)
        innerHTML = driver.execute_script("return document.body.innerHTML")
        soup = BeautifulSoup(innerHTML, "html5lib")
        driver.close()

        #1) Course URL
        course_info['URL'] = url

        #2) course Title
        title = soup.find('h1', attrs={'class':'ts-info-box-header-title ts-course-title'}).getText()
        course_info['Title'] = title
        #print(soup)

        #3) Course Topic
        course_info['Topic'] = 'Coding'

        #4)Course SkillLevel
        prerequisites = soup.find('span', attrs={'class':'ts-course-prerequisites'}).getText()
        skillLevel = getSkillLevel(prerequisites)
        course_info['SkillLevel'] = skillLevel

        #5)Course Type
        course_info['CourseType'] = 'Bootcamp/Course'

        #6) Age
        course_info['MaximumAge'] = -1
        course_info['MinimumAge'] = -1

        #7) Description
        course_box = soup.find('div', attrs={'class':'ts-info-box-description'})
        description = course_box.find('p')
        course_info['Description'] = description.getText()

        #8) Provider
        course_info['Provider'] = 'Tech Smart'

        #9) Location
        course_info['Location'] = ['Seattle']

        csv.append(course_info) 

    #--------------------------------------------------#
    #Converting list of dictionary into CSV
    import pandas as pd

    df = pd.DataFrame(csv)
    df.to_csv('csv\\course_TechSmartKids.csv', index=False, encoding='utf-8')

    print('Complete!')