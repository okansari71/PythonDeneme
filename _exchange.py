import requests
import json


api_key = "bff7ff78075f0b35b3e74da1"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("bozulan döviz kuru: ")
alinan_doviz = input("aliınan döviz türü: ")
miktar = int (input(f"ne kadar döviz {bozulan_doviz} bozdurmak istiyorsunuz: "))

sonuc = requests.get(api_url + bozulan_doviz)
sonuc_json = json.loads(sonuc.text)

# print(sonuc_json["conversion_rates"][alinan_doviz])

print("1 {0} = {1}{2}".format(bozulan_doviz,sonuc_json["conversion_rates"][alinan_doviz],alinan_doviz))
print("{0} {1} = {2}{3}".format(miktar, bozulan_doviz, miktar * sonuc_json["conversion_rates"][alinan_doviz],alinan_doviz))



