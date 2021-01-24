from Crawler import  CrawlerClass
from Request import ProxyTest
cr= CrawlerClass()
for ip in cr.getProxyList():
    ip="http://"+ip[0]+":"+ip[1]
    if ProxyTest(ip):
        print(ip)



