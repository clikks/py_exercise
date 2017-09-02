import requests
import time
from lxml import etree
from selenium import webdriver

class Proxies:
    def __init__(self,index=None,proxy_page=None,header={},pagination=2):
        print('Inital proxies web page!')
        self.pagination = pagination
        self.index = 'http://www.kuaidaili.com/free'
        self.proxy_page = 'http://www.kuaidaili.com/free/inha/%s/' %(self.pagination)
        self.header = {
                        'Accept': '*/*',
                        'Accept-Encoding' : 'gzip, deflate, sdch',
                        'Accept-Language' : 'zh-CN,zh;q=0.8',
                        'Connection' : 'keep-alive',
                        'Cookie' : '_ydclearance=7804918e590341298e145d56-196e-407a-b8c6-344b27429c10-1504190752;\
                         yd_cookie=2f8d5e6e-b32d-40acac5ecc15f44a5c5fc766c00ebb7471cd; _ga=GA1.2.679627446.1504107640; \
                         _gid=GA1.2.1010858908.1504107640; _gat=1; \
                         Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1504107640,1504109383,1504185178; \
                         Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1504185178; channelid=0; sid=1504184953373567',
                        'Host' : 'www.kuaidaili.com',
                        'Referer' : 'http://www.kuaidaili.com/',
                        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                         Chrome/55.0.2883.87 Safari/537.36',
                        'X-Requested-With' : 'XMLHttpRequest',
                        }

    def page_count(self):
        while True:
            req = requests.session()
            html_page = req.get(self.index, headers=self.header, timeout=5)
            print(self.header)
            #         print(html_page.text)
            if html_page.status_code != 200:
                print('Request status code is %d' % html_page.status_code)
                # time.sleep(60)
                continue
            else:
                result = etree.HTML(html_page.text)
                pagecount = result.xpath('/html/body/div[@class="body"]/div[@id="content"]/div[@class="con-body"]\
                /div/div[@id="list"]/div[@id="listnav"]/ul/li[last()-1]/a/text()')
                return int(pagecount[0])
                break

# Lastcontent = Proxies()
# Lastcontent.page_count()

firfoxPath = r'D:\webdrive\geckodriver.exe'
wd = webdriver.Firefox(executable_path = firfoxPath)
wd.get('http://www.kuaidaili.com/free')
req = requests.session()
cookies = wd.get_cookies()
print(cookies)