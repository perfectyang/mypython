import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import threading
def getUrl(url, data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    try:
        # 获取网页内容，返回html数据
        response = requests.get(url, headers=headers)
        # print('response', response.text)
        # 通过状态码判断是否获取成功
        if response.status_code == 200:
            html = BeautifulSoup(response.text, 'html.parser')
            # print('html', html)
            result = html
            if result:
                site = result.find_all(class_="site-piclist_pic")
                for siteLink in site:
                    aLink = siteLink.find('a')
                    if aLink:
                       data.append({
                         'title': aLink.get('title'),
                         'link': aLink.get('href'),
                         'sourceLink': config['parseURL']+aLink.get('href'),
                         'imgUrl': aLink.find('img').get('src')
                       })
            return html
        return None
    except RequestException as e:
        return None

def allPage(index):
    link = f'http://list.iqiyi.com/www/1/-------------11-{index}-1-iqiyi--.html'
    return getUrl(link)

data = []
config = {
    "pageMaxNum":"20",
    "parseURL":"http://vip.jlsprh.com/index.php?url="
}

def main():
    tList = []
    for i in range(1, 100):
        t = threading.Thread(target=allPage, args=(i, data))
        t.start()
        tList.append(t)
    for tline in tList:
        tline.join()
    print('data', data)
    with open('moive5.js', 'w+') as f:
        f.write(str(data))
if __name__ == '__main__':
    main()
