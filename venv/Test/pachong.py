from bs4 import BeautifulSoup
import requests
import time

url = 'http://www.runoob.com/python/python-100-examples.html'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
}
r = requests.get(url, headers=headers).content.decode('utf8')
soup_start = BeautifulSoup(r, 'html.parser')
links = soup_start.find(id='content').find_all("a", limit=100)
num = 1
for i in links:
    url2 = 'http://www.runoob.com' + i.attrs["href"]
    r2 = requests.get(url2, headers=headers).content.decode('utf8')
    soup_title = BeautifulSoup(r2, "html.parser")
    title = soup_title.find(id='content').find_all('p')[1].text
    try:
        answer = soup_title.find(id='content').find_all(class_='hl-main')[0].text
    except:
        answer = soup_title.find(id='content').find_all('pre')[0].text

    with open("python100.txt", 'a+') as file:
        file.write(title + '\n' + answer + '\n' + '-' * 60 + '\n')
    print('爬取页数{}', format(num))
    num += 1
