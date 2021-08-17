import re
from bs4 import BeautifulSoup
import urllib3
import requests

u2 = requests.get('https://store.lindyssports.com/collections/ncaa/products/2021-pro-football?variant=37772907086007')
# u2 = requests.get('https://store.lindyssports.com/collections/special-editions/products/2020-national-champions')
# print(u2.text)
x = re.search(r'Buy\s*it\s*now', u2.text, re.I)

if x:
    print(x.group())
else:
    print("not for sale")

soup = BeautifulSoup(u2.text, 'html.parser')

s = soup.find("h1")
print(s.text)
