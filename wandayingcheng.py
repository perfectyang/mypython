import requests
from bs4 import BeautifulSoup
import re
import json
from threading import Thread as moreLine
response = requests.get('http://www.wandayingcheng.com/dongzuopian/')
html = BeautifulSoup(response.text, 'html.parser')
allMoive = html.find_all(class_='box-video-list')[0].find_all("li")
allLink = []
for moive in allMoive:
    aContent = moive.find('a')
    print('aContent', aContent)
    if aContent:
        allLink.append({
            'title': aContent.get('title'),
            'href':  'http://www.wandayingcheng.com' + aContent.get('href')
        })

def getMoiveUrl(url, dataList):
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    res = re.search('zanpiancms_player\s*=\s*({.*?})', str(html), re.S)
    # print('res', res)
    if res:
        url = res.group(1)
        realUrl = re.sub(r'\\/', '/', url)
        realUrl = re.sub(r'(null)', r'"\1"', realUrl)
        objs = json.loads(realUrl)
        # print('真', objs)
        dataList.append(objs)

def getContent(link, dataList):
    response = requests.get(link['href'])
    html = BeautifulSoup(response.text, 'html.parser')
    playList = html.find(class_="playlist")
    if playList:
        links = html.find(class_="playlist").find('a').get('href')
        getMoiveUrl('http://www.wandayingcheng.com/' + links, dataList)

dataList = []
reT = []
for link in allLink:
    t = moreLine(target=getContent, args=(link, dataList))
    t.start()
    reT.append(t)
for tlink in reT:
    tlink.join()
print('dataList', dataList)
with open('dataList.json', 'w+') as f:
    f.write(str(dataList))
