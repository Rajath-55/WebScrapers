import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://finance.yahoo.com/cryptocurrencies"
re = requests.get(url)
soup = BeautifulSoup(re.text, 'html.parser')
# print(soup)
table = soup.find('table', {'class': 'W(100%)'})
# print(table)
head = []
headers = table.find('thead')
for header in headers:
    head.append(header.text)
print(head)   

df = pd.read_html(str(table))[0]
print(df)

df.to_csv('Crypto.csv', index=False)