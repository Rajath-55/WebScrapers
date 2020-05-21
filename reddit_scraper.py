from bs4 import BeautifulSoup
from requests import get
from fake_useragent import UserAgent
import pandas as pd

ua = UserAgent()


def lovely_soup(u):
    r = get(u, headers={'User-Agent': ua.chrome})
    return BeautifulSoup(r.text, 'lxml')


url = 'https://old.reddit.com/r/Showerthoughts?sort=top&t=week'
soup = lovely_soup(url)

titles = soup.findAll('p', {'class': 'title'})
data = []
for title in titles:
    data.append(title) 
df = pd.DataFrame(data)
print(df) 
with open('new.csv', 'w+') as file:
    df.to_csv('new.csv')  

file.close()