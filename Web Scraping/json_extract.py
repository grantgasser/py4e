## Grant Gasser
## JSON
## Dr Chuck

import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# get data
url = input('Enter location: ')

uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode()

data = json.loads(data)

sum = 0
for comment in data['comments']:
    sum += int(comment['count'])

print(sum)
