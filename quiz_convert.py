import requests
from bs4 import BeautifulSoup
import json
"""
Convert a quizlet stufy set to csv format using web crawling
"""
# read data from html file
with open('tst.html', 'r', encoding='utf-16') as f:
    html_content = f.read()

# Crawl html file to find the content rows
soup = BeautifulSoup(html_content)
container = soup.find('div', class_='TermRows')
container = container.div

rows = container.find_all('p')

# Create the array of cards
cards = []
row_dict = {'term': '', 'def': ''}

for i in range(len(rows)):
    text = rows[i].text    
    if i % 2 == 0:
        row_dict['term'] = text
    else:
        row_dict['def'] = text
        cards.append(row_dict.copy())



# Format the output
output = {
    'name': 'pytest',
    "description": "testing converting from python",
    'cards': cards
}
output = json.dumps(output, ensure_ascii=False)
# print('-------------------------output---------------------', output)


# Write the string to file
with open('tst.json', 'w', encoding='utf-16') as f:
    f.write(output)

