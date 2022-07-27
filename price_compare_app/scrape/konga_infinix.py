import requests
from bs4 import BeautifulSoup

hot_11='https://www.konga.com/product/infinix-hot-11-4gb-ram-128gb-rom-6-82-6000mah-4g-lte-fingerprint-purple-5782514'
hot_11play='https://www.konga.com/product/infinix-hot-11-play-x688b-6-82-hd-64gb-rom-4gb-ram-13mp-8mp-6000mah-4g-lte-helio-g35-blue-5596949'
hot_12i='https://www.konga.com/product/infinix-hot-12i-6-6hd-64gb-rom-4gb-4g-lte-5000mah-fingerprint-gold-5760934'
hot_12play='https://www.konga.com/product/infinix-hot-12-play-6-82-128gb-rom-4gb-ram-dual-sim-4g-lte-fingerprint-6000mah-green-5724735'
zeroX='https://www.konga.com/product/infinix-infinix-zero-x-6-67-128gb-rom-8gb-ram-4500-mah-dual-sim-silver-5504785'
smart6='https://www.konga.com/product/infinix-smart-6x657-6-6-hd-32gb-rom-2gb-ram-8mp-8mp-5000mah-3g-ocean-blue-5684008'
note_10='https://www.konga.com/product/infinix-note-10-6-95-4gb-ram-128gb-rom-48mp-dual-sim-4g-lte-5000mah-fingerprint-green-5782700'
note_11pro='https://www.konga.com/product/infinix-note-11-pro-6-95-8gb-ram-128gb-rom-dual-sim-4g-lte-64mp-fingerprint-5000mah-blue-5760920'
note_12i='https://www.konga.com/product/infinix-note-12i-x6819-128gb-4gb-50mp-8mp-dual-sim-5000mah-snowfall-5748844'
note12='https://www.konga.com/product/infinix-note-12-6-7-4gb-ram-128gb-rom-android-11-dual-sim-4g-lte-5000mah-gold-5741889'


#Just add the product link here and fetch the price

def konga_infinix(product_link):
    jumia_url= product_link
    page = requests.get(url=jumia_url)
    soup=BeautifulSoup(page.content,'lxml')
    price =soup.find('div', class_='_678e4_e6nqh').text
    phone={
        'price':price
    }
    return phone["price"]
    
print(konga_infinix(hot_11))
print(konga_infinix(hot_11play))
print(konga_infinix(hot_12i))
print(konga_infinix(hot_12play))
print(konga_infinix(zeroX))
print(konga_infinix(smart6))
print(konga_infinix(note_10))
print(konga_infinix(note_11pro))
print(konga_infinix(note_12i))
print(konga_infinix(note12))


