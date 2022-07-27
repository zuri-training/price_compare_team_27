import requests
from bs4 import BeautifulSoup

pova_neo='https://www.konga.com/product/tecno-pova-neo-le6-6-8-hd-64gb-rom-4gb-ram-13mp-8mp-4g-lte-6000mah-fingerprint-blue-5554576?seller_id=67157&sku_id=5554576&sclid=09wZqDUpdKygv1CZEcktnDI9Jp2Ig8JY'
pop6_go='https://www.konga.com/product/tecno-pop-6-go-be6-6-screen-32gb-rom-2gb-ram-5mp-5mp-4000mah-fingerprint-grey-5740575?seller_id=67157&sku_id=5740575&sclid=CmyvmH6o0ROVhVkvkcfxtQsIdyvcHi11'
pop5='https://www.konga.com/product/tecno-pop-5-bd2p-dual-sim-6-1-2gb-ram-32gb-rom-5000mah-blue-5308694?seller_id=67157&sku_id=5308694&sclid=EivpTjfvs2xcDGYYJkrireSb91vrRvYY'
camon_18i='https://www.konga.com/product/tecno-camon-18i-6-6-5000mah-128gb-rom-4gb-ram-grey-5796767'
camon_17pro='https://www.konga.com/product/tecno-camon-17-pro-6-8-256gb-rom-8gb-ram-dual-sim-5516738'
pop5_pro='https://www.konga.com/product/tecno-pop-5-pro-6-52-hd-2gb-ram-32gb-rom-6000mah-android-11-deepsea-luster-5653507'
pova2='https://www.konga.com/product/tecno-pova-2-128gb-6gb-7000mah-battery-6-9-display-android-11-polar-silver-color-5625108'
spark_8c='https://www.konga.com/product/tecno-spark-8c-kg5j-6-6-hd-64gb-rom-2gb-ram-13mp-8mp-4g-lte-5000mah-black-5684006'
spark_9t='https://www.konga.com/product/tecno-spark-9t-6-6-hd-64gb-rom-4gb-ram-dual-sim-4glte-fingerprint-5000mah-black-5784631'
camon18_premier='https://www.konga.com/product/tecno-camon-18-premier-6-7-256gb-rom-8gb-ram-dual-sim-4g-lte-4750mah-vast-sky-5477598'

#Just add the product link here and fetch the price

def konga_tecno(product_link):
    jumia_url= product_link
    page = requests.get(url=jumia_url)
    soup=BeautifulSoup(page.content,'lxml')
    price =soup.find('div', class_='_678e4_e6nqh').text
    phone={
        'price':price
    }
    return phone["price"]

print(konga_tecno(pova_neo))
print(konga_tecno(pop6_go))
print(konga_tecno(pop5))
print(konga_tecno(camon_18i))
print(konga_tecno(camon_17pro))
print(konga_tecno(pop5_pro))
print(konga_tecno(pova2))
print(konga_tecno(spark_8c))
print(konga_tecno(spark_9t))
print(konga_tecno(camon18_premier))
    

