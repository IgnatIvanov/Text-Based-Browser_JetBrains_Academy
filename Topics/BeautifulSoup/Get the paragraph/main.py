import requests

from bs4 import BeautifulSoup

certain_word = str(input())
url = str(input())

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
p = soup.find_all('p')

for paragraph in p:
    if str(paragraph).find(certain_word) != -1:
        print(str(paragraph)[3:-4])
        break
