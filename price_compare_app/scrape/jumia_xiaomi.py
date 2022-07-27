import requests
from bs4 import BeautifulSoup

redmi_note10='https://www.jumia.com.ng/xiaomi-redmi-10-6.5-inch-6gb-ram-128gb-rom-android-11-50mp-8mp-2mp-2mp-8mp-dual-sim-carbon-gray-104725632.html'
redmi_note10s='https://www.jumia.com.ng/xiaomi-redmi-note-10s-8gb128gb-blue-129757859.html'
redmi_note11='https://www.jumia.com.ng/xiaomi-redmi-note-11-6.5-4gb-ram-64gb-rom-50mp-dual-sim-4g-lte-5000mah-fingerprint-gray-98898983.html'
redmi_note11pro='https://www.jumia.com.ng/redmi-note-11-pro-5g-6.67-inch-8gb-ram-256gb-rom-android-11-108mp-8mp-2mp-16mp-dual-sim-graphite-gray-xiaomi-mpg1662881.html'
redmi_10c='https://www.jumia.com.ng/xiaomi-redmi-10c-6.53-inch-4gb-ram-128gb-rom-5000mah-gray-132645099.html'
redmi_10a='https://www.jumia.com.ng/xiaomi-redmi-10a-6.53-inches-4gb-ram-128gb-rom-5000mah-grey-134168483.html'
redmi_11t='https://www.jumia.com.ng/xiaomi-11t-pro-6.67-inch-5g-12gb-ram-256gb-rom-android-11-108mp-8mp-5mp-16mp-dual-sim-moonlight-white-111184692.html'
redmi_9a='https://www.jumia.com.ng/xiaomi-redmi-9a-2gb32gb-granite-grey-132924162.html'
m11_lite='https://www.jumia.com.ng/xiaomi-mi-11-lite-ne-5g-6.55-8gb128gb-6485mp4k20mp-4250mah-141736736.html'
redmi_11s='https://www.jumia.com.ng/redmi-note-11s-6gb128gb-graphite-gray-xiaomi-mpg1662461.html'


#Just add the product link here and fetch the price

def jumia_xiaomi(product_link):
    jumia_url= product_link
    page = requests.get(url=jumia_url)
    soup=BeautifulSoup(page.content,'lxml')
    price =soup.find('span', class_='-b -ltr -tal -fs24').text
    phone={
        'price':price
    }
    return phone["price"]

print(jumia_xiaomi(redmi_note10))
print(jumia_xiaomi(redmi_note10s))
print(jumia_xiaomi(redmi_note11))
print(jumia_xiaomi(redmi_note11pro))
print(jumia_xiaomi(redmi_10c))
print(jumia_xiaomi(redmi_10a))
print(jumia_xiaomi(redmi_11t))
print(jumia_xiaomi(redmi_9a))
print(jumia_xiaomi(m11_lite))
print(jumia_xiaomi(redmi_11s))

