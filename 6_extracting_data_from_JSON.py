import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_1272638.json'
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()

results = list()
info = json.loads(data)
comments = info['comments']
for item in comments :
    num = (item.get('count'))
    inum = int(num)
    results.append(inum)

print(sum(results))
