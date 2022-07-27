import requests
from bs4 import BeautifulSoup


A03_core ='https://www.jumia.com.ng/samsung-galaxy-a03-core-2gb32gb-memory-onyx-136322463.html'
A13='https://www.jumia.com.ng/samsung-galaxy-a13-4gb64gb-memory-5000-mah-battery-black-126589247.html'
A22='https://www.jumia.com.ng/samsung-galaxy-a22-6.4-inch-4gb-ram-64gb-android-11-48mp-8mp-2mp-2mp-13mp-dual-sim-mint-81157923.html'
A23='https://www.jumia.com.ng/samsung-galaxy-a23-6.6-tft-screen-4gb128gb-memory-50mp-quad-camera-5000-mah-battery-android-12-blue-106401391.html'
A53='https://www.jumia.com.ng/samsung-galaxy-a53-5g-6gb128gb-memory-android-12-black-125642178.html'
S9_plus='https://www.jumia.com.ng/samsung-galaxy-s9-plus-6gb-ram64gb-rom8.0-oreo.-black-111935879.html'
S10_plus='https://www.jumia.com.ng/samsung-galaxy-s10-plus-s10-6.4-inch-amoled-8gb128gb-rom-4g-smartphone-back-case-screen-guide-100783895.html'
S20_ultra='https://www.jumia.com.ng/samsung-galaxy-s20-5g-12128gb-single-sim-android-10-octa-core-6.2-inch-quad-hd-121264mp-tri-lens-gray-134489070.html'
S21_ultra='https://www.jumia.com.ng/samsung-galaxy-s21-ultra-5g-12256gb-g998u-android-11-single-sim-6.8-inch-quad-hd-108121010mp-four-camera-black-122317208.html'
S22_ultra='https://www.jumia.com.ng/samsung-galaxy-s22-ultra-dual-sim-12gb-ram-256gb-5g-phantom-black-107448815.html'


#Just add the product link here and fetch the price

def samsung_jumia(product_link):
    samsung_url = product_link
    page = requests.get(url=samsung_url)
    soup=BeautifulSoup(page.content,'lxml')
    price =soup.find('span', class_='-b -ltr -tal -fs24').text
    phone={
        'price':price
    }
    return phone['price']


print(samsung_jumia(A03_core))
print(samsung_jumia(A13))
print(samsung_jumia(A22))
print(samsung_jumia(A23))
print(samsung_jumia(A53))
print(samsung_jumia(S9_plus))
print(samsung_jumia(S10_plus))
print(samsung_jumia(S20_ultra))
print(samsung_jumia(S21_ultra))
print(samsung_jumia(S22_ultra))
