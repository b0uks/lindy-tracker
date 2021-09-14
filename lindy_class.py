import re
from bs4 import BeautifulSoup
import requests
from datetime import datetime


def get_url_text(url):
    return requests.get(url).text


def get_name(text):
    soup = BeautifulSoup(text, 'html.parser')
    s = soup.find("h1")
    return s.text


def get_order_fulfillment(text):
    x = re.search(r'Order\sfulfillment\sbegins: ([a-zA-Z]*\s\d{1,2},\s*\d{4})', text, re.I)
    if x:
        # print(x.group(1))
        return x.group(1)


class LindyListing:

    id = -1
    name = 'none'
    url = 'none'
    status = 'none'
    last_update = 'never'
    key = None
    text = ''

    def __init__(self, url):
        self.url = url
        self.text = get_url_text(url)
        self.status = self.get_status(self.text)
        self.name = get_name(self.text)
        self.fulfill = get_order_fulfillment(self.text)
        self.last_update = str(datetime.now())

    def get_status(self, u2):
        x = re.search(r'(Buy\s*it\s*now)|(Buy\s*your\s*copy\s*today)', u2, re.I)
        self.last_update = str(datetime.now())
        if x:
            return 'ACTIVE'
        else:
            return 'OUT'

    def print_stuff(self):
        # print(self.text)
        print(f'Listing name: {self.name}')
        print(self.url)
        print(f'Status: {self.status}')
        print(f'last update: {self.last_update}')
        print(f'order fulfillment: {get_order_fulfillment(self.text)}')
        print(f'key: {self.key}')
        print('')

    def update(self):
        self.text = get_url_text(self.url)
        old = self.status
        self.status = self.get_status(self.text)
        self.name = get_name(self.text)
        if old != self.status:
            print('!!!LISTING AVAIL HAS CHANGED!!!')
            print(f'{self.name} has changed from {old} to {self.status}')

    def to_list(self):
        return (self.name, self.status, self.fulfill, self.url)