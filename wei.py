import requests
import time
import csv
import random
from bs4 import BeautifulSoup


requests.packages.urllib3.disable_warnings()

URL = "https://csie.asia.edu.tw/project/semester-10{0}"

def generate_urls(url,start_page, end_page):
    urls = []
    for page in range (start_page, end_page):
        if( int(page) == 6):
            urls.append(url.format(61))
        elif( int(page) != 6 ):
            urls.append(url.format(page))
    urls.append("https://csie.asia.edu.tw/project/108學年")
    return urls



def get_resource(url):
    headers ={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0;Win64; x64) APPLWebKit/537.36 (KHTML,like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    
    return requests.get(url,headers=headers,verify=False)

def parse_html(html_str):
    return BeautifulSoup(html_str,"lxml")


def get_word(soup,file):
    words = []
    count = 0
    for wordlist_table in soup.find_all(class_="table table-bordered table-hover"):
        count += 1
        for word_entry in wordlist_table.find_all("tr"):
            new_word = []
            new_word.append(file)
            new_word.append(str(count))
            new_word.append(word_entry.text)
            words.append(new_word)
    return words
def web_scraping_bog(urls):
    eng_words = []
    for url in urls:
        file = url.split("/")[-1]
        print("catching:",file,"web data...")
        r = get_resource(url)
        if r.status_code == requests.codes.ok:
            soup = parse_html(r.text)
            words = get_word(soup, file)
            eng_words = eng_words + words
            print("waiting 3~7 seconds...")
            time.sleep(random.randint(3,7))
        else:
            print("HTTP requesterror!!")
    return eng_words


def save_to_csv(words, file):
    with open(file, "w+",newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp)
        for word in words:
            writer.writerow(word)
if __name__ == "__main__":
    urlx =generate_urls(URL, 0, 8)
    eng_words = web_scraping_bog(urlx)
    for item in eng_words:
        print(item)
    save_to_csv(eng_words, "projectsList.csv")