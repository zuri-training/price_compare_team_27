import requests
from bs4 import BeautifulSoup




iphone6_refurbished='https://www.jumia.com.ng/apple-refurbished-apple-iphone-6-16gb-grey-89901727.html'
iphone7_plus='https://www.jumia.com.ng/apple-renewed-iphone-7-plus-32gbram3gb-black-iphone7p-118774089.html'
iphone8_plus='https://www.jumia.com.ng/apple-iphone-8-3gb64gb-space-gray-5.5-inch-refurbished-99-new-3d-touch-fingerprint-ios-smartphone-73398517.html'
iphoneX='https://www.jumia.com.ng/apple-iphone-x-256gb-5.8-inch-3gb-ram-space-grey-92801020.html'
iphoneXS_Max='https://www.jumia.com.ng/apple-iphone-xs-max-256gb-4gb-6.5-gold.-free-case-screen-guide-134599590.html'
iphone11='https://www.jumia.com.ng/apple-iphone-11-128gb-black-authorized-reseller-store-44865293.html'
iphone11_ProMax= 'https://www.jumia.com.ng/iphone-11-pro-max-6.5-inch-4gb-ram-256gb-romios-13-12mp12mp12mp12mp-4g-lte-smartphone-midnight-green-apple-mpg1598798.html'
iphone12='https://www.jumia.com.ng/apple-iphone-12-128gb-purple-78398928.html'
iphone12_ProMax='https://www.jumia.com.ng/iphone-12-pro-max-256gb-6gb-ram-6.7-inch12mp12mp12mp-pacific-blue-apple-mpg1595399.html'
iphone13_ProMax='https://www.jumia.com.ng/apple-iphone-13-pro-max-6.7-xdr-display-6gb-ram-128gb-rom-ios-15-sierra-blue-93389767.html'


#Just add the product link here and fetch the price

def jumia_iphone(product_link):
    jumia_url= product_link
    page = requests.get(url=jumia_url)
    soup=BeautifulSoup(page.content,'lxml')
    price =soup.find('span', class_='-b -ltr -tal -fs24').text
    phone={
        'price':price
    }
    return phone["price"]
    


print(jumia_iphone(iphone6_refurbished))
print(jumia_iphone(iphone7_plus))
print(jumia_iphone(iphone8_plus))
print(jumia_iphone(iphoneX))
print(jumia_iphone(iphoneXS_Max))
print(jumia_iphone(iphone11))
print(jumia_iphone(iphone11_ProMax))
print(jumia_iphone(iphone12))
print(jumia_iphone(iphone12_ProMax))
print(jumia_iphone(iphone12))

