import requests
from bs4 import BeautifulSoup


nova9='https://www.jumia.com.ng/huawei-nova-9-se-6.78-8128gb-android-11-dual-midnight-black-137053499.html'
p40_pro='https://www.jumia.com.ng/huawei-p40-pro-6.58-inch-8gb-ram-256gb-rom-android-10-50mp-12mp-40mp-32mp-5g-dual-sim-silver-frost-106095064.html'
p50_pro='https://www.jumia.com.ng/huawei-p50-pro-6.6-256gb-rom8gb-ram-harmonyos-2.0-50401364mp-13mp-selfie-4g-hybrid-dual-4360mah-golden-black-123195151.html'
p10_lite='https://www.jumia.com.ng/huawei-p10-lite-5.2inch-4gbram64gbrom-dual-sim-card-97074590.html'
nova_8i='https://www.jumia.com.ng/huawei-nova-8i-6.67-6gb-ram-128gb-rom-android-10-dual-sim-moonlight-silver-139149481.html'
p30_pro='https://www.jumia.com.ng/huawei-p30-pro-6.47-inch-8gb-ram-256gb-rom-android-9.040mp-20mp-8mp-dual-sim-breathing-crystal-36665572.html'
y9='https://www.jumia.com.ng/huawei-y9-2019-smartphone-6.56gb128gb-ram-dual-sim-93925424.html'
p30_lite='https://www.jumia.com.ng/huawei-p30-lite-6.15-inch-6gb-ram-256gb-rom-android-9.048mp-8mp-2mp-dual-sim-midnight-black-71467107.html'
y9a='https://www.jumia.com.ng/huawei-y9a-6.63-8gb-ram128gb-rom-64822mp-quad-camera-16mp-motorized-selfie-.-4300mah-4g-sakura-pink-69477481.html'
psmart='https://www.jumia.com.ng/huawei-psmart2019-6.2-fhd-6gb-128gb-24mp16mp-2mp-black-123938316.html'

#Just add the product link here and fetch the price

def jumia_huawei(product_link):
    konga_url = product_link
    page = requests.get(url=konga_url)
    soup=BeautifulSoup(page.content,'lxml')
    price =soup.find('span', class_='-b -ltr -tal -fs24').text
    phone={
        'price':price
    }
    return phone['price']


print(jumia_huawei(nova9))
print(jumia_huawei(p40_pro))
print(jumia_huawei(p50_pro))
print(jumia_huawei(p10_lite))
print(jumia_huawei(nova_8i))
print(jumia_huawei(p30_pro))
print(jumia_huawei(y9))
print(jumia_huawei(p30_lite))
print(jumia_huawei(y9a))
print(jumia_huawei(psmart))
