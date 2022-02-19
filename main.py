# Required module- pip install requests

import requests

# pip install Bs4

from bs4 import BeautifulSoup

# Passing Request

page = requests.get(

    "https://www.goodreturns.in/gold-rates/#Today+24+Carat+Gold+Rate+Per+Gram+in+India+%28INR%29")


# Getting Content of Page

Soup = BeautifulSoup(page.content, 'html.parser')

# Getting info specific Class

info = Soup.find_all(class_='odd_row')


count = 0

# Getting Date Which we Required...

for items in info:

    count += 1

    if count == 2:


        print(items.get_text())

        break