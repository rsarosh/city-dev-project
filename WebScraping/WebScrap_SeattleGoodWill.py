import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import time

if __name__ == "__main__":
    print('Program running...')
    base_url = 'https://seattlegoodwill.org'
    csv = []

    r = requests.get(base_url + '/job-training-and-education')
    soup = BeautifulSoup(r.text, 'html5lib')
    #Prints the Raw HTML code.
    #print(soup)

    content_div = soup.find('div', attrs={'class':'content-text'})
    all_location_links = content_div.find_all('a')
    #print(all_location_links)

    location_urls = []
    for tag in all_location_links:
        url = base_url + tag['href']
        location_urls.append(url)
        #print(url)
    
    '''Course_info: URL, Title, Topic, SkillLevel, CourseType, MinimumAge, MaximumAge, Description, Provider, Location'''
    for url in location_urls:
        course_info = {}
        #url = location_urls[0]
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html5lib')
        body_section = soup.find('div', attrs={'class':'content-text'})
        text = str(body_section.getText())
        #print(text)
        if('Computer Classes' in text):
            #print(url)
            #1) url 
            course_info['URL'] = url

            #2)Title 
            cc_all_a_tag = body_section.find_all('a')
            cc_a_tag = cc_all_a_tag[2]
            title = cc_a_tag.getText()
            #print(title)
            course_info['Title'] = title
            
            #3)Topic 
            all_table_tags = body_section.find_all('table')
            computer_courses_table = all_table_tags[0]
            course_topics = computer_courses_table.find_all('tr')
            topics = ''
            for topic in course_topics:
                text = topic.find('p').getText().strip()
                if topic != course_topics[-1]:
                    topics += text + ", "
                else:
                    topics += text
            course_topics
            course_info['Topics'] = topics
            #print(topics)

            #4) SkillLevel:
            course_info['SkillLevel'] = 'Beginner'

            #5) CourseType
            course_info['CourseType'] = 'Course'

            #6) Age
            course_info['MaximumAge'] = -1
            course_info['MinimumAge'] = -1

            #7) Description
            cc_all_a_tag = body_section.find_all('a')
            cc_a_tag = cc_all_a_tag[2]
            #print(cc_a_tag)
            cc_url = base_url + cc_a_tag['href']
            #print(cc_url)
            r = requests.get(cc_url)
            soup2 = BeautifulSoup(r.text, 'html5lib')

            cc_content_div = soup2.find('div', attrs={'class':'content-text'})
            cc_all_p_tags = cc_content_div.find_all('p')
            #print(cc_all_p_tags[2])
            description = cc_all_p_tags[2].getText()
            course_info['Description'] = description

            #8) Provider
            course_info['Provider'] = 'Seattle Good Will'

            #9) Location
            header_div = soup.find('div',attrs={'class':'secondary-hero'})
            header = header_div.find('h2').getText()
            index_job = str(header).find('Job')
            location = header[0:index_job]
            #print(location)
            locations = [location]
            course_info['Location'] = locations

            csv.append(course_info)

#--------------------------------------------------#
    #Converting list of dictionary into CSV
    import pandas as pd

    df = pd.DataFrame(csv)
    df.to_csv('course_SeattleGoodWill.csv', index=False, encoding='utf-8')

    print('Complete!')

    