import requests
from bs4 import BeautifulSoup

def getCourseTopics(description):
    web_publishing = ['web design', 'HTML', 'CSS', 'Javascript', 'PHP', 'Terminal']
    design = ['Creative Suite 6', 'Photoshop', 'Illustrator', 'InDesign']
    digital_video = ['Video Overview', 'iMovie', 'Final Cut Pro', 'Premiere Pro', 'After Effects', 'Movie Maker', 'iDVD Manual', ]
    digital_audio = ['Digitial Audio', 'Audacity', 'Propellerhead Reason', 'Garageband']
    doc = ['Microsoft', 'Excel', 'Word']
    for topic in web_publishing:
        if topic in description:
            return 'Web Publishing'
    for topic in design:
        if topic in description:
            return 'Graphics & Design'
    for topic in digital_video:
        if topic in description:
            return 'Digital Video'
    for topic in digital_audio:
        if topic in description:
            return'Digital Audio'
    for topic in doc:
        if topic in description:
            return 'Microsoft Office'
    return ''

if __name__ == "__main__":
    print('Program running...')
    base_url = 'https://itconnect.uw.edu/learn/workshops/online-tutorials/'
    csv = []

    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, 'html5lib')
    #Prints the Raw HTML code.
    #print(soup)
    main_body = soup.find('div', attrs={'class':'uw-body-copy'})
    course_tags = main_body.find_all('a')
    print(len(course_tags))
    #first link is unessary, so it's removed form the list.
    course_tags.remove(course_tags[0])

    '''geting the URL from the tag and storing in list: course_urls.'''
    course_urls = []
    for tag in course_tags:
        course_url = tag['href'] #getting the link by adding the base and remaing url which is in URF
        course_urls.append(course_url)
        #Print check to see if the url is correct.
        #print(course_url)

    '''Course_info: URL, Title, Topic, SkillLevel, CourseType, MinimumAge, MaximumAge, Description, Provider, Location'''
    csv = []

    for url in course_urls:
        course_info = {}
        #url = course_urls[0]
        print(url)
        if 'itconnect.uw.edu/learn/workshops/online-tutorials/' in url:
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html5lib')

            #1) url 
            course_info['URL'] = url

            #2) Title
            main_body = soup.find('div', attrs={'class':'uw-body-copy'})
            title = main_body.find('h1').getText()
            course_info['Title'] = title
            #print(title)

            #3) Topics
            description = main_body.find('p').getText()
            topic = getCourseTopics(title)
            course_info['Topic'] = topic
            #print(topic)

            #4) Skill Level
            course_info['SkillLevel'] = 'Beginner-Advanced'

            #5)course type
            course_info['CourseType'] = 'Online Workshop'

            #6) Age
            course_info['MaximumAge'] = -1
            course_info['MinimumAge'] = -1

            #7) Description
            course_info['Description'] = description

            #8) Provider
            course_info['Provider'] = 'University of Washington IT Connect'

            #9) Location 
            course_info['Location'] = []
            
            csv.append(course_info)

    #--------------------------------------------------#
    #Converting list of dictionary into CSV
    import pandas as pd

    df = pd.DataFrame(csv)
    df.to_csv('course_UWOnlineWorkshops.csv', index=False, encoding='utf-8')

    print('Complete!')
