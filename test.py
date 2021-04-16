import requests
from bs4 import BeautifulSoup
url = 'https://csie.asia.edu.tw/project/semester-101'
headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }

r=requests.get(url,headers=headers,verify=False)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text, 'lxml') #lxml = html.parser
soup = soup.find('tbody')
Ysoup = soup.find_all('p')
Nsoup = soup.find_all('a')
Ysoup = str(Ysoup)
Nsoup = str(Nsoup)
Ysoup=Ysoup.replace('<p>',"")
Nsoup=Nsoup.replace('<p>',"")
Ysoup=Ysoup.replace('</p>',"")
Nsoup=Nsoup.replace('</p>',"")
Ysoup=list(Ysoup.split(','))
Nsoup=list(Nsoup.split(','))
for i in Ysoup:
    print(i)