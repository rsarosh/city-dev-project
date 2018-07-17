#Completed
import requests
from bs4 import BeautifulSoup
#Takes in a course type list and returns a string hold the course types it is.
#Techsherpas has In-classroom learning(ICL) or Virtual Live Training(VLT)
def getCourseType(course_type_list):
    course_type = []
    for info_types in course_type_list:
        #print(info_types)
        info_types_list = info_types.find_all('span')
        #print(info_types_list)
        for t in info_types_list: #t = type
            text = t.getText()
            #print(text)
            if text not in course_type:
                course_type.append(text)
    course_type_string = ""
    if 'ICL' in course_type:
        course_type_string = 'In-Classroom Learning'
    if 'VLT' in course_type:
        if "" != course_type_string:
            course_type_string += " or "
        course_type_string += 'Virtual Live Training'
    #print(course_type_string)
    return course_type_string

def getCourseLocations(course_location_section):
    locations = []
    for CLS in course_location_section:
        location_selection = CLS.find('select')
        location_list = location_selection.find_all('option')
        #The first two index in Location_list is unnessary.
        location_list = location_list[2:]
        #print(location_list)
        for location in location_list:
            text = location.getText()
            if text not in locations:
                locations.append(text)
    #print(locations)
    return locations

if __name__ == "__main__":
    print('Program running...')
    base_url = 'https://www.techsherpas.com/it-training-centers/seattle-wa/'
    csv = []

    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, 'html5lib')
    #Prints the Raw HTML code.
    #print(soup)
    courses_block = soup.find('div', attrs={'id':'builder-module-5714e91a8eda7-background-wrapper'})
    #print(courses_block)
    courses_inner_block = courses_block.find('div',attrs={'class':'loop-content search-product burn-location'})
    course_tags = courses_inner_block.find_all('a')
    #print(len(course_tags))

    '''geting the URL from the tag and storing in list: course_urls.'''
    course_urls = []
    for tag in course_tags:
        course_url = tag['href'] #getting the link by adding the base and remaing url which is in URF
        illegal_link1 = bool('javascript:void(0)' not in course_url)
        illegal_link2 = bool('https://www.techsherpas.com/cart/' not in course_url)
        if illegal_link1 and illegal_link2:
            extra_index = course_url.find('javascript:void(0)')
            course_urls.append(course_url)
            #Print check to see if the url is correct.
            #print(course_url)

    csv = []
    '''Course_info: URL, Title, Topic, SkillLevel, CourseType, MinimumAge, MaximumAge, Description, Provider, Location'''
    count = 0
    for url in course_urls:
        course_info = {}

        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html5lib')

        #1) Course URL
        course_info['URL'] = url

        #2) course Title:
        page_title = soup.find('h1', attrs={'class':'pgtitle'}).getText()
        course_info['Title'] = page_title
        #print(page_title)

        #3) Topics:
        course_body = soup.find('body', attrs={'id':'builder-layout-5708247b15877'})
        course_overview_section = course_body.find('div', attrs={'class':'woocommerce-Tabs-panel woocommerce-Tabs-panel--short_desc panel entry-content wc-tab'})
        course_topic_overview = course_overview_section.find('p').getText()
        #topic format: About this <Topic>
        course_index = course_topic_overview.find('Course')
        if 'About this' in course_topic_overview:
            topic = course_topic_overview[11:course_index+6]
        course_info['Topic'] = topic
        #print(topic)

        #4)skill-level
        if 'Introduction' in page_title or 'introduction' in page_title:
            course_info['SkillLevel'] = 'Beginner'
        else:
            course_info['SkillLevel'] = 'Advanced' 

        #5)CourseType
        course__table = soup.find('table',attrs={'class':'tg'})
        course_type_section = course__table.find_all('td', attrs={'class':'tg-yw4l class_info leg_col legend'})
        #print(course_type_section)
        course_info['CourseType'] = getCourseType(course_type_section)

        #6)Ages - Age could not be found on webpage
        course_info['MaximumAge'] = -1
        course_info['MinimumAge'] = -1

        #7) Description
        course_overview_paragraphs = course_overview_section.find_all('p')
        description = ""
        if(len(course_overview_paragraphs) == 2):
            description = course_overview_paragraphs[1].getText()
        else:
            description = course_overview_paragraphs[1].getText() + "\n\n" + course_overview_paragraphs[2].getText()
        #print(description)
        course_info['Description'] = description

        #8) Provider
        course_info['Provider'] = 'Tech Sherpas'

        #9) Locations
        course_location_section = course__table.find_all('td', attrs={'class':'tg-yw4l loc'})
        course_info['Locations'] = getCourseLocations(course_location_section)

        csv.append(course_info)
        count += 1
        print('Completed:', count,'out of', len(course_urls), url) 

    #--------------------------------------------------#
    #Converting list of dictionary into CSV
    import pandas as pd

    df = pd.DataFrame(csv)
    df.to_csv('csv\\course_TechSherpas.csv', index=False, encoding='utf-8')

    print('Complete!')
