import requests
from bs4 import BeautifulSoup
import soup_extra_methods as methods

# ONLY locations are scraped - the 3 courses are all manually inputted
base_url = "https://www.seattleymca.org/locations?type=ymca,camps"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html5lib')

print('Loaded data from ' + base_url)

locations = []

# finds list of rows within the first 'section' of locations (first section is YMCAs, second is camps, etc.)
location_divs = methods.find_all('article', soup, attrs={'data-locations':'{"tags":["YMCA"]}'})

for location_div in location_divs:
    location = methods.find('p', location_div, attrs={'class':'address'}) # paragraph tagged with 'address'
    for br in methods.find_all('br', location): # remove all 'br'
        br.replace_with("\n")


    location = location.getText().strip().replace('  ', '').replace(' \n\n ',' ') # formatting
    locations.append(location)

print('Locations found')

csv = []

dictionary = {}
dictionary['URL'] = 'https://www.seattleymca.org/accelerator/ytech'
dictionary['Title'] = 'YTech Digital Lifehacks'
dictionary['Topic'] = 'Digital Literacy'
dictionary['SkillLevel'] = 'Beginner'
dictionary['CourseType'] = 'Workshop'
dictionary['MinimumAge'] = 18
dictionary['MaximumAge'] = -1
dictionary['Description'] = "A series of 6 workshops targeted at young adults experiencing or at risk of homelessness, focusing on real-world digital skills that will increase participant access to employment, education and other important resources, including housing, and healthcare. Participants will have the opportunity to earn laptops, tablets, and internet connection through hotspots."
dictionary['Provider'] = 'YMCA'
dictionary['Locations'] = locations
csv.append(dictionary)

dictionary = {}
dictionary['URL'] = 'https://www.seattleymca.org/accelerator/ytech'
dictionary['Title'] = 'YTech Tuesdays'
dictionary['Topic'] = 'Digital Literacy'
dictionary['SkillLevel'] = 'Beginner/Intermediate'
dictionary['CourseType'] = 'Afterschool Program'
dictionary['MinimumAge'] = 11
dictionary['MaximumAge'] = 18
dictionary['Description'] = "A weekly after-school program for middle and high school students, intended to help build a bridge between low income youth, youth of color, immigrant and refugee youth, and Seattle’s tech economy. Participants will participate in skill-building workshops, field trips, and job shadowing. This program will include building partnerships with various tech professionals within the industry. Participants will have the opportunity to earn laptops, tablets, cameras, and internet connection through hotspots."
dictionary['Provider'] = 'YMCA'
dictionary['Locations'] = locations
csv.append(dictionary)

dictionary = {}
dictionary['URL'] = 'https://www.seattleymca.org/accelerator/ytech'
dictionary['Title'] = 'Job Readiness Training'
dictionary['Topic'] = 'Job search / digital literacy'
dictionary['SkillLevel'] = 'Beginner'
dictionary['CourseType'] = 'Course'
dictionary['MinimumAge'] = -1
dictionary['MaximumAge'] = 18
dictionary['Description'] = "In junction other organizations, YTech programming aims to have youth be aware of the importance of both soft and hard skills. In partnership with the Horn of Africa Services organization, youth are taught interview techniques, how to job search, and more. In addition, they are given projects that allow them to allow use and learn devices such as cameras, camcorders, and laptops for presentations.\nFurthermore, youth attending the YTech program will have the opportunity to ask for tips from various professionals in how to get themselves started and what approaches are best taken; the program has a slight integration of leadership skill building through moments of mentorship from professionals and volunteers."
dictionary['Provider'] = 'YMCA'
dictionary['Locations'] = locations
csv.append(dictionary)

import pandas as pd

df = pd.DataFrame(csv)
df.to_csv('csv\\course_ymca.csv', index=False,encoding='utf-8')

print('Complete')