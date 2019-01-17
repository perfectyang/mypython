from webScrawer import webScrawer
import pdfkit
import os
from threading import Thread as multiprocessline

def catchPage(params):
    urls = []
    for n in range(params['begin'], params['end']):
      urls.append('https://www.zhangxinxu.com/wordpress/page/{}/'.format(n))
    webscrawer = webScrawer(urls)
    webscrawer.startCrawUrl()
    allHTML = webscrawer.backResult

    def pdf(curLink, title):
        confg = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
        pdfkit.from_url(curLink, os.path.join(os.getcwd(), 'pdfbook', '{}.pdf'.format(title)), configuration=confg)
        print('--------{}--下载成功!!'.format(title))

    def quickPdf(pdfUrl):
        result = []
        for curUrl in pdfUrl:
            t = multiprocessline(target=pdf, args=(curUrl['link'], curUrl['title']))
            result.append(t)
            t.start()
        for t in result:
            t.join()

    allLinks = []
    for html in allHTML:
        allLink = html.find_all(id='content')[0].select('.entry-title')
        for link in allLink:
            curLink = link.get('href')
            title = link.get_text()
            allLinks.append({
              'link': curLink,
              'title': title
            })
    quickPdf(allLinks)

#
numbList = [
  # {
  #   'begin': 1,
  #   'end': 10
  # },
  {
    'begin': 10,
    'end': 20
  },
  {
    'begin': 20,
    'end': 10
  },
  {
    'begin': 30,
    'end': 40
  },
   {
     'begin': 40,
     'end': 50
   },
   {
     'begin': 50,
     'end': 60
   },
   {
     'begin': 60,
     'end': 64
   }
]

for params in numbList:
    catchPage(params)
