import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_1272637.xml'
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
tree = ET.fromstring(data)

results = list()
counts = tree.findall('.//count')
for count in counts :
    numbers = count.text
    inum = int(numbers)
    results.append(inum)

print(sum(results))
