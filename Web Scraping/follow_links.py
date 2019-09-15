## Grant Gasser
## Following Links
## Dr Chuck

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# input
url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

i = 0
while i < count:
    # Retrieve all of the anchor tags
    tags = soup('a')
    j = 1
    for tag in tags:
        #print(tag.get('href', None))

        if j == 3:
            new_link = tag.get('href', None)
            print(new_link)
            break

        j += 1

    html = urllib.request.urlopen(new_link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    i += 1
