import requests
from bs4 import BeautifulSoup


iphone6='https://www.konga.com/product/apple-iphone-6-4-7-16gb-grey-4623548'
iphone7_plus='https://www.konga.com/product/iphone-7-plus-5-5-32gb-rom-3gb-ram-nano-sim-black-5226700'
iphone8_plus='https://www.konga.com/product/apple-iphone-8-plus-5-5-64gb-rom-3gb-ram-ios-11-12mp-5630055'
iphoneX='https://www.konga.com/product/apple-iphone-x-256gb-pouch-screen-guide-selfie-stick-grey-4678237'
iphoneXS_Max='https://www.konga.com/product/apple-iphone-xs-max-256gb-rom-4gb-ram-12mp-6-5-space-grey-free-case-and-screen-guide-5763466'
iphone11='https://www.konga.com/product/apple-iphone-11-128gb-rom-4gb-ram-red-4719450'
iphone11_ProMax= 'https://www.konga.com/product/apple-iphone-11-pro-max-6-5-256gb-rom-4gb-ram-ios-13-3969mah-gold-5699852'
iphone12='https://www.konga.com/product/apple-iphone-12-6-1-display-128gb-rom-4gb-ram-single-sim-2815mah-power-bank-blue-5682008'
iphone12_ProMax='https://www.konga.com/product/apple-iphone-12-pro-max-256gb-6gb-ram-6-7-pacific-blue-5187171'
iphone13_ProMax='https://www.konga.com/product/apple-iphone-13-pro-128gb-5g-sierra-blue-5501066'


#Just add the product link here and fetch the price

def konga_iphone(product_link):
    konga_url = product_link
    page = requests.get(url=konga_url)
    soup=BeautifulSoup(page.content,'lxml')
    price =soup.find('div', class_='_678e4_e6nqh').text
    phone={
        'price':price
    }
    return phone['price']


print(konga_iphone(iphone6))
print(konga_iphone(iphone7_plus))
print(konga_iphone(iphone8_plus))
print(konga_iphone(iphoneX))
print(konga_iphone(iphoneXS_Max))
print(konga_iphone(iphone11))
print(konga_iphone(iphone11_ProMax))
print(konga_iphone(iphone12))
print(konga_iphone(iphone12_ProMax))
print(konga_iphone(iphone13_ProMax))
