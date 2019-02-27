import requests
import json

url = "http://zipcloud.ibsnet.co.jp/api/search?zipcode=6711523"
r = requests.get(url).json()

zipcode = (r['results'][0]['zipcode'])
address1 = (r['results'][0]['address1'])
address2 = (r['results'][0]['address2'])
kana1 = (r['results'][0]['kana1'])
kana2 = (r['results'][0]['kana2'])
print ("〒" + zipcode + "\n" + address1 + "(" + kana1 +")\n" + address2 + "(" + kana2 +")")
