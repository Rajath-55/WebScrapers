import requests
import csv
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as bs
url = "https://www.worldometers.info/coronavirus/"
data = requests.get(url).text
# print(data)
soup = bs(data, 'html.parser')
table = soup.find('table', {'id': 'main_table_countries_today'})
# print(type(table))
# print(table)
headers = [th.text.encode("utf-8") for th in table.select("tr th")]
with open("COVID.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(headers)
    wr.writerows([[td.text.encode("utf-8").strip() for td in row.find_all("td")] for row in table.select("tr + tr")])
