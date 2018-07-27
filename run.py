# import os
# import requests
# #
# # currentPath = os.path.join(os.getcwd(), 'img2')
# # print(currentPath)
# # headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
# #             'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
# #             'Accept-Encoding':'gzip'
# #            }
# # torrentLink = 'https://torrents.linuxmint.com/torrents/linuxmint-19-cinnamon-64bit.iso.torrent'
# #
# # res = requests.get(torrentLink, headers=headers)
# #
# # allFiles = os.listdir(os.getcwd())
# # k = 0
# # for files in allFiles:
# #     # os.rename(files, 'new' + k)
# #     if files != 'run.py':
# #         print('files', files[-3:])
# #         os.rename(files, 'new-' + str(k))
# #         k += 1



from bs4 import BeautifulSoup
import requests ##导入requests
import os
import uuid
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'Accept-Encoding':'gzip'
}
URL_1024="https://torrents.linuxmint.com/torrents/linuxmint-19-cinnamon-64bit.iso.torrent"
start_html = requests.get(URL_1024,  headers=headers)
start_html.encoding='utf-8'
bsObj = BeautifulSoup(start_html.text,'html.parser')
imgPath = r'/Users/perfectyang/Desktop/project/learn/py3'
torrenName = str(uuid.uuid3()) + '.torrent'
with open(os.path.join(imgPath, torrenName), 'wb') as f:
     f.write(start_html.content)
print('bsobj', start_html.content)
