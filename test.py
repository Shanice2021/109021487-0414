import requests
from bs4 import BeautifulSoup
url = 'https://csie.asia.edu.tw/project/semester-10{0}'
headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
def generate_urls(url,sp,ep):
    urls = []
    for p in range (sp,ep):
        if( int(p) == 6):
            urls.append(url.format(61))
        else:
            urls.append(url.format(p))
    urls.append("https://csie.asia.edu.tw/project/108學年")
    return urls
def abc(url):
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
    return Ysoup
if __name__ == "__main__":
    urls =generate_urls(url, 0, 8)
    work =abc(urls)
    for i in work:
        print(i)
