from bs4 import BeautifulSoup
import requests
import re


class CrawlerClass:
    def __init__(self):
        self.url = "https://free-proxy-list.net/"
        self.listIp = False

    def getProxyList(self):
        if not self.listIp : self.listIp = self.Crawl()
        return self.listIp

    def Crawl(self):
        html = self.DownloadHtml()
        if not html: return False
        craw = BeautifulSoup(html, 'html.parser')
        tr = craw.select_one("body textarea")
        return re.findall(r"([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\:([0-9]{1,5})?", tr.text)

    def DownloadHtml(self):
        req = requests.get(self.url)
        if req.status_code == 200:
            return req.text
        else:
            return False
