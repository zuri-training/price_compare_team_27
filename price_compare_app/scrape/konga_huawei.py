import requests
from bs4 import BeautifulSoup


nova9='https://www.konga.com/product/huawei-nova-9-6-57-oled-128gb-rom-8gb-ram-dual-sim-4g-lte-50mp-4300mah-fingerprint-black-5619078'
p40_pro='https://www.konga.com/product/huawei-p40-pro-dual-sim-8gb-ram-256gb-rom-4g-lte-6-58-4200mah-fingerprint-silver-5136141?gclid=Cj0KCQjwof6WBhD4ARIsAOi65ahiqEPtmj5AJoRnWQKtmORLzAmuP1D-O7kCsMqlu273JnqauGW_73caAiefEALw_wcB'
y6_prime='https://www.konga.com/product/huawei-y6-prime-2018-5-7-8gb-ram-128gb-rom-4g-lte-dual-sim-3000mah-black-5785260'
p50_pro='https://www.konga.com/product/huawei-p50-pro-6-6-8gb-ram-256gb-rom-harmony-os-dual-sim-golden-black-5774129'
p10_lite='https://www.konga.com/product/huawei-p10-lite-64gb-rom-4gb-ram-dual-sim-white-5577702?gclid=Cj0KCQjwof6WBhD4ARIsAOi65ajVyR6vIC3MoCQJoSL00mDVyZiNRixBLDzEw9RnT-4e-2lOn6HqZMcaApVXEALw_wcB'
nova_8i='https://www.konga.com/product/huawei-nova-8i-6gb-ram-128gb-rom-6-67-dual-sim-moonlight-silver-5792557'
p30_pro='https://www.konga.com/product/huawei-p30-pro-6-47-8gb-ram-256gb-rom-android-9-0-dual-sim-breathing-crystal-4392902?gclid=Cj0KCQjwof6WBhD4ARIsAOi65ajOck0wjnDKqQY6x2l2K5JgmtlBTbYYm9K7GSiUtwBXn792syPjPCwaAnM8EALw_wcB'
y9='https://www.konga.com/product/huawei-y9-2019-128gb-rom-6gb-am-dual-sim-gold-5577684'
p30_lite='https://www.konga.com/product/huawei-p30-lite-6-15-6gb-ram-256gb-rom-48-8-2-mp-32mp-selfie-hybrid-dual-blue-5716380'
y9a='https://www.konga.com/product/huawei-y9a-dual-sim-8gb-ram-128gb-rom-4g-lte-6-63-4300mah-fingerprint-black-5612167'

#Just add the product link here and fetch the price

def konga_huawei(product_link):
    konga_url = product_link
    page = requests.get(url=konga_url)
    soup=BeautifulSoup(page.content,'lxml')
    price =soup.find('div', class_='_678e4_e6nqh').text
    phone={
        'price':price
    }
    return phone['price']


print(konga_huawei(nova9))
print(konga_huawei(p40_pro))
print(konga_huawei(y6_prime))
print(konga_huawei(p50_pro))
print(konga_huawei(p10_lite))
print(konga_huawei(nova_8i))
print(konga_huawei(p30_pro))
print(konga_huawei(y9))
print(konga_huawei(p30_lite))
print(konga_huawei(y9a))
