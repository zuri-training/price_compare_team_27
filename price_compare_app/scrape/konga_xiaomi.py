import requests
from bs4 import BeautifulSoup


redmi_note10='https://www.konga.com/product/xiaomi-redmi-10-6-5-6gb-ram-128gb-rom-50mp-dual-sim-4g-lte-5000mah-fingerprint-grey-5440619'
redmi_note10s='https://www.konga.com/product/xiaomi-redmi-note-10s-8gb-128gb-white-smartphone-5487470'
redmi_note11='https://www.konga.com/product/xiaomi-redmi-note-11-6-43-fhd-64gb-rom-4gb-ram-4g-lte-50mp-13mp-5000mah-gray-5651531?seller_id=67157&sku_id=5651531&sclid=uaQM0R1e8gY8cRbl5CbXHlD0i8HHdw6B'
redmi_note11pro='https://www.konga.com/product/xiaomi-redmi-note-11-pro-5g-6-67amoled-256gb-rom-8gb-ram-dual-sim-4500mah-fingerprint-gray-5690025'
redmi_10c='https://www.konga.com/product/xiaomi-redmi-10c-6-71-128gb-rom-4gb-ram-dual-sim-4g-lte-5000mah-fingerprint-gray-5670908'
redmi_10a='https://www.konga.com/product/xiaomi-redmi-10a-6-53-128gb-rom-4gb-ram-dual-sim-4g-lte-fingerprint-5000mah-blue-5759542'
redmi_11t='https://www.konga.com/product/xiaomi-11t-pro-5g-6-67amoled-12gb-ram-256gb-rom-108mp-dual-sim-5000mah-fingerprint-blue-5705422'
redmi_9a='https://www.konga.com/product/xiaomi-redmi-9a-dual-android-10-32gb-rom-2gb-ram-4g-lte-6-53-13mp-5000mah-grey-5022134'
m11_lite='https://www.konga.com/product/xiaomi-mi-11-lite-6-55amoled-128gb-rom-8gb-ram-dual-sim-4g-lte-4250mah-fingerprint-peach-5716263'
redmi_11s='https://www.konga.com/product/xiaomi-redmi-note-11s-6-43-fhd-128gb-rom-6gb-ram-4g-lte-108mp-16mp-5000mah-blue-5639607?seller_id=67157&sku_id=5639607&sclid=lvWstlfGgtWMCO8bp37mNDTLMOPkyyeO'



#Just add the product link here and fetch the price

def konga_xiaomi(product_link):
    jumia_url= product_link
    page = requests.get(url=jumia_url)
    soup=BeautifulSoup(page.content,'lxml')
    price =soup.find('div', class_='_678e4_e6nqh').text
    phone={
        'price':price
    }
    return phone["price"]

print(konga_xiaomi(redmi_note10))
print(konga_xiaomi(redmi_note10s))
print(konga_xiaomi(redmi_note11))
print(konga_xiaomi(redmi_note11pro))
print(konga_xiaomi(redmi_10c))
print(konga_xiaomi(redmi_10a))
print(konga_xiaomi(redmi_11t))
print(konga_xiaomi(redmi_9a))
print(konga_xiaomi(m11_lite))
print(konga_xiaomi(redmi_11s))
    

