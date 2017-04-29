from bs4 import BeautifulSoup
import json

file = 'mock_webpage.html'
line_end_character = '|'
remove_characters = '\n\xa0'
file_contents = open(file).read()

soup = BeautifulSoup(file_contents, 'html.parser')

# print( soup.find_all('span') )

dates = [el.get_text().split(line_end_character)[0] for el in soup.find_all('span', class_='date')]
locations = [el.get_text().split(line_end_character)[1] for el in soup.find_all('span', class_='date')]
titles = [el.get_text() for el in soup.find_all('span', class_='event-title')]

for i, el in enumerate( locations ):
    locations[i] = el.translate({ord(c): None for c in remove_characters})
for i, el in enumerate( titles ):
    titles[i] = el.translate({ord(c): None for c in remove_characters})


print(locations)
print(titles)
print(dates)

from dev_phase_first_hackathon import xml_parser
for i in range(len(dates)):
    R = xml_parser.RawData(titles[i], dates[i], locations[i])
    R.dump('test')
