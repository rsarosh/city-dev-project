import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import time

def getMaximumAge(age_groups):
    if 'All_ages' in age_groups or 'Senior 55+' in age_groups:
        return '55+'
    elif 'Adults' in age_groups:
        return 55
    elif 'Teens' in age_groups:
        return 19
    else:
        return -1

def getMinimumAge(age_groups):
    if 'All_ages' in age_groups:
        return 6
    elif 'Teens' in age_groups:
        return 13
    elif 'Adults' in age_groups:
        return 20
    elif 'Senior 55+' in age_groups:
        return 55
    else:
        return -1

if __name__ == "__main__":
    print('Program running...')
    base_url = 'https://calendar.piercecountylibrary.org/'
    csv = []

    driver = webdriver.Chrome()
    driver.get(base_url + 'events?term=get%20smart')
    time.sleep(3) #wait time inorder to full load the webpage before info is proccessed.
    innerHTML = driver.execute_script("return document.body.innerHTML")
    soup = BeautifulSoup(innerHTML, "html5lib")
    #print(soup)

    event_section = soup.find('div',attrs={'class':'events-right'})
    event_body = event_section.find('div',attrs={'class':'events-body'})
    #print(event_body)
    event_urls = event_body.find_all('a')

    '''geting the URL from the tag and storing in list: course_urls.'''
    course_urls = []
    index = 0
    for tag in event_urls:

        course_url = base_url + tag['href'] #getting the link by adding the base and remaing url which is in URF
        course_urls.append(course_url)
        #Print check to see if the url is correct.
        #print(course_url)

    csv = []
    for url in course_urls:
        #url = course_urls[key] #test working with just the first link.
        course_info = {}

        driver.get(url)
        time.sleep(2)   #wait time inorder to full load the webpage before info is proccessed.
        innerHTML = driver.execute_script("return document.body.innerHTML")
        soup = BeautifulSoup(innerHTML, "html5lib")

        #1) Course URL
        course_info['URL'] = url

        #2) Course Title
        all_h2_tags = soup.find_all('h2')
        #print(all_h2_tags)  
        course_info['Title'] =  all_h2_tags[0].getText()

        #3) Course Topic 
        course_info['Topic'] = 'Computing, Tech help'

        #4) Course SkillLvel
        course_info['SkillLevel'] = 'Beginner-Advance'

        #5) Course type
        course_info['CourseType'] = 'Course'

        #6) Ages 
        age_group_location = soup.find('em')
        age_groups = age_group_location.find_all('a')
        for i in range(len(age_groups)):
            age_groups[i] = age_groups[i].getText()
        #print(age_groups)
        maxAge = getMaximumAge(age_groups)
        minAge = getMinimumAge(age_groups)
        course_info['MaximumAge'] = maxAge
        course_info['MinimumAge'] = minAge
        #print(minAge, maxAge)

        #7) Description     
        all_p_tags = soup.find_all('p')
        #print(all_p_tags)   
        course_info['Description'] = all_p_tags[3].getText()

        #8)Provider
        course_info['Provider'] = 'Pierce County Library'

        #9) Location
        locations = soup.find_all('a',attrs={'href':'#branch'})
        locations = [locations[1].getText()]
        #print(locations)
        course_info['Locations'] = locations

        csv.append(course_info)



    driver.close()
#--------------------------------------------------#
    #Converting list of dictionary into CSV
    import pandas as pd

    df = pd.DataFrame(csv)
    df.to_csv('course_PierceCountyLibrary.csv', index=False, encoding='utf-8')

    print('Complete!')
            



