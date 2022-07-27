import requests
from bs4 import BeautifulSoup


A03_core ='https://www.konga.com/product/samsung-samsung-galaxy-a03-core-2gb-ram-32gb-rom-dual-sim-4g-lte-5000mah-5706106'
A13='https://www.konga.com/product/samsung-samsung-galaxy-a13-4gb-ram-64gb-rom-lte-5000mah-5706179'
A22='https://www.konga.com/product/samsung-galaxy-a22-5g-64gb-rom-4gb-ram-5000mah-android-11-6-6-white-5673453'
A23='https://www.konga.com/product/samsung-samsung-galaxy-a23-6-6-4gb-ram-128gb-rom-dual-sim-5000mah-peach-5674621'
A53='https://www.konga.com/product/samsung-samsung-galaxy-a53-6-5-6gb-ram-128gb-rom-dual-sim-5g-5000mah-white-5674576'
S9_plus='https://www.konga.com/product/samsung-galaxy-s9-plus-6-2-single-sim-6gb-ram-64gb-rom-3500mah-4g-blue-5180044'
S10_plus='https://www.konga.com/product/samsung-s10-plus-8gb-128gb-6-4-single-nano-sim-black-5374804'
S20_ultra='https://www.konga.com/product/samsung-galaxy-s20-ultra-5g-12-6-9-128gb-rom-12gb-ram-5g-single-sim-5000mah-black-5778075'
S21_ultra='https://www.konga.com/product/samsung-galaxy-s21-ultra-6-8-256gb-rom-12gb-ram-dual-sim-5g-5000mah-fingerprint-silver-5090504'
S22_ultra='https://www.konga.com/product/samsung-galaxy-s22-ultra-5g-6-8-256gb-rom-12gb-ram-5g-dual-sim-5000mah-black-5797496'


#Just add the product link here and fetch the price

def samsung_konga(product_link):
    samsung_url = product_link
    page = requests.get(url=samsung_url)
    soup=BeautifulSoup(page.content,'lxml')
    price =soup.find('div', class_='_678e4_e6nqh').text
    phone={
        'price':price
    }
    return phone['price']


print(samsung_konga(A03_core))
print(samsung_konga(A13))
print(samsung_konga(A22))
print(samsung_konga(A23))
print(samsung_konga(A53))
print(samsung_konga(S9_plus))
print(samsung_konga(S10_plus))
print(samsung_konga(S20_ultra))
print(samsung_konga(S21_ultra))
print(samsung_konga(S22_ultra))
