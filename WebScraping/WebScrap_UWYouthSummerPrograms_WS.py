#Program Completed 
import requests 
from bs4 import BeautifulSoup

#Gets a string with the description of the course and 
def getTopics(description):
    topics = []
    if("Engineering" in description  or "engineering" in description):
        topics.append("Engineering")
    if("Art" in description or "art" in description):
        topics.append("Art")
    if("Coding" in description or "coding" in description):
        topics.append("Code")
    #maybe needs more topics'
    #print(topics)
    return topics

#Takes in a string holding the info of the website
#returns the courseType if a certain keyword is founded.
def getCourseType(description):
    courseType = ""
    if("course" in description):
        courseType = "Course"
    elif("camp" in description):
        courseType = "Camp"
    elif("program" in description):
        courseType = "Program"
    else:
        courseType = ""
    #print(courseType)
    return courseType

#Takes a string holding the program details(Grade level, cost, & refund deadline)
#parse out Grade level and returns it as a string.
def getGradeLevel(program_details):
    grade_index = program_details.find("Grades:")
    cost_index = program_details.find("Cost:")
    return program_details[grade_index:cost_index]

#Takes in a string that hold info on the grade level and returns the Minimum Age level. 
def getMinimumAge(grade_levels):
    #Format: "Grades: X-Y "
    dash_index = grade_levels.find("–")
    min_grade_level = int(grade_levels[8:dash_index])
    #print(min_grade_level)
    age = min_grade_level + 6
    #print(age)
    return age

#Takes in a string that hold info on the grade level and returns the Maximum Age level. 
def getMaximumAge(grade_levels):
    #Format: "Grades: X-Y "
    dash_index = grade_levels.find("–")
    max_grade_level = int(grade_levels[dash_index+1:len(grade_levels)-1])
    #print(max_grade_level)
    age = max_grade_level + 6
    #print(age)
    return age

if __name__ == "__main__":
    print('Program running...')
    base_url = 'https://www.summer-camp.uw.edu'
    csv = []

    r = requests.get(base_url + '/camps-courses/')
    soup = BeautifulSoup(r.text, 'html5lib')
    #Prints the Raw HTML code.
    #print(soup)

    course_tags = soup.find_all('a', attrs={'id':'linkCourse'})
    #print(len(course_tags))

    '''geting the URL from the tag and storing in list: course_urls.'''
    course_urls = []
    for tag in course_tags:
        course_url = base_url + tag['href'] #getting the link by adding the base and remaing url which is in URF
        course_urls.append(course_url)
        #Print check to see if the url is correct.
        #print(course_url)

    '''information that need to be obtained: CourseType, Description, Locations, MaximumAge, MinimumAge, Provider, SkillLevel, Title, Topic, & URL'''
    for url in course_urls:
        course_info = {}

        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html5lib')

        #1) URL for the course
        course_info['URL'] = url

        #2) Title for the course
        website_body_text = soup.find('div', attrs={'class':'uw-body-copy'})
        title = website_body_text.find('h1').getText()
        course_info['Title'] = title
        #print(title)

        #3) Topics - using the description to detemine the topics
        course_info['Topics'] = getTopics(soup.find('p').getText())

        #4) Skill level - initlizing it to just Beginner & Advanced.
        course_info['SkillLevel'] = "Beginner-Advanced"

        #5) Course Type
        course_info['CourseType'] = getCourseType(website_body_text.getText())

        #6) Age for the course (Min & Max Ages)
        '''The course bases the ages by grade levels, and doesn't have tag for just the grades.
                1)taking the whole div tag as string
                2)break it apart to get "Grade: X - Y" (x & y reprsents a grade)  
                3)Then take X & Y and change to actual ages.'''
        course_details_blocks = soup.find('div', attrs={'class':'course-setails-card'})
        #print(course_details_blocks.getText())
        grade_levels = getGradeLevel(course_details_blocks.getText())
        #print(grade_levels)

        course_info['MaximumAge'] = getMaximumAge(grade_levels)
        course_info['MinimumAge'] = getMinimumAge(grade_levels)

        #7) Description
        description = soup.find('p').getText()
        course_info['Description'] = description
        #print(description)

        #8) Course provider
        course_info['Provider'] = 'UW Summer Youth Programs'

        #9) Locations
        dates_and_time_section = website_body_text.find('div')
        tables = dates_and_time_section.find_all('table')
        locations = []
        for table in tables:
            location_section = table.find('td', attrs={'class':"matrixBG matrixBorderBottom"})
            location = location_section.find('a').getText()
            if(location not in locations):
                locations.append(location)
        #print(locations)
        course_info['Locations'] = locations

        csv.append(course_info)

    #--------------------------------------------------#
    #Converting list of dictionary into CSV
    import pandas as pd

    df = pd.DataFrame(csv)
    df.to_csv('csv\\course_UWSummerYouthPrograms.csv', index=False, encoding='utf-8')

    print('Complete!')


