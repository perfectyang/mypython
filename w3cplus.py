import os
from webScrawer import webScrawer
from threading import Thread as multiprocessline

allInfo = []
def parseHtml(html):
    allArticles = html.find_all(id='page')[0].select('.node-blog')
    for article in allArticles:
        title = article.select('h1')[0].get_text().replace('\n', '')
        link = 'https://www.w3cplus.com' + article.select('.node_read_more')[0].get('href')
        description = article.select('.body-content')[0].get_text()
        allInfo.append({
          'link': link,
          'title': title,
          'description': description,
        })
        print('{}---------------------成功解析!!'.format(title))

def moreProgress(allHtml):
    result = []
    for html in allHtml:
        t = multiprocessline(target=parseHtml, args=(html,))
        result.append(t)
        t.start()
    for t in result:
        t.join()

def main():
    urls = []
    allArticle = []
    for n in range(0, 1):
      urls.append('https://www.w3cplus.com/?page='.format(n))
    webscrawer = webScrawer(urls)
    webscrawer.startCrawUrl()
    moreProgress(webscrawer.backResult)
    webscrawer.saveFile('w3cplus.js', allInfo)
    print('总共数据:{}条'.format(len(allInfo)))

main()
