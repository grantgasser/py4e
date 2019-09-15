## Grant Gasser
## XML Parsing
## Dr Chuck

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# TEST LINKS:
# http://py4e-data.dr-chuck.net/comments_42.xml
# http://py4e-data.dr-chuck.net/comments_242504.xml


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

results = tree.findall('.//count')

sum = 0
for res in results:
    sum += int(res.text)

print(sum)
