import requests

from bs4 import BeautifulSoup

index = int(input())
url = str(input())

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
h2 = soup.find_all('h2')
answer = str(h2[index])
print(answer[4:-5])
