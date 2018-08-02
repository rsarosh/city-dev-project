import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import time

def getCourseType(title):
    if('One-on-One' in title):
        return 'Computer Basic Course'
    elif 'Class' in title or 'class' in title:
        return 'Course'
    elif 'lab' in title or 'Lab' in title:
        return 'Lab'
    else:
        return 'Workshop'

def getSkillLevel(title):
    title = str(title).lower()
    if 'advanced' in title or 'advance' in title:
        return 'Advanced'
    else: 
        return 'Beginners' 

def getMaxAge(age_group):
    age_group = str(age_group).lower()
    if '50+' in age_group or 'seniors' in age_group:
        return '50+'
    elif 'adults' in age_group:
        return 50
    elif 'teens' in age_group:
        return 18
    elif 'tweens' in age_group:
        return 12
    else:
        return -1

def getMinAge(age_group):
    age_group = str(age_group).lower()
    if '50+' in age_group or 'seniors' in age_group:
        return 50
    elif 'adults' in age_group:
        return 19
    elif 'teens' in age_group:
        return 13
    elif 'tweens' in age_group:
        return 10
    else:
        return -1


if __name__ == "__main__":
    print('Program running...')
    base_url = 'https://kcls.bibliocommons.com'
    driver = webdriver.Chrome()

    '''paratial url for each library link.
    Each library link couldn't be scrapped to get 
    every location so their manually inserted.
    Every single libray and their courses will have their own individual
    csv file'''
    #A total of 27 library urls
    kcls_library_urls = ['/events/search/fq=branch_location_id:(1489)&fq=types:(567990aa9fdb8abb6200c819)', #Alogona Library  
                        '/events/search/fq=branch_location_id:(1490)&fq=types:(567990aa9fdb8abb6200c819)',  #Auburn
                        '/events/search/fq=branch_location_id:(1492)&fq=types:(567990aa9fdb8abb6200c819)',  #Bellevue
                        '/events/search/fq=branch_location_id:(1493)&fq=types:(567990aa9fdb8abb6200c819)',  #Bothell
                        '/events/search/fq=branch_location_id:(1495)&fq=types:(567990aa9fdb8abb6200c819)',  #Burien
                        '/events/search/fq=branch_location_id:(1497)&fq=types:(567990aa9fdb8abb6200c819)',  #Convington
                        '/events/search/fq=branch_location_id:(1513)&fq=types:(567990aa9fdb8abb6200c819)',  #Issaquah
                        '/events/search/fq=branch_location_id:(1519)&fq=types:(567990aa9fdb8abb6200c819)',  #Kenmore Lib
                        '/events/search/fq=branch_location_id:(1520)&fq=types:(567990aa9fdb8abb6200c819)', #kent library
                        '/events/search/fq=branch_location_id:(1517)&fq=types:(567990aa9fdb8abb6200c819)', #Kingsgate Libray
                        '/events/search/fq=branch_location_id:(1521)&fq=types:(567990aa9fdb8abb6200c819)', #Lake Forest Park
                        '/events/search/fq=branch_location_id:(1522)&fq=types:(567990aa9fdb8abb6200c819)', #Lake Hills
                        '/events/search/fq=branch_location_id:(1527)&fq=types:(567990aa9fdb8abb6200c819)', #Maple valley library
                        '/events/search/fq=branch_location_id:(1525)&fq=types:(567990aa9fdb8abb6200c819)', #Mercer Island Libray
                        '/events/search/fq=branch_location_id:(1529)&fq=types:(567990aa9fdb8abb6200c819)', #Newport Way
                        '/events/search/fq=branch_location_id:(1528)&fq=types:(567990aa9fdb8abb6200c819)', #North Bend
                        '/events/search/fq=branch_location_id:(1533)&fq=types:(567990aa9fdb8abb6200c819)', #Redmond
                        '/events/search/fq=branch_location_id:(1556)&fq=types:(567990aa9fdb8abb6200c819)', #Renton library
                        '/events/search/fq=branch_location_id:(1557)&fq=types:(567990aa9fdb8abb6200c819)', #Renton Highland
                        '/events/search/fq=branch_location_id:(1532)&fq=types:(567990aa9fdb8abb6200c819)', #Richmond beach
                        '/events/search/fq=branch_location_id:(1534)&fq=types:(567990aa9fdb8abb6200c819)', #Sammamish Libray
                        '/events/search/fq=branch_location_id:(1535)&fq=types:(567990aa9fdb8abb6200c819)', #Shoreline Library
                        '/events/search/fq=branch_location_id:(1546)&fq=types:(567990aa9fdb8abb6200c819)', #Valley View
                        '/events/search/fq=branch_location_id:(1545)&fq=types:(567990aa9fdb8abb6200c819)', #Vashon Library
                        '/events/search/fq=branch_location_id:(1547)&fq=types:(567990aa9fdb8abb6200c819)', #White center
                        '/events/search/fq=branch_location_id:(1549)&fq=types:(567990aa9fdb8abb6200c819)'  #Woodmont
                        ]

    for library_url in kcls_library_urls:
        driver.get(base_url + library_url)
        time.sleep(5) #stops the program and lets the browser load for 3 seconds
        innerHTML = driver.execute_script("return document.body.innerHTML")
        soup = BeautifulSoup(innerHTML, "html5lib")
        #Prints the Raw HTML code.
        #print(soup)'

        csv = []
        library_Name = "" #name for csv file

        course_column = soup.find('div', attrs={'class':'col-sm-9 event-results'})
        #print(course_column)
        all_course_sections = course_column.find_all('div', attrs={'class':'row event-row'})
        #print(all_course_sections)

        course_urls = []
        for course in all_course_sections:
            url = base_url + course.find('a')['href']
            course_urls.append(url)

        csv = []
        count = 0
        #Course_info: URL, Title, Topic, SkillLevel, CourseType, MinimumAge, MaximumAge, Description, Provider, Location
        for url in course_urls:
            course_info = {}
            
            url = course_urls[0]
            driver.get(url)
            time.sleep(7)
            innerHTML = driver.execute_script("return document.body.innerHTML")
            soup = BeautifulSoup(innerHTML, "html5lib")    

            #1 Course URL
            course_info['URL'] = url

            #2 Course title
            title_section = soup.find('div', attrs={'class':'event-summary-title'})
            title = title_section.find('span').getText()
            title = str(title).strip()
            #print(title)
            course_info['Title'] = title

            #3 course topic 
            basic_course_info = soup.find('div', attrs={'class','event-facets-list'})
            #print(basic_course_info)
            topic = basic_course_info.find('a').getText()
            #print(topic)
            course_info['Topic'] = topic

            #4 course Skill level
            course_info['SkillLevel'] = getSkillLevel(title)

            #5 course type
            courseType = getCourseType(title) 
            #print(courseType)
            course_info['CourseType'] = courseType

            #6 Age
            all_basic_course_info = basic_course_info.find_all('dd')
            #print(all_basic_course_info)
            age_group = all_basic_course_info[0].getText()
            #print(age_group)

            maximumAge = getMaxAge(age_group) 
            minimumAge = getMinAge(age_group)
            #print(maximumAge, minimumAge)
            course_info['MaximumAge'] = maximumAge
            course_info['MinimumAge'] = minimumAge

            #7 course description
            description = soup.find('div', attrs={'class','event-decription-content'}).getText()
            #print(description)
            course_info['Description'] = description

            #8 course provider
            course_info['Provider'] = 'King County Library System'
            #9 course location
            location_section = soup.find('div', attrs={'class':'collapsible'})
            #print(location_section)
            location = location_section.find('a',attrs={'class':'primary-link'}).getText()    
            #print(location)
            library_Name = str(location)
            course_info['Location'] = location
            count += 1
            print(library_Name, 'Completed', count, 'out of', len(course_urls), 'courses')
            csv.append(course_info)
        #--------------------------------------------------#
        #Converting list of dictionary into CSV
        import pandas as pd

        df = pd.DataFrame(csv)
        library_Name += "~KingCountyLibrary"
        df.to_csv('course_'+library_Name+'.csv', index=False, encoding='utf-8')
        library_Name = ""
        print('Complete!')
    driver.close()

