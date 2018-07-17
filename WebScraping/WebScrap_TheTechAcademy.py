#completed
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    print('Program running...')
    base_url = 'https://learncodinganywhere.com/CourseOverViews'
    csv = []

    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, 'html5lib')
    #Prints the Raw HTML code.
    #print(soup)

    ''' Getting the courses on the webpage.'''
    courses_container = soup.find('div', attrs={'class':'container mt-20 mb-60'})
    courses_column = courses_container.find('div', attrs={'class':'col-sm-8'})
    courses = courses_column.find_all('div',attrs={'class':'course-list'})
    #print(courses)
    '''Course_info: URL, Title, Topic, SkillLevel, CourseType, MinimumAge, MaximumAge, Description, Provider, Location'''
    for course in courses:
        #course = courses[0]
        course_info = {}
        #1) URL
        course_info['URL'] = base_url
        #2) Title
        course_details = course.find('div',attrs={'class':'course-detail'})
        course_title = course_details.find('h4').getText()
        course_info['Title'] = course_title
        #print(course_title)

        #3) Topics
        course_info['Topics'] = 'Coding'

        #4) SkillLevel
        course_info['SkillLevel'] = 'Beginner-Advanced'

        #5) CourseType
        course_info['CourseType'] = 'Course'

        #6) Age
        course_info['MaximumAge'] = -1
        course_info['MinimumAge'] = -1

        #7) Description
        course_description_section = course.find('div', attrs={'class':'panel panel-default'})
        course_panel_list = course_description_section.find_all('div')
        course_description_list = course_panel_list[1].find_all('div',attrs={'class':'panel-body'})
        course_descrip_paragh_list = course_description_list[1].find_all('p')
        description = ""
        for paragh in course_descrip_paragh_list:
            description += paragh.getText() 
            if(paragh != course_descrip_paragh_list[-1]):
                description +="\n\n"
        course_info['Description'] = description

        #8) Provide
        course_info['Provider'] = 'The Tech Academy'

        #9) Locations
        course_info['Locations'] = ['Portland', 'Seattle', 'Denver']

        csv.append(course_info)

    #--------------------------------------------------#
    #Converting list of dictionary into CSV
    import pandas as pd

    df = pd.DataFrame(csv)
    df.to_csv('course_TheTechAcademy.csv', index=False, encoding='utf-8')

    print('Complete!')