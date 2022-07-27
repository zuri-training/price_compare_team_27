import requests
from bs4 import BeautifulSoup

pova_neo='https://www.jumia.com.ng/tecno-pova-neo-le6-6.8-hd-4gb-ram-64gb-rom-6000mah-battery-18w-charge-13mp-8mp-camera-android-11-4g-lte-black-92402560.html'
pop6_go='https://www.jumia.com.ng/tecno-pop-6-go6.0-2gb-ram-32gb-rom-4000mah-5mp-5mp-grey-123293724.html'
pop5='https://www.jumia.com.ng/tecno-pop-5-bd2d-6.1-hd-display-2gb-ram-32gb-rom-5000mah-android-10-5mp-5mp-camera-fingerprint-face-id-black-78011919.html'
camon_18i='https://www.jumia.com.ng/tecno-camon-18i-cg6-6.6-90hz-hd-4gb-ram-128gb-rom-48mp-triple-rear8mp-selfie-camera-android-11-5000mah-4g-blue-87815399.html'
camon_17pro='https://www.jumia.com.ng/camon-17-pro-cg8-6.8-256gb-rom-8gb-ram-64mp-quad-rear-48mp-selfie-5000mah-4g-lte-malibublue-tecno-mpg1624354.html'
pop5_pro='https://www.jumia.com.ng/pop-5-pro-bd4j-6.52-hd-2gb-ram-32gb-rom-6000mah-battery-8mp-5mp-camera-4g-android-11-fingerprint-blue-tecno-mpg1648268.html'
pova2='https://www.jumia.com.ng/tecno-pova-2-6.9-fhd-6gb-ram-128gb-rom-android-11-48mp-ai-quad-camera-8mp-selfie-4g-7000mah-battery-polar-silver-91592242.html'
spark_8c='https://www.jumia.com.ng/tecno-spark-8c-6.62gb64gb5000mah-magnet-black-132879311.html'
spark_9t='https://www.jumia.com.ng/tecno-spark-9t-kh6-6.6-hd-90hz-64gb-rom-4gb-rom-up-to-7gb-5000mah-android-12-32mp-selfie-4g-fingerprint-blue-139397680.html'
camon18_premier='https://www.jumia.com.ng/tecno-camon-18-premier-ch9-6.7-fhd-8gb-ram-256gb-rom-64mp-93327467.html'

#Just add the product link here and fetch the price

def jumia_tecno(product_link):
    jumia_url= product_link
    page = requests.get(url=jumia_url)
    soup=BeautifulSoup(page.content,'lxml')
    price =soup.find('span', class_='-b -ltr -tal -fs24').text
    phone={
        'price':price
    }
    return phone["price"]
    
print(jumia_tecno(pova_neo))
print(jumia_tecno(pop6_go))
print(jumia_tecno(pop5))
print(jumia_tecno(camon_18i))
print(jumia_tecno(camon_17pro))
print(jumia_tecno(pop5_pro))
print(jumia_tecno(pova2))
print(jumia_tecno(spark_8c))
print(jumia_tecno(spark_9t))
print(jumia_tecno(camon18_premier))
 
