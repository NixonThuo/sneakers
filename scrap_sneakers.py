import urllib2
from bs4 import BeautifulSoup
import re
import json


def lowest():
    TAG_RE = re.compile(r'<[^>]+>')
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    sneakers_url = 'http://stockx.com/sneakers/recent_asks'
    # sneakers_request = urllib2.Request(sneakers_url)
    sneakers_response = opener.open(sneakers_url)
    sneakers_html = sneakers_response.read()
    # print(type(sneakers_html))
    soup = BeautifulSoup(sneakers_html, 'html.parser')
    sneakers_div = soup.findAll("div", class_="clickZone")
    count = 0
    items = {}
    min_item = {}
    for sneaker in sneakers_div:
        sneaker_price_div = sneakers_div[count]
        # print(sneaker_price_div.findAll("div")[1].text)
        sneaker_name = sneaker_price_div.findAll("div")[1].text
        position = str(sneaker_price_div).find("$")
        price_raw = (str(sneaker_price_div)[position + 1:])
        price_raw = TAG_RE.sub('', price_raw)
        price = price_raw.replace(',', '')
        # print(price)
        items[sneaker_name] = int(price)
        count += 1

    key_min = min(items.keys(), key=(lambda k: items[k]))
    min_item[key_min] = items[key_min]
    # print(min_item)
    json_string = json.dumps(min_item)

    # soup_two = BeautifulSoup(str(sneaker_price_div), 'html.parser')
    # real_price_div = soup_two.findAll("div", {"class": "price-line"})
    # print(real_price_div[0])
    return json_string


print(lowest())
