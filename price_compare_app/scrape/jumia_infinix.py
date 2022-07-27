import requests
from bs4 import BeautifulSoup

hot_11='https://www.jumia.com.ng/infinix-hot-11-6.82-hd-4gb-ram-128gb-rom-android-11-polar-black-139128307.html'
hot_11play='https://www.jumia.com.ng/infinix-hot-11-play-x688b-6000-mah-64-gb-storage-4-gb-ram-black-94735893.html'
hot_12i='https://www.jumia.com.ng/infinix-hot-12i-4gb64gb-memory-racing-black-129805008.html'
hot_12play='https://www.jumia.com.ng/infinix-hot-12-play-x6816-6.82-1284gb-ram-13mp8mp-4g-lte-6000mah-blue-130414749.html'
zeroX='https://www.jumia.com.ng/infinix-zero-x-8gb128gb-memory-android-11-starry-silver-129757280.html'
smart6='https://www.jumia.com.ng/infinix-smart-6-6.6-2gb32gb-5000mah-android-11-midnight-black-127629700.html'
note_10='https://www.jumia.com.ng/infinix-note-10-x693-6.95-fhd-128gb4gb-memory-16mp-selfie-camera48mp-ultra-night-camera-android-11-106836009.html'
note_11pro='https://www.jumia.com.ng/infinix-note-11-pro-8gb128gb-memory-android-11-mist-blue-129754367.html'
note_12i='https://www.jumia.com.ng/infinix-note-12i-4gb128gb-memory-snowfall-129859134.html'
note12='https://www.jumia.com.ng/infinix-note-12-6.7-fhd-128gb-rom-4gb-ram-50-mp-wide-2-mp-depth-qvga-16mpselfie-4g-lte-5000mah-gold-122494504.html'


#Just add the product link here and fetch the price

def jumia_infinix(product_link):
    jumia_url= product_link
    page = requests.get(url=jumia_url)
    soup=BeautifulSoup(page.content,'lxml')
    price =soup.find('span', class_='-b -ltr -tal -fs24').text
    phone={
        'price':price
    }
    return phone["price"]
    
print(jumia_infinix(hot_11))
print(jumia_infinix(hot_11play))
print(jumia_infinix(hot_12i))
print(jumia_infinix(hot_12play))
print(jumia_infinix(zeroX))
print(jumia_infinix(smart6))
print(jumia_infinix(note_10))
print(jumia_infinix(note_11pro))
print(jumia_infinix(note_12i))
print(jumia_infinix(note12))


