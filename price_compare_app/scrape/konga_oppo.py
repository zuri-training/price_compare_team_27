import requests
from bs4 import BeautifulSoup

a54='https://www.konga.com/product/oppo-oppo-a54-blue-4gb-128gb-5392698'
reno3_pro='https://www.konga.com/product/oppo-reno-3-pro-6-4-256gb-rom-12gb-ram-dual-sim-4g-lte-fingerprint-4025mah-black-5504072'
a76='https://www.konga.com/product/oppo-oppo-a76-6-56-6gb-ram-128gb-rom-5000mah-black-5685658'
a96='https://www.konga.com/product/oppo-a96-6-59-8gb-ram-256gb-rom-dual-sim-4g-lte-50mp-fingerprint-5000mah-blue-5682361'
a16k='https://www.konga.com/product/oppo-a16k-6-52-64gb-rom-4gb-ram-dual-sim-4g-lte-13mp-android-11-4230mah-blue-5620878'
a57='https://www.konga.com/product/oppo-a57-4g-6-56-64gb-rom-4gb-ram-dual-sim-fingerprint-5000mah-green-5793675'
a83='https://www.konga.com/product/oppo-a83-64gb-rom-4gb-ram-4g-lte-dual-sim-compact-5-7-display-face-unlock-blue-5792198'
a3s='https://www.konga.com/product/oppo-a3s-64gb-rom-4gb-ram-4g-lte-dual-sim-6-2-inch-display-blue-5789057'
reno7='https://www.konga.com/product/oppo-reno7-6-43amoled-256gb-rom-8gb-ram-dual-sim-4g-lte-4500mah-fingerprint-gold-5722454'
a55='https://www.konga.com/product/oppo-oppo-a55-6-51-64gb-4gb-ram-android-11-dual-sim-5000mah-black-5623397'

#Just add the product link here and fetch the price

def konga_oppo(product_link):
    konga_url = product_link
    page = requests.get(url=konga_url)
    soup=BeautifulSoup(page.content,'lxml')
    price =soup.find('div', class_='_678e4_e6nqh').text
    phone={
        'price':price
    }
    return phone['price']

print(konga_oppo(a54))
print(konga_oppo(reno3_pro))
print(konga_oppo(a76))
print(konga_oppo(a96))
print(konga_oppo(a16k))
print(konga_oppo(a57))
print(konga_oppo(a83))
print(konga_oppo(a3s))
print(konga_oppo(reno7))
print(konga_oppo(a55))

