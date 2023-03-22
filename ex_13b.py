# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def retrieve_content(url):
    print("Retrieving:", url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    pos = int(position)
    if len(tags) >= pos:
        return tags[pos-1].get('href', None), tags[pos-1].contents[0]

url = input('Enter URL:')
count = input('Enter count:')
position = input('Enter position:')
sequence_name = list()
for i in range(int(count)):
    url, name = retrieve_content(url)
    sequence_name.append(name)
print(sequence_name)


