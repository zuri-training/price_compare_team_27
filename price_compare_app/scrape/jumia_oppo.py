import requests
from bs4 import BeautifulSoup

a54='https://www.jumia.com.ng/oppo-a54-6.51-inch-4gb-ram128gb-rom-andriod-10-13mp-2mp-2mp-16mp-dual-sim-crystal-black-77285533.html'
reno3_pro='https://www.jumia.com.ng/oppo-reno-3-pro-6.5-12gb-ram-256gb-rom-android-10-641382mp-442mp-selfie-4g-dual-4025mah-moonlight-black-133981491.html'
a76='https://www.jumia.com.ng/oppo-a76-6.56-6gb-128gb-rom-android-11-132mp-8mp-selfie-dual-sim-snapdragon-4g-5000mah-glowing-blue-136177075.html'
a96='https://www.jumia.com.ng/oppo-a96-6.59-8256gb-50mp2mp-rear-16mp-selfie-blue-126530872.html'
a16k='https://www.jumia.com.ng/oppo-a16k-blue-6.52-64gb-4gb-ram-4230mah-98658988.html'
a57='https://www.jumia.com.ng/oppo-a57-6.56-4gb-ram-64gb-rom-android-12-132mp-8mp-selfie-4g-lte-5000mah-side-fingerprint-glowing-black-142731454.html'
a83='https://www.jumia.com.ng/oppo-a83-blue-5.7-64gb-4gb-ram-3180mah-141561907.html'
a3s='https://www.jumia.com.ng/oppo-a3s-blue-6.2-64gb-4gb-ram-4230mah-141561905.html'
reno7='https://www.jumia.com.ng/oppo-reno-7-6.438gb-ram256gb-rom-6422mp32mp4g-4500mah-132805617.html'
a55='https://www.jumia.com.ng/oppo-a55-6.51-64gb-4gb-ram-50mp2mp2mp-rear-camera-16mp-front-camera-android-11-dual-sim-5000mah-starry-black-106094705.html'



#Just add the product link here and fetch the price

def jumia_oppo(product_link):
    jumia_url= product_link
    page = requests.get(url=jumia_url)
    soup=BeautifulSoup(page.content,'lxml')
    price =soup.find('span', class_='-b -ltr -tal -fs24').text
    phone={
        'price':price
    }
    return phone["price"]
    

print(jumia_oppo(a54))
print(jumia_oppo(reno3_pro))
print(jumia_oppo(a76))
print(jumia_oppo(a96))
print(jumia_oppo(a16k))
print(jumia_oppo(a57))
print(jumia_oppo(a83))
print(jumia_oppo(a3s))
print(jumia_oppo(reno7))
print(jumia_oppo(a55))
