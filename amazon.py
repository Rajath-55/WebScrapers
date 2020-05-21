import requests
from bs4 import BeautifulSoup
 
urls = ["https://www.amazon.in/Apple-MWP22HN-A-AirPods-Pro/dp/B07ZRXF7M8/ref=sr_1_1_sspa?dchild=1&keywords=airpods&qid=1589288928&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzSTROMFk0R1FRSVgxJmVuY3J5cHRlZElkPUEwNTIyOTY4UzdOSlRET0pNNDJMJmVuY3J5cHRlZEFkSWQ9QTAwMzkzMjAzSU1HSFZJOUFYSzVHJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==", "https://www.amazon.in/Apple-iPhone-XR-128GB-Black/dp/B07JG7DS1T/ref=sr_1_1?dchild=1&keywords=iphone&qid=1589289563&sr=8-1", "https://www.amazon.in/JBL-C100SI-Ear-Headphones-Black/dp/B01DEWVZ2C/ref=sr_1_1?dchild=1&keywords=jbl&qid=1589289639&sr=8-1"]
headers = { 
    "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
products = dict()
for url in urls:
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify)
    title = soup.find(id="productTitle").text
    print(title.strip())

    price = soup.find(id="priceblock_ourprice").text
    converted_price = price[:12]
    print(converted_price)
    products[title.strip()]=converted_price.strip()

print(products)
with open('costs.csv', 'w') as file:
    for item,value in products.items():
        file.write(item)
        file.write(value)
        file.write("\n")
file.close()