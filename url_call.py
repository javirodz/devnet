from urllib.request import urlopen
from xml.etree.ElementTree import parse

myURL = urlopen("https://vwannabe.com/feed/")
myXML=parse(myURL)

for item in myXML.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')

    print(title)
    print(date)
    print(link)
    print()