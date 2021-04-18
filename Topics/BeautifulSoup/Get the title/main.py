import requests

from bs4 import BeautifulSoup

url = str(input())

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
h1 = soup.find('h1')
answer = str(h1)
# print(answer[4:-5])
print(soup.h1.string)
