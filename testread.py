import requests
from bs4 import BeautifulSoup
import json

html = '<script>window.xvideo_id=[{"name": "\u4e2d \u6587\"}]</script>'

data = BeautifulSoup(html, 'html.parser')

htmlList = []
htmlList.append(data.text.replace('window.xvideo_id=', ''))
print('htmlList', htmlList)
# print('data', json.loads(json.dumps(data.text)))

with open('data.json', 'w', encoding='utf-8') as file:
    file.write(str(htmlList))
