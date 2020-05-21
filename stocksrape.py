import requests
from bs4 import BeautifulSoup
import time
def getprice():
    r = requests.get('https://finance.yahoo.com/quote/FB?p=FB')
    soup =BeautifulSoup(r.text, 'html.parser')
    # print(soup)
    get_price = soup.findAll('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text

    return get_price
count=0
while True:
    print('The Price is ' + str(getprice()))
    time.sleep(30)
    count +=1
    if count==1000:
        break